"""
Unit tests for the database module.
"""
import unittest
import os
import sqlite3
from database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        """Set up test database."""
        self.test_db_path = 'test_battlebuddy.db'
        self.db = Database(self.test_db_path)

    def tearDown(self):
        """Clean up test database."""
        if os.path.exists(self.test_db_path):
            os.remove(self.test_db_path)

    def test_init_db(self):
        """Test database initialization."""
        # Check if tables were created
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            self.assertIn(('character_stats',), tables)
            self.assertIn(('user_favorites',), tables)

    def test_record_character_pick(self):
        """Test recording character picks."""
        # Record a pick
        self.db.record_character_pick('test_game', 'test_char')
        
        # Verify the pick was recorded
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT picks, last_picked 
                FROM character_stats 
                WHERE game = ? AND character = ?
            ''', ('test_game', 'test_char'))
            result = cursor.fetchone()
            self.assertIsNotNone(result)
            self.assertEqual(result[0], 1)

        # Record another pick
        self.db.record_character_pick('test_game', 'test_char')
        
        # Verify the pick count increased
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT picks 
                FROM character_stats 
                WHERE game = ? AND character = ?
            ''', ('test_game', 'test_char'))
            result = cursor.fetchone()
            self.assertEqual(result[0], 2)

    def test_favorites(self):
        """Test favorites functionality."""
        user_id = 12345
        
        # Add favorite
        success = self.db.add_favorite(user_id, 'test_game', 'test_char')
        self.assertTrue(success)
        
        # Try to add same favorite again
        success = self.db.add_favorite(user_id, 'test_game', 'test_char')
        self.assertFalse(success)
        
        # Get favorites
        favorites = self.db.get_user_favorites(user_id)
        self.assertEqual(len(favorites), 1)
        self.assertEqual(favorites[0][0], 'test_game')
        self.assertEqual(favorites[0][1], 'test_char')
        
        # Remove favorite
        success = self.db.remove_favorite(user_id, 'test_game', 'test_char')
        self.assertTrue(success)
        
        # Verify favorite was removed
        favorites = self.db.get_user_favorites(user_id)
        self.assertEqual(len(favorites), 0)

    def test_get_character_stats(self):
        """Test getting character statistics."""
        # Record some picks
        self.db.record_character_pick('game1', 'char1')
        self.db.record_character_pick('game1', 'char1')
        self.db.record_character_pick('game1', 'char2')
        self.db.record_character_pick('game2', 'char3')
        
        # Test getting all stats
        all_stats = self.db.get_character_stats()
        self.assertEqual(len(all_stats), 3)
        
        # Test getting game-specific stats
        game1_stats = self.db.get_character_stats('game1')
        self.assertEqual(len(game1_stats), 2)
        self.assertEqual(game1_stats[0][2], 2)  # char1 should have 2 picks

if __name__ == '__main__':
    unittest.main() 