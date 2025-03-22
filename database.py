"""
Database module for BattleBuddy Discord bot.
Handles character statistics and user favorites.
"""
import sqlite3
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class Database:
    def __init__(self, db_path='battlebuddy.db'):
        self.db_path = db_path
        self.init_db()

    def get_connection(self):
        """Create and return a database connection."""
        return sqlite3.connect(self.db_path)

    def init_db(self):
        """Initialize the database with required tables."""
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
                logger.info("Database initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing database: {e}")
            raise

    def record_character_pick(self, game: str, character: str):
        """Record a character pick in the statistics."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO character_stats (game, character, picks, last_picked)
                    VALUES (?, ?, 1, ?)
                    ON CONFLICT(game, character) 
                    DO UPDATE SET picks = picks + 1, last_picked = ?
                ''', (game, character, datetime.now(), datetime.now()))
                conn.commit()
        except Exception as e:
            logger.error(f"Error recording character pick: {e}")
            raise

    def get_character_stats(self, game: str = None):
        """Get statistics for all characters or for a specific game."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                if game:
                    cursor.execute('''
                        SELECT game, character, picks, last_picked
                        FROM character_stats
                        WHERE game = ?
                        ORDER BY picks DESC
                    ''', (game,))
                else:
                    cursor.execute('''
                        SELECT game, character, picks, last_picked
                        FROM character_stats
                        ORDER BY game, picks DESC
                    ''')
                return cursor.fetchall()
        except Exception as e:
            logger.error(f"Error getting character stats: {e}")
            raise

    def add_favorite(self, user_id: int, game: str, character: str):
        """Add a character to a user's favorites."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO user_favorites (user_id, game, character)
                    VALUES (?, ?, ?)
                ''', (user_id, game, character))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False  # Already in favorites
        except Exception as e:
            logger.error(f"Error adding favorite: {e}")
            raise

    def remove_favorite(self, user_id: int, game: str, character: str):
        """Remove a character from a user's favorites."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    DELETE FROM user_favorites
                    WHERE user_id = ? AND game = ? AND character = ?
                ''', (user_id, game, character))
                conn.commit()
                return cursor.rowcount > 0
        except Exception as e:
            logger.error(f"Error removing favorite: {e}")
            raise

    def get_user_favorites(self, user_id: int):
        """Get all favorites for a user."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT game, character, added_at
                    FROM user_favorites
                    WHERE user_id = ?
                    ORDER BY added_at DESC
                ''', (user_id,))
                return cursor.fetchall()
        except Exception as e:
            logger.error(f"Error getting user favorites: {e}")
            raise 