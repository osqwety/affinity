import discord
from discord.ext import commands

class dm(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command() #type: ignore
    async def dm(self, message: discord.Message):
        await message.author.send(f"yes")



async def setup(bot):
    await bot.add_cog(dm(bot))
        