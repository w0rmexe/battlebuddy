"""
Cooldown utility functions for command rate limiting.
"""

from datetime import datetime, timedelta
from typing import Dict

# Global dictionary to track user command cooldowns
# Format: {user_id: datetime when cooldown expires}
cooldowns: Dict[int, datetime] = {}

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

def set_cooldown(user_id: int, cooldown_seconds: int):
    """Set cooldown for a user after command use.
    
    Args:
        user_id (int): Discord user ID to set cooldown for
        cooldown_seconds (int): Number of seconds for the cooldown
    """
    cooldowns[user_id] = datetime.now() + timedelta(seconds=cooldown_seconds) 