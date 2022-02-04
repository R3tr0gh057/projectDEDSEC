import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
from datetime import datetime
from discord.ext.commands import has_permissions, MissingPermissions
import time
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game(".help"))
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

#mention's if someone deletes a message (4k)
@client.event
async def on_message_delete(ctx):
        msg = f'{ctx.author} has deleted the message: {ctx.content}'
        await ctx.channel.send(msg)

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
    await ctx.channel.send(member.display_name+" has been banned from "+guild.name)
    await member.ban(reason=reason)
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
    await ctx.channel.send(member.display_name+" has been kicked from "+guild.name)
    await member.kick(reason=reason)
    try:
        await member.send("You have been kicked from "+guild.name+" for "+reason)
    except:
        print(member.display_name+" is not accepting dms")

@client.command(name='unban', help='unban a banned member')
@commands.has_permissions(ban_members = True)
async def unban(ctx,*,member):
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    banned_users= await ctx.guild.bans()
    member_name, member_disc =member.split('#')
    for banned_entry in banned_users:
        user=banned_entry.user
        if (user.name, user.discriminator)==(member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.channel.send(member_name+" has been unbanned")
            return
    await ctx.send(member+" is not in the ban list")
    
    try:
        await member.send("You have been unbanned in "+guild.name)
    except:
        print(member.display_name+" is not accepting dms")

@client.command(name='mute', help='mute a member')
@commands.has_permissions(kick_members = True)
async def mute(ctx, member : discord.Member):
    muted_role= ctx.guild.get_role(937655146182246401)
    await member.add_roles(muted_role)
    await ctx.channel.send(member.mention+' has been muted')

@client.command(name='unmute', help='unmute a member')
@commands.has_permissions(kick_members = True)
async def unmute(ctx, member : discord.Member):
    muted_role= ctx.guild.get_role(937655146182246401)
    await member.remove_roles(muted_role)
    await ctx.channel.send(member.mention+', your mute has been lifted')

#exception handling start

@ban.error
async def ban_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send("You dont have the perms to ban members")

@kick.error
async def kick_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send("You dont have the perms to kick members")

@unban.error
async def unban_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send("You dont have the perms to unban members")

@mute.error
async def mute_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send("You dont have the perms to mute members")

@unmute.error
async def unban_error(error, ctx):
    if isinstance(error, MissingPermissions):
        await ctx.channel.send("You dont have the perms to unmute members")

#exception handling end

client.run(TOKEN)