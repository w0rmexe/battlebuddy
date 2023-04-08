import discord
import random

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')

@client.event
async def on_message(message):
    if message.content.startswith('BB'):
        # Extract the game name from the message
        game = message.content[3:].strip().lower()

        # Create a dictionary of characters for each game
        characters = {
            'apex': sorted(['Bangalore', 'Bloodhound', 'Caustic', 'Crypto', 'Fuse',
                            'Gibraltar', 'Horizon', 'Lifeline', 'Mirage', 'Octane',
                            'Pathfinder', 'Rampart', 'Revenant', 'Valkyrie', 'Wraith']),
            'overwatch': sorted(['Ashe', 'Baptiste', 'Brigitte', 'D.Va', 'Echo',
                                 'Genji', 'Hanzo', 'Junkrat', 'Lúcio', 'McCree',
                                 'Mei', 'Mercy', 'Moira', 'Orisa', 'Pharah',
                                 'Reaper', 'Roadhog', 'Sigma', 'Soldier: 76',
                                 'Symmetra', 'Torbjörn', 'Tracer', 'Widowmaker',
                                 'Winston', 'Zarya', 'Zenyatta']),
            'valorant': sorted(['Astra', 'Breach', 'Brimstone', 'Cypher', 'Jett',
                                'Kay/o', 'Killjoy', 'Omen', 'Phoenix', 'Reyna',
                                'Sage', 'Skye', 'Sova', 'Viper', 'Yoru'])
        }

        # Pick a random character from the corresponding game
        if game in characters:
            chosen_character = random.choice(characters[game])
            await message.channel.send(f'Your random character for {game} is {chosen_character}!')
        else:
            await message.channel.send('Sorry, I do not recognize that game.')

client.run('MTA5NDI4NzU0MzE1Mjk0MzI5NA.Ge77GH.3cBJE0iJTuUtPNSkRxyOU4f5kjkUpnbmp72V2A')