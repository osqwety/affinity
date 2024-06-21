import discord
from discord.ext import commands

class ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command() # type: ignore
    async def ban(self, ctx, member:discord.Member, reason:str):
        await member.ban(reason=reason)
        await ctx.reply(f'{member.mention} has been banned cuz {reason}!')


async def setup(bot):
    await bot.add_cog(ban(bot))

