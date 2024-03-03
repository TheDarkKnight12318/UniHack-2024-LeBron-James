import discord
import spotipy
from discord import app_commands
#import lyricgenius
from discord.ext import commands
from lyric import lyric_getter

client = commands.Bot(command_prefix="^", intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity('Basketball'))
    print('Ready to le meat')
    print('----------------')

@client.command()
async def meat(ctx):
    await ctx.send('I am your lord and saviour')

@client.command()
async def daddy(ctx):
    await ctx.send("Don't worry. I got you pookie. :heart:")
    
#DM Command
@client.command()
async def dm(ctx, user: discord.Member, *, message=None):
    message = message or "You lookin sexy"
    await user.send(message)
#Dunk Command
@client.command()
async def dunk(ctx):
    await ctx.message.author.send('SLAM DUNK \n https://tenor.com/view/lakers-gif-26550379')

#Dunk Command
@client.command()
async def threepointer(ctx):
    await ctx.message.author.send('FROM THE THREE POINT LINE! \n https://tenor.com/XkC2.gif')

#Toggles realtime lyrics on
@client.command()
async def toggle_on(ctx):
    lyric_printer = True
    await ctx.send('Lyrics have been turned on')

#Toggles realtime lyrics off
@client.command()
async def toggle_off(ctx):
    lyric_printer = False
    await ctx.send('Lyrics have been turned off')

#Fetch lyrics

@client.command()
async def songlyrics(ctx, artist, song):
    #Convert arguement with underscore to space
    artist = artist.replace('_', ' ')
    song = song.replace('_', ' ')
    full_lyric = lyric_getter.get_lyrics(artist, song)
    await ctx.message.author.send(full_lyric[0:2000])
    await ctx.message.author.send(full_lyric[2000:4000])
    await ctx.message.author.send(full_lyric[4000:6000])
    await ctx.message.author.send(full_lyric[6000:8000])

    #for char in full_lyric:
        #if char == '\n':
        #    current_line = [0, full_lyric.index(char)]
        #    await ctx.send(current_line)
        #    current_line.pop(0, full_lyric.index(char))



#--------

client.run('')
