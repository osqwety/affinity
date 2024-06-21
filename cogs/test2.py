import discord
from discord.ext import commands

class test2(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command()  # type: ignore
    async def test(self,ctx, member:discord.Member):
        await ctx.reply(f'this cog work {member.mention}')




async def setup(bot):
    await bot.add_cog(test2(bot))