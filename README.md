# BattleBuddy Discord Bot

A Discord bot that helps you randomly select characters from various games.

## Features

- Random character selection from multiple games
- Role-based character filtering
- Character statistics tracking
- User favorites system
- Rich embedded messages
- Command cooldowns
- Error handling

## Supported Games

### Apex Legends
- Roles: Assault, Skirmisher, Recon, Support, Controller
- 26 characters

### Overwatch
- Roles: Tank, Damage, Support
- 39 characters

### Valorant
- Roles: Controller, Duelist, Initiator, Sentinel
- 27 characters

### League of Legends
- Roles: Assassin, Fighter, Mage, Marksman, Support, Tank
- 165 champions

### Marvel Rivals
- Roles: Vanguard, Duelist, Strategist
- 37 characters

## Commands

- `/who [game] [role]` - Select a random character from a game (optionally filtered by role)
- `/random` - Select a random character from any game
- `/stats [game]` - View character pick statistics
- `/favorite [game] [character]` - Add/remove a character from your favorites
- `/favorites` - View your favorite characters
- `/help` - Display available commands and supported games

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/battlebuddy.git
   cd battlebuddy
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your Discord bot token:
   ```
   DISCORD_TOKEN=your_bot_token_here
   ```

5. Run the bot:
   ```bash
   python battlebuddy.py
   ```

## Development

### Running Tests
   ```bash
   pytest
   ```

### Adding New Games
To add a new game:
1. Add the game to the `CHARACTERS` dictionary in `config.py`
2. Include character list, roles, and role mappings
3. Update the README.md with the new game information

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.
