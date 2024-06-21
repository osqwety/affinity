import discord
from discord.ext import commands

class tmfilter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_message(self, message):
        timings = ["am", "pm"]
        #num = ["10", "20"]
        #timings = 'am'
        #timng = ["pm", "am"]
        #data = message.content.split(' ')

        if message.channel.id == 1154456335929315489:
                if str(message.content.lower()).split(' ')[-1] in timings:
                    pass
                else:
                    await message.delete()
                
    
async def setup(bot):
    await bot.add_cog(tmfilter(bot))
