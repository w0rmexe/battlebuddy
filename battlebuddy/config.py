"""
Configuration file for BattleBuddy Discord bot.
Contains game characters and other configuration settings.

This module defines:
1. Character lists for each supported game
2. Role types and role mappings for characters
3. Bot configuration settings
4. Command cooldown settings
"""

# Bot configuration settings
COMMAND_PREFIX = '!'  # Prefix for legacy text commands
BOT_DESCRIPTION = 'A bot that helps you select random characters from various games'
COMMAND_COOLDOWN = 5  # Cooldown period in seconds between command uses

# Dictionary of characters for each supported game with their roles and descriptions
# Each game entry contains:
# - characters: List of available characters
# - roles: Available role types
# - role_mapping: Dictionary mapping characters to their roles
CHARACTERS = {
    'apex': {
        'characters': [
            'Alter', 'Ash', 'Ballistic', 'Bangalore', 'Bloodhound', 'Catalyst', 'Caustic', 'Conduit',
            'Crypto', 'Fuse', 'Gibraltar', 'Horizon', 'Lifeline', 'Loba', 'Mad Maggie', 'Mirage',
            'Newcastle', 'Octane', 'Pathfinder', 'Rampart', 'Revenant', 'Seer', 'Valkyrie',
            'Vantage', 'Wattson', 'Wraith'
        ],
        'roles': ['Assault', 'Skirmisher', 'Recon', 'Support', 'Controller'],
        'role_mapping': {
            'Ash': 'Assault',
            'Ballistic': 'Assault',
            'Bangalore': 'Assault',
            'Bloodhound': 'Recon',
            'Catalyst': 'Controller',
            'Caustic': 'Controller',
            'Conduit': 'Support',
            'Crypto': 'Recon',
            'Fuse': 'Assault',
            'Gibraltar': 'Support',
            'Horizon': 'Skirmisher',
            'Lifeline': 'Support',
            'Loba': 'Support',
            'Mad Maggie': 'Assault',
            'Mirage': 'Support',
            'Newcastle': 'Support',
            'Octane': 'Skirmisher',
            'Pathfinder': 'Skirmisher',
            'Rampart': 'Controller',
            'Revenant': 'Skirmisher',
            'Seer': 'Recon',
            'Valkyrie': 'Skirmisher',
            'Vantage': 'Recon',
            'Wattson': 'Controller',
            'Wraith': 'Skirmisher',
            'Alter': 'Skirmisher'
        }
    },
    'overwatch': {
        'characters': [
            'Ana', 'Ashe', 'Baptiste', 'Bastion', 'Brigitte', 'Cassidy', 'D.Va', 'Doomfist', 'Echo',
            'Genji', 'Hanzo', 'Hazard', 'Illari', 'Junker Queen', 'Junkrat', 'Kiriko', 'Lúcio', 'Mei',
            'Mercy', 'Moira', 'Orisa', 'Pharah', 'Ramattra', 'Reaper', 'Reinhardt', 'Roadhog', 'Sigma',
            'Soldier: 76', 'Sojourn', 'Sombra', 'Symmetra', 'Torbjörn', 'Tracer', 'Widowmaker', 'Winston',
            'Wrecking Ball', 'Zarya', 'Zenyatta'
        ],
        'roles': ['Tank', 'Damage', 'Support'],
        'role_mapping': {
            'Ana': 'Support',
            'Ashe': 'Damage',
            'Baptiste': 'Support',
            'Bastion': 'Damage',
            'Brigitte': 'Support',
            'Cassidy': 'Damage',
            'D.Va': 'Tank',
            'Doomfist': 'Tank',
            'Echo': 'Damage',
            'Genji': 'Damage',
            'Hanzo': 'Damage',
            'Hazard': 'Damage',
            'Illari': 'Support',
            'Junker Queen': 'Tank',
            'Junkrat': 'Damage',
            'Kiriko': 'Support',
            'Lúcio': 'Support',
            'Mei': 'Damage',
            'Mercy': 'Support',
            'Moira': 'Support',
            'Orisa': 'Tank',
            'Pharah': 'Damage',
            'Ramattra': 'Tank',
            'Reaper': 'Damage',
            'Reinhardt': 'Tank',
            'Roadhog': 'Tank',
            'Sigma': 'Tank',
            'Soldier: 76': 'Damage',
            'Sojourn': 'Damage',
            'Sombra': 'Damage',
            'Symmetra': 'Damage',
            'Torbjörn': 'Damage',
            'Tracer': 'Damage',
            'Widowmaker': 'Damage',
            'Winston': 'Tank',
            'Wrecking Ball': 'Tank',
            'Zarya': 'Tank',
            'Zenyatta': 'Support'
        }
    },
    'valorant': {
        'characters': [
            'Astra', 'Breach', 'Brimstone', 'Chamber', 'Clove', 'Cypher', 'Deadlock', 'Fade', 'Gekko',
            'Harbor', 'Iso', 'Jett', 'Kay/o', 'Killjoy', 'Neon', 'Omen', 'Phoenix', 'Raze', 'Reyna',
            'Sage', 'Skye', 'Sova', 'Tejo', 'Viper', 'Vyse', 'Waylay', 'Yoru'
        ],
        'roles': ['Controller', 'Duelist', 'Initiator', 'Sentinel'],
        'role_mapping': {
            'Astra': 'Controller',
            'Breach': 'Initiator',
            'Brimstone': 'Controller',
            'Chamber': 'Sentinel',
            'Clove': 'Controller',
            'Cypher': 'Sentinel',
            'Deadlock': 'Sentinel',
            'Fade': 'Initiator',
            'Gekko': 'Initiator',
            'Harbor': 'Controller',
            'Iso': 'Duelist',
            'Jett': 'Duelist',
            'Kay/o': 'Initiator',
            'Killjoy': 'Sentinel',
            'Neon': 'Duelist',
            'Omen': 'Controller',
            'Phoenix': 'Duelist',
            'Raze': 'Duelist',
            'Reyna': 'Duelist',
            'Sage': 'Sentinel',
            'Skye': 'Initiator',
            'Sova': 'Initiator',
            'Tejo': 'Initiator',
            'Viper': 'Controller',
            'Vyse': 'Sentinel',
            'Waylay': 'Duelist',
            'Yoru': 'Duelist'
        }
    },
    'lol': {
        'characters': [
            'Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alistar', 'Amumu', 'Anivia', 'Annie', 'Aphelios',
            'Ashe', 'Aurelion Sol', 'Azir', 'Bard', 'Bel\'Veth', 'Blitzcrank', 'Brand', 'Braum',
            'Caitlyn', 'Camille', 'Cassiopeia', 'Cho\'Gath', 'Corki', 'Darius', 'Diana', 'Draven',
            'Dr. Mundo', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora', 'Fizz',
            'Galio', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger',
            'Illaoi', 'Irelia', 'Ivern', 'Janna', 'Jarvan IV', 'Jax', 'Jayce', 'Jhin', 'Jinx',
            'K\'Sante', 'Kai\'Sa', 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle',
            'Kayn', 'Kennen', 'Kha\'Zix', 'Kindred', 'Kled', 'Kog\'Maw', 'LeBlanc', 'Lee Sin',
            'Leona', 'Lillia', 'Lissandra', 'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar',
            'Maokai', 'Master Yi', 'Milio', 'Miss Fortune', 'Mordekaiser', 'Morgana', 'Naafiri',
            'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Nidalee', 'Nilah', 'Nocturne', 'Nunu & Willump',
            'Olaf', 'Orianna', 'Ornn', 'Pantheon', 'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan',
            'Rammus', 'Rek\'Sai', 'Rell', 'Renata Glasc', 'Renekton', 'Rengar', 'Riven', 'Rumble',
            'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana',
            'Singed', 'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra',
            'Tahm Kench', 'Taliyah', 'Talon', 'Taric', 'Teemo', 'Thresh', 'Tristana', 'Trundle',
            'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne', 'Veigar',
            'Vel\'Koz', 'Vex', 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong',
            'Xayah', 'Xerath', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Yuumi', 'Zac', 'Zed', 'Zeri',
            'Ziggs', 'Zilean', 'Zoe', 'Zyra', 'Briar', 'Hwei', 'Smolder'
        ],
        'roles': ['Assassin', 'Fighter', 'Mage', 'Marksman', 'Support', 'Tank'],
        'role_mapping': {
            # Assassins
            'Akali': 'Assassin', 'Evelynn': 'Assassin', 'Fizz': 'Assassin', 'Kassadin': 'Assassin',
            'Katarina': 'Assassin', 'Kha\'Zix': 'Assassin', 'LeBlanc': 'Assassin', 'Nocturne': 'Assassin',
            'Pyke': 'Assassin', 'Qiyana': 'Assassin', 'Rengar': 'Assassin', 'Shaco': 'Assassin',
            'Talon': 'Assassin', 'Zed': 'Assassin', 'Naafiri': 'Assassin',
            
            # Fighters
            'Aatrox': 'Fighter', 'Camille': 'Fighter', 'Darius': 'Fighter', 'Fiora': 'Fighter',
            'Garen': 'Fighter', 'Gnar': 'Fighter', 'Gwen': 'Fighter', 'Irelia': 'Fighter',
            'Jax': 'Fighter', 'Jayce': 'Fighter', 'K\'Sante': 'Fighter', 'Kayn': 'Fighter',
            'Kled': 'Fighter', 'Lillia': 'Fighter', 'Lucian': 'Fighter', 'Mordekaiser': 'Fighter',
            'Nasus': 'Fighter', 'Olaf': 'Fighter', 'Pantheon': 'Fighter', 'Poppy': 'Fighter',
            'Renekton': 'Fighter', 'Riven': 'Fighter', 'Sett': 'Fighter', 'Sylas': 'Fighter',
            'Trundle': 'Fighter', 'Tryndamere': 'Fighter', 'Udyr': 'Fighter', 'Urgot': 'Fighter',
            'Vi': 'Fighter', 'Volibear': 'Fighter', 'Warwick': 'Fighter', 'Wukong': 'Fighter',
            'Xin Zhao': 'Fighter', 'Yasuo': 'Fighter', 'Yone': 'Fighter', 'Yorick': 'Fighter',
            'Briar': 'Fighter',
            
            # Mages
            'Ahri': 'Mage', 'Anivia': 'Mage', 'Annie': 'Mage', 'Aurelion Sol': 'Mage',
            'Azir': 'Mage', 'Brand': 'Mage', 'Cassiopeia': 'Mage', 'Corki': 'Mage',
            'Diana': 'Mage', 'Ekko': 'Mage', 'Elise': 'Mage', 'Fiddlesticks': 'Mage',
            'Galio': 'Mage', 'Gragas': 'Mage', 'Heimerdinger': 'Mage', 'Karma': 'Mage',
            'Karthus': 'Mage', 'Kennen': 'Mage', 'Leona': 'Mage', 'Lissandra': 'Mage',
            'Lux': 'Mage', 'Malzahar': 'Mage', 'Morgana': 'Mage', 'Neeko': 'Mage',
            'Nidalee': 'Mage', 'Orianna': 'Mage', 'Rumble': 'Mage', 'Ryze': 'Mage',
            'Seraphine': 'Mage', 'Swain': 'Mage', 'Syndra': 'Mage', 'Taliyah': 'Mage',
            'Twisted Fate': 'Mage', 'Veigar': 'Mage', 'Vel\'Koz': 'Mage', 'Vex': 'Mage',
            'Viktor': 'Mage', 'Vladimir': 'Mage', 'Xerath': 'Mage', 'Ziggs': 'Mage',
            'Zilean': 'Mage', 'Zoe': 'Mage', 'Zyra': 'Mage', 'Hwei': 'Mage',
            
            # Marksmen
            'Akshan': 'Marksman', 'Aphelios': 'Marksman', 'Ashe': 'Marksman', 'Caitlyn': 'Marksman',
            'Draven': 'Marksman', 'Ezreal': 'Marksman', 'Jhin': 'Marksman', 'Jinx': 'Marksman',
            'Kai\'Sa': 'Marksman', 'Kalista': 'Marksman', 'Kindred': 'Marksman', 'Kog\'Maw': 'Marksman',
            'Lucian': 'Marksman', 'Miss Fortune': 'Marksman', 'Nilah': 'Marksman', 'Quinn': 'Marksman',
            'Samira': 'Marksman', 'Sivir': 'Marksman', 'Tristana': 'Marksman', 'Twitch': 'Marksman',
            'Varus': 'Marksman', 'Vayne': 'Marksman', 'Xayah': 'Marksman', 'Zeri': 'Marksman',
            'Smolder': 'Marksman',
            
            # Supports
            'Alistar': 'Support', 'Bard': 'Support', 'Blitzcrank': 'Support', 'Braum': 'Support',
            'Janna': 'Support', 'Karma': 'Support', 'Leona': 'Support', 'Lulu': 'Support',
            'Milio': 'Support', 'Nami': 'Support', 'Rakan': 'Support', 'Renata Glasc': 'Support',
            'Senna': 'Support', 'Seraphine': 'Support', 'Sona': 'Support', 'Soraka': 'Support',
            'Taric': 'Support', 'Thresh': 'Support', 'Yuumi': 'Support', 'Zilean': 'Support',
            
            # Tanks
            'Amumu': 'Tank', 'Cho\'Gath': 'Tank', 'Dr. Mundo': 'Tank', 'Galio': 'Tank',
            'Gragas': 'Tank', 'Hecarim': 'Tank', 'Illaoi': 'Tank', 'Jarvan IV': 'Tank',
            'Malphite': 'Tank', 'Maokai': 'Tank', 'Nautilus': 'Tank', 'Nunu & Willump': 'Tank',
            'Ornn': 'Tank', 'Poppy': 'Tank', 'Rammus': 'Tank', 'Rell': 'Tank', 'Sejuani': 'Tank',
            'Shen': 'Tank', 'Sion': 'Tank', 'Skarner': 'Tank', 'Tahm Kench': 'Tank',
            'Thresh': 'Tank', 'Volibear': 'Tank', 'Zac': 'Tank'
        }
    },
    'rivals': {
        'characters': [
            # Vanguards
            'Captain America', 'Doctor Strange', 'Groot', 'Hulk', 'Magneto', 'Peni Parker',
            'The Thing', 'Thor', 'Venom',
            # Duelists
            'Black Panther', 'Black Widow', 'Hawkeye', 'Hela', 'Human Torch', 'Iron Fist',
            'Iron Man', 'Magik', 'Mister Fantastic', 'Moon Knight', 'Namor', 'Psylocke',
            'Scarlet Witch', 'Spider-Man', 'Squirrel Girl', 'Star-Lord', 'Storm',
            'The Punisher', 'Winter Soldier', 'Wolverine',
            # Strategists
            'Adam Warlock', 'Cloak & Dagger', 'Invisible Woman', 'Jeff the Land Shark',
            'Loki', 'Luna Snow', 'Mantis', 'Rocket Raccoon'
        ],
        'roles': ['Vanguard', 'Duelist', 'Strategist'],
        'role_mapping': {
            # Vanguards
            'Captain America': 'Vanguard',
            'Doctor Strange': 'Vanguard',
            'Groot': 'Vanguard',
            'Hulk': 'Vanguard',
            'Magneto': 'Vanguard',
            'Peni Parker': 'Vanguard',
            'The Thing': 'Vanguard',
            'Thor': 'Vanguard',
            'Venom': 'Vanguard',
            # Duelists
            'Black Panther': 'Duelist',
            'Black Widow': 'Duelist',
            'Hawkeye': 'Duelist',
            'Hela': 'Duelist',
            'Human Torch': 'Duelist',
            'Iron Fist': 'Duelist',
            'Iron Man': 'Duelist',
            'Magik': 'Duelist',
            'Mister Fantastic': 'Duelist',
            'Moon Knight': 'Duelist',
            'Namor': 'Duelist',
            'Psylocke': 'Duelist',
            'Scarlet Witch': 'Duelist',
            'Spider-Man': 'Duelist',
            'Squirrel Girl': 'Duelist',
            'Star-Lord': 'Duelist',
            'Storm': 'Duelist',
            'The Punisher': 'Duelist',
            'Winter Soldier': 'Duelist',
            'Wolverine': 'Duelist',
            # Strategists
            'Adam Warlock': 'Strategist',
            'Cloak & Dagger': 'Strategist',
            'Invisible Woman': 'Strategist',
            'Jeff the Land Shark': 'Strategist',
            'Loki': 'Strategist',
            'Luna Snow': 'Strategist',
            'Mantis': 'Strategist',
            'Rocket Raccoon': 'Strategist'
        }
    }
}

# Character descriptions and additional information
CHARACTER_INFO = {
    'apex': {
        'Alter': {
            'description': 'A mysterious character with unique abilities',
            'difficulty': 'Medium',
            'release_date': '2024'
        },
        'Ash': {
            'description': 'A former Apex Predator turned mercenary',
            'difficulty': 'Medium',
            'release_date': '2021'
        },
        # ... Add descriptions for other Apex characters
    },
    'overwatch': {
        'Ana': {
            'description': 'A skilled sniper and healer',
            'difficulty': 'Hard',
            'release_date': '2016'
        },
        'Ashe': {
            'description': 'A sharpshooter with a powerful rifle',
            'difficulty': 'Medium',
            'release_date': '2018'
        },
        # ... Add descriptions for other Overwatch characters
    }
}

# Game-specific settings and configurations
GAME_SETTINGS = {
    'apex': {
        'max_team_size': 3,
        'game_modes': ['Battle Royale', 'Arena', 'Control'],
        'update_frequency': 'Seasonal'
    },
    'overwatch': {
        'max_team_size': 5,
        'game_modes': ['Quick Play', 'Competitive', 'Arcade'],
        'update_frequency': 'Monthly'
    }
}

# Error messages and responses
ERROR_MESSAGES = {
    'invalid_game': 'Invalid game selected. Please choose from the available games.',
    'invalid_role': 'Invalid role selected. Please choose from the available roles.',
    'cooldown': 'Please wait before using this command again.',
    'database_error': 'An error occurred while accessing the database.',
    'no_favorites': 'You haven\'t added any favorites yet.',
    'character_not_found': 'Character not found in the specified game.'
}

# Success messages and responses
SUCCESS_MESSAGES = {
    'favorite_added': 'Character added to your favorites!',
    'favorite_removed': 'Character removed from your favorites.',
    'stats_updated': 'Character statistics updated successfully.',
    'command_success': 'Command executed successfully.'
} 