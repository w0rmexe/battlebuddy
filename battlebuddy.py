import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command(name='who')
async def who(ctx, game: str):
    # Create a dictionary of characters for each game
    characters = {
        'apex': sorted(['Ash', 'Bangalore', 'Bloodhound', 'Catalyst', 'Caustic', 'Crypto', 'Fuse',
                        'Gibraltar', 'Horizon', 'Lifeline', 'Loba', 'Mad Maggie', 'Mirage', 'Newcastle', 'Octane',
                        'Pathfinder', 'Rampart', 'Revenant', 'Seer', 'Valkyrie', 'Vantage', 'Wattson', 'Wraith']),
        'overwatch': sorted(['Ana', 'Ashe', 'Baptiste', 'Bastion', 'Brigitte', 'Cassidy', 'D.Va', 'Doomfist', 'Echo',
                             'Genji', 'Hanzo', 'Junker Queen', 'Junkrat', 'Kiriko', 'Lúcio',
                             'Mei', 'Mercy', 'Moira', 'Orisa', 'Pharah', 'Ramattra',
                             'Reaper', 'Reinhardt', 'Roadhog', 'Sigma', 'Soldier: 76', 'Sojourn',
                             'Sombra', 'Symmetra', 'Torbjörn', 'Tracer', 'Widowmaker',
                             'Winston', 'Wrecking Ball', 'Zarya', 'Zenyatta']),
        'valorant': sorted(['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 'Fade',
                            'Gekko', 'Harbor', 'Jett', 'Kay/o', 'Killjoy', 'Neon', 'Omen', 'Phoenix', 'Raze',
                            'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru'])
    }

    # Pick a random character from the corresponding game
    if game.lower() in characters:
        chosen_character = random.choice(characters[game.lower()])
        await ctx.send(f'Your random character for {game} is {chosen_character}!')
    else:
        await ctx.send('Sorry, I do not recognize that game.')

bot.run('MTA5NDI4NzU0MzE1Mjk0MzI5NA.Gj5g_-.PcxvZc-ElGGbJjTq3mTyu5DAKaE7u8yJkrlykE')
