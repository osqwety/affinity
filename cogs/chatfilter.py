import discord
from discord.ext import commands
from datetime import datetime
class chatfilter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_message(self, message):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
        chal2 = self.bot.get_channel(1136976877194584134)
        blocked_words = ["shit","shii","shi","schit"]
        timings = ["am", "pm"]
        message_lower = "".join(dict.fromkeys(message.content.lower()))
        for word in blocked_words:
            if word == message_lower: 
                emb = discord.Embed(title="blocked word", description=f"'{message.content}' by {message.author} at {now}")
                if message.guild.id == 1054890085331509379:
                    await chal2.send(embed = emb)
                    await message.delete() 
                else:
                    print(f"{message.guild.name} // {message.author.name} // '{message.content}'")
                    await message.delete()

        if message.channel.id == 1154456335929315489:
                if str(message.content.lower()).split(' ')[-1] in timings:
                    pass
                else:
                    await message.delete()

    
    
async def setup(bot):
    await bot.add_cog(chatfilter(bot))