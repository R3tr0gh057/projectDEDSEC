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

@client.command(name='mumei', help='Returns an embed with a random mumei gif.')
async def mumei(ctx):
    mumeigifs = ["https://c.tenor.com/cfW8VbIKhawAAAAd/nanashi-mumei-new-outfit.gif",
	"https://c.tenor.com/IQ1PeZCHCxkAAAAC/nanashi-mumei-mumei.gif",
	"https://c.tenor.com/gnuWgEUMIYsAAAAC/mumei-nanashi-mumei.gif",
	"https://c.tenor.com/UInV6S43QuIAAAAC/rgb-ghost.gif",
	"https://c.tenor.com/DlEQy_mx-uEAAAAd/eat-bun.gif",
	"https://c.tenor.com/smmsu2CX0yYAAAAC/loading-mumei.gif",
	"https://c.tenor.com/660xvspq7swAAAAC/nanashi-mumei-nanashi.gif",
	"https://c.tenor.com/oLs2f6DudWwAAAAd/mumei-nanashi-mumei.gif",
	"https://c.tenor.com/h_4Wg0DA6K8AAAAd/nanashi-mumei-ghost.gif",
	"https://c.tenor.com/uXrBBIfVGsgAAAAd/nanashi-mumei-mumei.gif",
	"https://c.tenor.com/U_aHpiPW-SAAAAAC/mumei-kronii.gif",
	"https://c.tenor.com/4zED3Wj9TUoAAAAd/mumei-stare-head-turn.gif",
	"https://c.tenor.com/rZ1QePZ8NvAAAAAd/mumei-hololive.gif",
	"https://c.tenor.com/skq_WPw4e88AAAAd/nanashi-mumei.gif",
	"https://c.tenor.com/KPlqoiI8SIgAAAAd/anime-hololive.gif",
	"https://c.tenor.com/tY18hJ6pfHAAAAAd/holo-council-nanashi-mumei.gif",
	"https://c.tenor.com/1JplCwKBH1cAAAAC/nanashi-mumei-ghost.gif",
	"https://c.tenor.com/fIGnX2zFETYAAAAd/nanashi-mumei-mumei.gif"]
    embed=discord.Embed(title="Mumei says hi :>", description="᲼᲼", color=0xdf7411)
    embed.set_image(url=random.choice(mumeigifs))
    embed.set_footer(text='Requested by {}'.format(ctx.message.author.name))
    await ctx.channel.send(embed=embed)

@client.command(name='kronii', help='Returns an embed with a random kronii gif.')
async def mumei(ctx):
    kroniigifs = ["https://c.tenor.com/VeQvnPxQHZkAAAAd/ouro-kronii-kimono.gif",
    "https://c.tenor.com/Fh58fxSBt08AAAAd/ouro-kronii-wink.gif",
    "https://c.tenor.com/27AoNcj4F70AAAAd/ouro-kronii-gangimari.gif",
    "https://c.tenor.com/95W2eTktpDEAAAAd/ouro-kronii-cursed.gif",
    "https://c.tenor.com/D6fZnhirfWAAAAAC/ouro-kronii-hololive.gif",
    "https://c.tenor.com/MYFSAXUCXt4AAAAd/kronii-loading.gif",
    "https://c.tenor.com/bwULHAJARx0AAAAd/kronii-blank-stare-nodding.gif",
    "https://c.tenor.com/a9Vn6IArztUAAAAC/kronii-hololive.gif",
    "https://c.tenor.com/1jX0q0YxnV4AAAAC/ouro-kronii-kronii.gif",
    "https://c.tenor.com/3kx2gyt2aqQAAAAC/hololive-ouro-kronii.gif",
    "https://c.tenor.com/ToYOxtjHFp0AAAAC/ouro-kronii.gif",
    "https://c.tenor.com/wE24uejNv4oAAAAC/ouro-kronii.gif",
    "https://c.tenor.com/9ol5OfJW8kIAAAAC/kronii-ha.gif",
    "https://c.tenor.com/WN6ggs7vI_gAAAAC/ouro-kronii-double-blink.gif",
    "https://c.tenor.com/S7z4cOS62IUAAAAd/kronii-ouro-kronii.gif",
    "https://c.tenor.com/zyaOLVRqnHkAAAAC/ouro-kronii-derpy.gif",
    "https://c.tenor.com/Iwj_HGRj-cUAAAAC/ouro_kronii-holo_council.gif",
    "https://c.tenor.com/-J92DVIlnzQAAAAd/ouro-kronii-kronii.gif",
    "https://c.tenor.com/yLM2eAOoWu4AAAAC/kronii-vtuber.gif",
    "https://c.tenor.com/inv2qpuIcmYAAAAC/ouro-kronii-hololive.gif",
    "https://c.tenor.com/RlCpu55u2S8AAAAd/kronii-ouro-ouro-kronii.gif",
    "https://c.tenor.com/5R4UPPjGTMIAAAAd/ouro-kronii-trailer.gif",
    "https://c.tenor.com/rS4E5CgvOJgAAAAd/ouro-kronii-ouro.gif",
    "https://c.tenor.com/kopcbK29f5IAAAAd/hololive-en-kronii-ouro.gif",
    "https://c.tenor.com/tH9cNwaQkWMAAAAd/ouro-kronii-hololive.gif",
    "https://c.tenor.com/aXNX2mUBkLcAAAAd/ouro-kronii-kronii.gif",
    "https://c.tenor.com/yZ_zvPP3kUcAAAAd/kronii-ribbon-smooth.gif",
    "https://c.tenor.com/uH50L7c0Cu8AAAAC/ouro-kronii-hololive.gif",
    "https://c.tenor.com/JN-DNJ2aGs8AAAAd/ouro-kronii-kronii.gif",
    "https://c.tenor.com/AArvHsN63e0AAAAd/ouro-kronii-boros.gif",
    "https://c.tenor.com/e5y6XJQ_iVoAAAAd/tower-of-babel-gaming-show-me-your-nuts.gif"]
    embed=discord.Embed(title="Kronii says hi :>", description="᲼᲼", color=0xdf7411)
    embed.set_image(url=random.choice(kroniigifs))
    embed.set_footer(text='Requested by {}'.format(ctx.message.author.name))
    await ctx.channel.send(embed=embed)

@client.command(name='dedsec', help='Slayer mode.')
async def dedsec(ctx):
    x=0

client.run(TOKEN)