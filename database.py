"""
Database module for BattleBuddy Discord bot.
Handles character statistics and user favorites.

This module provides database operations for:
1. Tracking character pick statistics across different games
2. Managing user's favorite characters
3. Maintaining pick history and usage patterns
"""
import sqlite3
import logging
from datetime import datetime
from typing import List, Tuple, Optional

logger = logging.getLogger(__name__)

class Database:
    """Database handler for BattleBuddy bot.
    
    Manages all database operations including:
    - Character statistics tracking
    - User favorites management
    - Database initialization and connection handling
    """
    
    def __init__(self, db_path='battlebuddy.db'):
        """Initialize database connection and create necessary tables.
        
        Args:
            db_path (str): Path to the SQLite database file
        """
        self.db_path = db_path
        self.init_db()

    def get_connection(self):
        """Create and return a database connection.
        
        Returns:
            sqlite3.Connection: Database connection object
        """
        return sqlite3.connect(self.db_path)

    def init_db(self):
        """Initialize the database with required tables.
        
        Creates two main tables:
        1. character_stats: Tracks pick statistics for each character
           - game: The game name
           - character: Character name
           - picks: Number of times picked
           - last_picked: Timestamp of last pick
           
        2. user_favorites: Stores user's favorite characters
           - user_id: Discord user ID
           - game: Game name
           - character: Character name
           - added_at: When the favorite was added
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                
                # Create character statistics table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS character_stats (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        game TEXT NOT NULL,
                        character TEXT NOT NULL,
                        picks INTEGER DEFAULT 0,
                        last_picked TIMESTAMP,
                        UNIQUE(game, character)
                    )
                ''')
                
                # Create user favorites table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS user_favorites (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER NOT NULL,
                        game TEXT NOT NULL,
                        character TEXT NOT NULL,
                        added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        UNIQUE(user_id, game, character)
                    )
                ''')
                
                conn.commit()
                logger.info("Database tables initialized successfully")
        except sqlite3.Error as e:
            logger.error(f"Error initializing database: {e}")
            raise

    def record_character_pick(self, game: str, character: str):
        """Record a character pick in the statistics.
        
        Args:
            game (str): The game name (e.g., 'apex', 'overwatch')
            character (str): The character name that was picked
            
        Note:
            Uses SQLite's UPSERT functionality to either insert a new record
            or increment the pick count for existing records
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO character_stats (game, character, picks, last_picked)
                    VALUES (?, ?, 1, CURRENT_TIMESTAMP)
                    ON CONFLICT(game, character) DO UPDATE 
                    SET picks = picks + 1, last_picked = CURRENT_TIMESTAMP
                ''', (game, character))
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error recording character pick: {e}")
            raise

    def get_character_stats(self, game: Optional[str] = None) -> List[Tuple]:
        """Retrieve character pick statistics, optionally filtered by game.
        
        Args:
            game (Optional[str]): If provided, filter stats for this game only
            
        Returns:
            List[Tuple]: List of tuples containing (character, picks) or (game, character, picks)
                        depending on whether game filter is applied
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                if game:
                    cursor.execute('''
                        SELECT character, picks FROM character_stats
                        WHERE game = ? ORDER BY picks DESC
                    ''', (game,))
                else:
                    cursor.execute('''
                        SELECT game, character, picks FROM character_stats
                        ORDER BY game, picks DESC
                    ''')
                return cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Error retrieving character stats: {e}")
            raise

    def add_favorite(self, user_id: int, game: str, character: str):
        """Add a character to a user's favorites.
        
        Args:
            user_id (int): Discord user ID
            game (str): Game name
            character (str): Character name to add as favorite
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO user_favorites (user_id, game, character)
                    VALUES (?, ?, ?)
                ''', (user_id, game, character))
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error adding favorite: {e}")
            raise

    def remove_favorite(self, user_id: int, game: str, character: str):
        """Remove a character from a user's favorites.
        
        Args:
            user_id (int): Discord user ID
            game (str): Game name
            character (str): Character name to remove from favorites
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    DELETE FROM user_favorites
                    WHERE user_id = ? AND game = ? AND character = ?
                ''', (user_id, game, character))
                conn.commit()
        except sqlite3.Error as e:
            logger.error(f"Error removing favorite: {e}")
            raise

    def get_favorites(self, user_id: int) -> List[Tuple[str, str]]:
        """Get all favorite characters for a user.
        
        Args:
            user_id (int): Discord user ID
            
        Returns:
            List[Tuple[str, str]]: List of (game, character) tuples
        """
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT game, character FROM user_favorites
                    WHERE user_id = ?
                ''', (user_id,))
                return cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Error retrieving favorites: {e}")
            raise 