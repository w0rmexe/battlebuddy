"""
Script to move files to their new package structure.
"""

import os
import shutil

def move_file(src: str, dst: str):
    """Move a file from source to destination."""
    if os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.move(src, dst)
        print(f"Moved {src} to {dst}")

def main():
    """Move files to their new locations."""
    # Move main files
    move_file("battlebuddy.py", "battlebuddy/bot.py")
    move_file("database.py", "battlebuddy/database.py")
    move_file("config.py", "battlebuddy/config.py")
    move_file("test_database.py", "battlebuddy/tests/test_database.py")

if __name__ == "__main__":
    main() 