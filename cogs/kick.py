import discord
from discord.ext import commands

class kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command() # type: ignore
    async def kick(self, ctx, member:discord.Member, reason:str):
        await member.kick(reason=reason)
        await ctx.reply(f'{member.mention} has been kick because "{reason}!"')


async def setup(bot):
    await bot.add_cog(kick(bot))