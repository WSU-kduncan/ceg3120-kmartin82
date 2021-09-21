import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    expanse_quotes = ['Its better to go down swinging than rolling over.',
		      'As long as were living and breathing, theres more we can do. we just have to to be strong enough',
		      'A child who wont grow up turns into a fool',
		      'Earthers have a home its time Belters had one, too.',
		      'A kid needs atleast one person who never gives up on them, no matter what.',
		      'Cold war is a bloodless war. Mutual distrust and complete co-dependence.']

    if message.content == 'towel!':
        response = random.choice(expanse_quotes)
        await message.channel.send(response)

client.run(TOKEN)
