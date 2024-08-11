import discord
from discord.ext import commands
from datetime import datetime

class deletedlog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
        if message.author.name is not self:
            file3 = open(r"\BFB_Logs\Deleted_user.txt", "a")
            file3.write(f"**NAME: {message.author.name} CONTENT:''{message.content}'' TIME: {now}\n")

    
async def setup(bot):
    await bot.add_cog(deletedlog(bot))
