import discord
from discord.ext import commands

client = commands.Bot(command_prefix="^", intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Ready to le meat')
    print('----------------')

@client.command()
async def meat(ctx):
    await ctx.send('I am your lord and saviour')

client.run('MTIxMzA2NjkwMDYzMjc3MjYyOA.GryVXE.ZP1rAunSFY71MBVNUbI-n-9yrvgnfmpHEMk9GM')

