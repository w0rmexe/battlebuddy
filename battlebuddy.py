import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # enable the members intent
intents.presences = True  # enable the presence intent

bot = commands.Bot(command_prefix='BB ', intents=intents)
TOKEN = 'MTA5NDI4NzU0MzE1Mjk0MzI5NA.Ge77GH.3cBJE0iJTuUtPNSkRxyOU4f5kjkUpnbmp72V2A'


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.slash_command(name='who-should-i-play', description='Get a random character suggestion for a specific game')
async def on_interaction(ctx: discord.Interaction):
    game = ctx.options['game'].lower()

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

    if game in characters:
        chosen_character = random.choice(characters[game])
        await ctx.respond(f'You should play {chosen_character} in {game}!')
    else:
        await ctx.respond(f'Sorry, I do not recognize {game}.')

bot.run(TOKEN)

