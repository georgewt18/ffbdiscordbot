import discord
from discord.ext import commands

class Responses(commands.Cog):
    """A set of commands to have the bot respond to you"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Responds with "Hello {your name}!"', description='Responds with "Hello {your name}!"')
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        await ctx.send(f'Hello {member.display_name}!')
        
    @commands.command(brief='Responds with "pong"', description='Responds with "pong"')
    async def ping(self, ctx):
        await ctx.send(f'pong')

def setup(bot):
	bot.add_cog(Responses(bot))
        