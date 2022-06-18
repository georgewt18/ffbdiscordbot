# bot.py
import os
import json
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv
from sleeper_wrapper import League, User, Stats, Players

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

with open('players.json') as f:
    try:
        all_players = json.load(f)
    except Exception as e:
        print(e)
        print('Please run getplayers.py first')
        exit()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot Ready')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Football"))

for f in os.listdir("./cogs"):
	if f.endswith(".py"):
		bot.load_extension("cogs." + f[:-3])

bot.run(TOKEN)
