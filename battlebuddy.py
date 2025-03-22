import discord
from discord.ext import commands
from dislash import slash_command
import random

# Add your token here
TOKEN = 'your_token_here'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@slash_command(name="who", description="Picks a random character from a game")
async def who(ctx, game: str):
    # Create a dictionary of characters for each game
    characters = {
        'apex': ['Ash', 'Bangalore', 'Bloodhound', 'Catalyst', 'Caustic', 'Crypto', 'Fuse',
                        'Gibraltar', 'Horizon', 'Lifeline', 'Loba', 'Mad Maggie', 'Mirage', 'Newcastle', 'Octane',
                        'Pathfinder', 'Rampart', 'Revenant', 'Seer', 'Valkyrie', 'Vantage', 'Wattson', 'Wraith'],
        'overwatch': ['Ana', 'Ashe', 'Baptiste', 'Bastion', 'Brigitte', 'Cassidy', 'D.Va', 'Doomfist', 'Echo',
                             'Genji', 'Hanzo', 'Junker Queen', 'Junkrat', 'Kiriko', 'Lúcio',
                             'Mei', 'Mercy', 'Moira', 'Orisa', 'Pharah', 'Ramattra',
                             'Reaper', 'Reinhardt', 'Roadhog', 'Sigma', 'Soldier: 76', 'Sojourn',
                             'Sombra', 'Symmetra', 'Torbjörn', 'Tracer', 'Widowmaker',
                             'Winston', 'Wrecking Ball', 'Zarya', 'Zenyatta'],
        'valorant': ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 'Fade',
                            'Gekko', 'Harbor', 'Jett', 'Kay/o', 'Killjoy', 'Neon', 'Omen', 'Phoenix', 'Raze',
                            'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru']
    }

    # Pick a random character from the corresponding game
    if game.lower() in characters:
        chosen_character = random.choice(characters[game.lower()])
        await ctx.send(f'Your random character for {game} is {chosen_character}!')
    else:
        await ctx.send('Sorry, I do not recognize that game.')

# Start the bot
