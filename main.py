import nextcord
from nextcord.ext import commands
import os

from server import server_on

message_to_edit = None
intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Game(name="เป็นบอทรับยศ"))
    print(f"{bot.user}")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

server_on()
bot.run(os.getenv('TOKEN'))
