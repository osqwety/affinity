import discord
from discord.ext import commands

class offline(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command() # type: ignore
    async def offline(self, ctx):
        await self.bot.change_presence(status=discord.Status.offline)
        await ctx.reply("Done")


async def setup(bot):
    await bot.add_cog(offline(bot))