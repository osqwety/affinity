import discord
from discord.ext import commands
from datetime import datetime

class editlog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
        try:
            file4 = open(r"\BFB_Logs\editedmsg.txt", "a")
            file4.write(f"NAME: {message_before.author.name} CONTENT BEFORE:''{message_before.content}'' CONTENT AFTER:''{message_after.content}''TIME: {now}\n")
        except UnicodeEncodeError:
            file4 = open(r"\BFB_Logs\editedmsg.txt", "a")
            file4.write(f"NAME: {message_before.author.name} CONTENT BEFORE:''Emoji'' CONTENT AFTER:''Emoji''TIME: {now}\n")

    
async def setup(bot):
    await bot.add_cog(editlog(bot))
