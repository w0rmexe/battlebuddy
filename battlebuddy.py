"""
BattleBuddy Discord Bot
A bot that helps users select random characters from various games.

Features:
- Random character selection from multiple games
- Character statistics tracking
- User favorites management
- Role-based character filtering
- Command cooldown system
- Detailed character information display

The bot uses slash commands for better user experience and includes
features like cooldowns to prevent spam and database persistence
for tracking statistics and favorites.
"""

import discord
from discord import app_commands
from discord.ext import commands
import random as random_module
import os
import logging
from dotenv import load_dotenv
from config import CHARACTERS, COMMAND_PREFIX, BOT_DESCRIPTION, COMMAND_COOLDOWN
from datetime import datetime, timedelta
import sqlite3
from typing import Optional, Dict, List, Tuple

# Set up logging with both file and console handlers
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('battlebuddy.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    logger.error("No Discord token found in environment variables!")
    raise ValueError("DISCORD_TOKEN environment variable is required")

# Initialize bot with required intents
intents = discord.Intents.default()
intents.message_content = True  # Required for message content access
intents.members = True          # Required for member-related operations
intents.guilds = True          # Required for server-related operations
bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents, description=BOT_DESCRIPTION)

# Global dictionary to track user command cooldowns
# Format: {user_id: datetime when cooldown expires}
cooldowns: Dict[int, datetime] = {}

class Database:
    """Database class to handle character statistics and user favorites.
    
    This class manages all database operations including:
    - Character pick statistics tracking
    - User favorites management
    - Database initialization and connection handling
    """
    
    def __init__(self):
        """Initialize database connection and create necessary tables."""
        self.conn = sqlite3.connect('battlebuddy.db')
        self.cursor = self.conn.cursor()
        self.create_tables()
    
    def create_tables(self):
        """Create database tables if they don't exist.
        
        Creates two main tables:
        1. character_stats: Tracks pick statistics for each character
        2. user_favorites: Stores user's favorite characters
        """
        # Table for tracking character pick statistics
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS character_stats (
                game TEXT,
                character TEXT,
                picks INTEGER DEFAULT 0,
                PRIMARY KEY (game, character)
            )
        ''')
        
        # Table for storing user favorites
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_favorites (
                user_id INTEGER,
                game TEXT,
                character TEXT,
                PRIMARY KEY (user_id, game, character)
            )
        ''')
        self.conn.commit()
    
    def record_character_pick(self, game: str, character: str):
        """Record a character pick in the statistics.
        
        Args:
            game (str): The game name (e.g., 'apex', 'overwatch')
            character (str): The character name that was picked
            
        Note:
            Uses SQLite's UPSERT functionality to either insert a new record
            or increment the pick count for existing records
        """
        self.cursor.execute('''
            INSERT INTO character_stats (game, character, picks)
            VALUES (?, ?, 1)
            ON CONFLICT(game, character) DO UPDATE SET picks = picks + 1
        ''', (game, character))
        self.conn.commit()
    
    def get_character_stats(self, game: Optional[str] = None) -> List[Tuple]:
        """Retrieve character pick statistics, optionally filtered by game.
        
        Args:
            game (Optional[str]): If provided, filter stats for this game only
            
        Returns:
            List[Tuple]: List of tuples containing (character, picks) or (game, character, picks)
                        depending on whether game filter is applied
        """
        if game:
            self.cursor.execute('''
                SELECT character, picks FROM character_stats
                WHERE game = ? ORDER BY picks DESC
            ''', (game,))
        else:
            self.cursor.execute('''
                SELECT game, character, picks FROM character_stats
                ORDER BY game, picks DESC
            ''')
        return self.cursor.fetchall()
    
    def add_favorite(self, user_id: int, game: str, character: str):
        """Add a character to a user's favorites.
        
        Args:
            user_id (int): Discord user ID
            game (str): Game name
            character (str): Character name to add as favorite
        """
        self.cursor.execute('''
            INSERT INTO user_favorites (user_id, game, character)
            VALUES (?, ?, ?)
        ''', (user_id, game, character))
        self.conn.commit()
    
    def remove_favorite(self, user_id: int, game: str, character: str):
        """Remove a character from a user's favorites.
        
        Args:
            user_id (int): Discord user ID
            game (str): Game name
            character (str): Character name to remove from favorites
        """
        self.cursor.execute('''
            DELETE FROM user_favorites
            WHERE user_id = ? AND game = ? AND character = ?
        ''', (user_id, game, character))
        self.conn.commit()
    
    def get_favorites(self, user_id: int) -> List[Tuple[str, str]]:
        """Get all favorite characters for a user.
        
        Args:
            user_id (int): Discord user ID
            
        Returns:
            List[Tuple[str, str]]: List of (game, character) tuples
        """
        self.cursor.execute('''
            SELECT game, character FROM user_favorites
            WHERE user_id = ?
        ''', (user_id,))
        return self.cursor.fetchall()

# Initialize database
db = Database()

def check_cooldown(user_id: int) -> bool:
    """Check if a user is on cooldown for commands.
    
    Args:
        user_id (int): Discord user ID to check
        
    Returns:
        bool: True if user can use commands, False if on cooldown
    """
    if user_id in cooldowns:
        if datetime.now() < cooldowns[user_id]:
            return False
    return True

def set_cooldown(user_id: int):
    """Set cooldown for a user after command use.
    
    Args:
        user_id (int): Discord user ID to set cooldown for
    """
    cooldowns[user_id] = datetime.now() + timedelta(seconds=COMMAND_COOLDOWN)

@bot.event
async def on_ready():
    """Event handler for when the bot is ready.
    
    Performs two main tasks:
    1. Logs successful bot login
    2. Syncs slash commands with Discord
    
    Note:
        Command sync is required for slash commands to work properly
        and must be done after the bot is ready
    """
    logger.info(f'Logged in as {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        logger.info(f"Synced {len(synced)} command(s)")
    except Exception as e:
        logger.error(f"Failed to sync commands: {e}")

@bot.tree.command(name="who", description="Select a random character from a game")
async def who(interaction: discord.Interaction, game: str, role: Optional[str] = None):
    """Select a random character from a specified game, optionally filtered by role"""
    try:
        if not check_cooldown(interaction.user.id):
            remaining = (cooldowns[interaction.user.id] - datetime.now()).seconds
            await interaction.response.send_message(
                f"Please wait {remaining} seconds before using this command again.",
                ephemeral=True
            )
            return

        game = game.lower()
        if game not in CHARACTERS:
            await interaction.response.send_message(
                f"Game '{game}' not found. Available games: {', '.join(CHARACTERS.keys())}",
                ephemeral=True
            )
            return

        characters = CHARACTERS[game]['characters']
        if role:
            role = role.capitalize()
            if role not in CHARACTERS[game]['roles']:
                await interaction.response.send_message(
                    f"Role '{role}' not found for {game}. Available roles: {', '.join(CHARACTERS[game]['roles'])}",
                    ephemeral=True
                )
                return
            characters = [c for c in characters if CHARACTERS[game]['role_mapping'][c] == role]

        character = random_module.choice(characters)
        db.record_character_pick(game, character)
        set_cooldown(interaction.user.id)

        embed = discord.Embed(
            title="Character Selected",
            description=f"Selected: **{character}**",
            color=discord.Color.green()
        )
        embed.add_field(name="Game", value=game.capitalize(), inline=False)
        embed.add_field(name="Role", value=CHARACTERS[game]['role_mapping'][character], inline=False)
        embed.set_footer(text=f"Requested by {interaction.user.name}")

        await interaction.response.send_message(embed=embed)
    except Exception as e:
        logger.error(f"Error in who command: {e}")
        await interaction.response.send_message(
            "An error occurred while processing your command. Please try again.",
            ephemeral=True
        )

@bot.tree.command(name="random", description="Select a random character from any game")
async def random(interaction: discord.Interaction):
    """Select a random character from any game"""
    try:
        if not check_cooldown(interaction.user.id):
            remaining = (cooldowns[interaction.user.id] - datetime.now()).seconds
            await interaction.response.send_message(
                f"Please wait {remaining} seconds before using this command again.",
                ephemeral=True
            )
            return

        game = random_module.choice(list(CHARACTERS.keys()))
        character = random_module.choice(CHARACTERS[game]['characters'])
        db.record_character_pick(game, character)
        set_cooldown(interaction.user.id)

        embed = discord.Embed(
            title="Random Character",
            description=f"Selected: **{character}**",
            color=discord.Color.green()
        )
        embed.add_field(name="Game", value=game.capitalize(), inline=False)
        embed.add_field(name="Role", value=CHARACTERS[game]['role_mapping'][character], inline=False)
        embed.set_footer(text=f"Requested by {interaction.user.name}")

        await interaction.response.send_message(embed=embed)
    except Exception as e:
        logger.error(f"Error in random command: {e}")
        await interaction.response.send_message(
            "An error occurred while processing your command. Please try again.",
            ephemeral=True
        )

@bot.tree.command(name="stats", description="View character pick statistics")
async def stats(interaction: discord.Interaction, game: Optional[str] = None):
    """Display character pick statistics, optionally filtered by game"""
    try:
        stats = db.get_character_stats(game)
        if not stats:
            await interaction.response.send_message(
                "No statistics available yet.",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="Character Statistics",
            description="Character pick statistics:",
            color=discord.Color.blue()
        )

        if game:
            for character, picks in stats:
                embed.add_field(name=character, value=f"Picks: {picks}", inline=True)
        else:
            current_game = None
            for game_name, character, picks in stats:
                if current_game != game_name:
                    current_game = game_name
                    embed.add_field(name=game_name.capitalize(), value="", inline=False)
                embed.add_field(name=character, value=f"Picks: {picks}", inline=True)

        embed.set_footer(text=f"Requested by {interaction.user.name}")
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        logger.error(f"Error in stats command: {e}")
        await interaction.response.send_message(
            "An error occurred while processing your command. Please try again.",
            ephemeral=True
        )

@bot.tree.command(name="favorite", description="Add/remove a character from your favorites")
async def favorite(interaction: discord.Interaction, game: str, character: str):
    """Add or remove a character from a user's favorites"""
    try:
        game = game.lower()
        if game not in CHARACTERS:
            await interaction.response.send_message(
                f"Game '{game}' not found. Available games: {', '.join(CHARACTERS.keys())}",
                ephemeral=True
            )
            return

        if character not in CHARACTERS[game]['characters']:
            await interaction.response.send_message(
                f"Character '{character}' not found in {game}.",
                ephemeral=True
            )
            return

        favorites = db.get_favorites(interaction.user.id)
        is_favorite = any(f[0] == game and f[1] == character for f in favorites)

        if is_favorite:
            db.remove_favorite(interaction.user.id, game, character)
            action = "removed from"
        else:
            db.add_favorite(interaction.user.id, game, character)
            action = "added to"

        embed = discord.Embed(
            title="Favorite Updated",
            description=f"**{character}** has been {action} your favorites.",
            color=discord.Color.green()
        )
        embed.add_field(name="Game", value=game.capitalize(), inline=False)
        embed.set_footer(text=f"Requested by {interaction.user.name}")

        await interaction.response.send_message(embed=embed)
    except Exception as e:
        logger.error(f"Error in favorite command: {e}")
        await interaction.response.send_message(
            "An error occurred while processing your command. Please try again.",
            ephemeral=True
        )

@bot.tree.command(name="favorites", description="View your favorite characters")
async def favorites(interaction: discord.Interaction):
    """Display a user's favorite characters"""
    try:
        favorites = db.get_favorites(interaction.user.id)
        if not favorites:
            await interaction.response.send_message(
                "You don't have any favorite characters yet.",
                ephemeral=True
            )
            return

        embed = discord.Embed(
            title="Your Favorites",
            description="Your favorite characters:",
            color=discord.Color.blue()
        )

        current_game = None
        for game, character in favorites:
            if current_game != game:
                current_game = game
                embed.add_field(name=game.capitalize(), value="", inline=False)
            embed.add_field(name=character, value="", inline=True)

        embed.set_footer(text=f"Requested by {interaction.user.name}")
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        logger.error(f"Error in favorites command: {e}")
        await interaction.response.send_message(
            "An error occurred while processing your command. Please try again.",
            ephemeral=True
        )

@bot.tree.command(name="help", description="Display available commands and supported games")
async def help(interaction: discord.Interaction):
    """Display help information and available commands"""
    try:
        embed = discord.Embed(
            title="BattleBuddy Help",
            description=BOT_DESCRIPTION,
            color=discord.Color.blue()
        )

        # Add commands section
        commands_text = """
        **Commands:**
        `/who [game] [role]` - Select a random character from a game (optionally filtered by role)
        `/random` - Select a random character from any game
        `/stats [game]` - View character pick statistics
        `/favorite [game] [character]` - Add/remove a character from your favorites
        `/favorites` - View your favorite characters
        `/help` - Display this help message
        """
        embed.add_field(name="Commands", value=commands_text, inline=False)

        # Add supported games section
        games_text = "**Supported Games:**\n"
        for game in CHARACTERS:
            games_text += f"\n**{game.capitalize()}**\n"
            games_text += f"Roles: {', '.join(CHARACTERS[game]['roles'])}\n"
            games_text += f"Characters: {len(CHARACTERS[game]['characters'])}"
        embed.add_field(name="Games", value=games_text, inline=False)

        embed.set_footer(text=f"Requested by {interaction.user.name}")
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        logger.error(f"Error in help command: {e}")
        await interaction.response.send_message(
            "An error occurred while processing your command. Please try again.",
            ephemeral=True
        )

# Add error handler for command errors
@bot.event
async def on_command_error(ctx, error):
    """Event handler for command errors"""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. Use `/help` to see available commands.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have permission to use this command.")
    else:
        logger.error(f"Command error: {error}")
        await ctx.send("An error occurred while processing your command.")

# Add error handler for application commands
@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    """Event handler for application command errors"""
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(
            f"This command is on cooldown. Try again in {error.retry_after:.1f}s",
            ephemeral=True
        )
    else:
        logger.error(f"Application command error: {error}")
        await interaction.response.send_message(
            "An error occurred while processing your command.",
            ephemeral=True
        )

def main():
    """Main function to run the bot"""
    try:
        bot.run(TOKEN)
    except Exception as e:
        logger.error(f"Critical error during startup: {e}")
        raise

if __name__ == "__main__":
    main()
