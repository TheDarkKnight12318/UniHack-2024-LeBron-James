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
async def songlyrics(ctx, user: discord.Member = None):
    #Convert arguement with underscore to space 
    if user is None:
        user = client.user
        await ctx.send("Please type user name")

    if user.activity is not None and isinstance(user.activity, discord.Spotify):
        spotify_activity = user.activity
        song = spotify_activity.title
        artist = spotify_activity.artist
    else:
        await ctx.send(f"{user.display_name} is not currently listening to Spotify.")
        await ctx.send(f"They are doing {user.activity}")

    a = 0
    b = 2000
    full_lyric = lyric_getter.get_lyrics(artist, song)
    lyric_len = len(full_lyric)
    cycle_times = lyric_len // 2000 + 1

    for n in range(cycle_times):
        await ctx.send(full_lyric[a:b])
        a = b
        b += 2000


@client.command()
async def spotify(ctx, user: discord.Member = None):
    # If no user is mentioned, use the bot's own status
    if user is None:
        user = client.user
        await ctx.send("Please type user name")

    # Fetch the status of the specified user
    if user.activity is not None and isinstance(user.activity, discord.Spotify):
        spotify_activity = user.activity
        await ctx.send(f"{user.display_name} is listening to Spotify:")
        await ctx.send(f"Song: {spotify_activity.title}\nArtist(s): {', '.join(spotify_activity.artists)}")
    else:
        await ctx.send(f"{user.display_name} is not currently listening to Spotify.")
        await ctx.send(f"They are doing {user.activity}")

#--------

client.run('token')
