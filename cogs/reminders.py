import discord
from discord.ext import commands

class Reminders(commands.Cog):
    """A set of tasks to have the bot remind you of certain things"""

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
	bot.add_cog(Reminders(bot))
        