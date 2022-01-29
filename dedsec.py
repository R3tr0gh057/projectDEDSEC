import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
from datetime import datetime
import time
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    #members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')
    print(", ".join([member.name for member in guild.members]))

@client.command(name='ping', help='Returns the client latency.')
async def ping(ctx):
    await ctx.channel.send(f'Client latency: {round(client.latency*1000)}ms')

@client.command(name='clear', help='Clears (x) amount of messages.')
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

client.run(TOKEN)