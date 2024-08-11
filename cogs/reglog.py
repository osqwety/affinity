import discord
from discord.ext import commands
from datetime import datetime

class reglog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
        try:
            file1 = open(r"\BFB_Logs\Regular_Log.txt", "a")
            file1.write(f"NAME: {message.author} CONTENT:''{message.content}'' TIME: {now}\n")
        except UnicodeEncodeError:
            file1.write(f"NAME: {message.author} CONTENT:'Emoji(exception)' TIME: {now}\n")

        #if message.author.id == 695309094667681883:
         #   await message.delete()
          #  print(f"{message.content} // {message.author.name}")
        #if message.author.id == 970397215673696398:    
         #   await message.delete()
async def setup(bot):
    await bot.add_cog(reglog(bot))
