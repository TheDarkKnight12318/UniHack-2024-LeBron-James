import discord
from discord.ext import commands
import spotipy
import asyncio  
#import lyricgenius
from discord.ext import commands
from lyric import lyric_getter

client = commands.Bot(command_prefix="^", intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity('THE BRONZE AGE'))
    print('Ready to le meat')
    print('----------------')

@client.command()
async def cena(ctx, user: discord.Member, *, message=None):
    await user.send('''# You can't see him\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀\n⠀''')  

@client.command()
async def drake(ctx, user: discord.Member, *, message=None):
    await user.send('# Drake Snake...\n https://cdn.discordapp.com/attachments/1213085984024043580/1213691358284619817/0_Cena.webp?ex=65f66529&is=65e3f029&hm=ecd19681c5e13812415c6d6492ceadc4df12e2f8292da83e6bb7483d30609b42&')

@client.command()
async def meat(ctx):
    await ctx.send('I am your lord and saviour')

@client.command()
async def daddy(ctx):
    await ctx.send("Don't worry. I got you pookie. :heart:") 

@client.command()
async def oilup(ctx, user: discord.Member, *, message=None):
    await user.send('You know what to do...\n https://tenor.com/view/noel-noel-deyzel-oil-noel-oil-oil-up-gif-15231228810340005316')
#DM Command
@client.command()
async def dm(ctx, user: discord.Member, *, message=None):
    message = message or "You lookin sexy"
    await user.send(message)
#Dunk Command
@client.command()
async def dunk(ctx):
    await ctx.message.author.send('SLAM DUNK \n https://tenor.com/view/lakers-gif-26550379')

#Threepointer Command
@client.command()
async def threepointer(ctx):
    await ctx.message.author.send('FROM THE THREE POINT LINE! \n https://tenor.com/XkC2.gif')

#Toggles realtime lyrics on
@client.command()
async def toggle_on(ctx):
    lyric_printer = True
    await ctx.send('Lyrics have been turned on')
    Inactivity = 10
    for i in range(Inactivity, 0, -1):
        await asyncio.sleep(1)
    lyric_printer = False
    await ctx.send('Lyrics have been turned off due to inactivity')
        

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

#spotify

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

client.run('MTIxMzQxMDQ4ODU0MTc3MzkxNg.GyOl_g.U0UctFIAWUk9uYftb_jTAvFAil7fgJtttEpf_I')