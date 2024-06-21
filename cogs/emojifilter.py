import discord
from discord.ext import commands

class emojifilter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('🇮🇱'):
            await message.delete()
            print('ky')

        data = message.content.split(' ')
        for i in data:
            if "🇮🇱" == i:
                await message.delete()  
                
        

        #if message.content.lower() == "🇮🇱":
         #   await message.delete()
          #  print('kys2')
    
async def setup(bot):
    await bot.add_cog(emojifilter(bot))