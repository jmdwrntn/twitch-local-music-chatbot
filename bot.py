from dotenv import load_dotenv
from twitchio.ext import commands
import os

load_dotenv()

# Set up the bot.
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


# Bot sign on message.
@bot.event
async def event_ready():
    """Called once when the bot goes online"""
    print(f"{os.environ['BOT_NICK']} is online!")


# Bot reads messages and ignores itself.
@bot.event
async def event_message(ctx):
    """Runs every time a message is sent in chat"""
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)


# Bot reads music text output and sends as message.
@bot.command(name='song')
async def song(ctx):
    with open(os.environ['MUSIC_FILE'], 'r', encoding='utf8') as f:
        now_playing = f.readline()

    await ctx.send('Now playing: ' + now_playing)

if __name__ == "__main__":
    bot.run()
