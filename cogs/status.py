import discord
from discord.ext import commands

class status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command() # type: ignore
    async def status(self, ctx, name1):
        await self.bot.change_presence(activity=discord.Game(name=name1))
        await ctx.reply("done")
    

async def setup(bot):
    await bot.add_cog(status(bot))