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

async def on_message_delete(self, message):
        msg = f'{message.author} has deleted the message: {message.content}'
        await message.channel.send(msg)

@client.command(name='ping', help='Returns the client latency.')
async def ping(ctx):
    await ctx.channel.send(f'Client latency: {round(client.latency*1000)}ms')

@client.command(name='clear', help='Clears (x) amount of messages.')
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@client.command(name='ban', help='Ban someone for breaking a rule/other reasons')
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member,*,reason="No reason provided"):
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    try:
        await ctx.channel.send(member.display_name+" has been kicked from "+guild.name)
        await member.kick(reason=reason)
    except:
        ctx.channel.send('You dont have the perms to do that')
    try:
        await member.send("You have been banned from "+guild.name+" for "+reason)
    except:
        print(member.name+" is not accepting dms")

@client.command(name='kick', help='kick someone for breaking a rule/other reasons')
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member,*,reason="No reason provided"):
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    try:
        await ctx.channel.send(member.display_name+" has been kicked from "+guild.name)
        await member.kick(reason=reason)
    except:
        ctx.channel.send('You dont have the perms to do that')
    try:
        await member.send("You have been kicked from "+guild.name+" for "+reason)
    except:
        print(member.display_name+" is not accepting dms")

client.run(TOKEN)