import discord
from discord.ext import commands
from datetime import datetime
import sys
import smtplib
import os
sys.path.append(r"*\bot\.env")

from dotenv import load_dotenv
load_dotenv()
email = os.environ.get("email")



class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def report(self, ctx): 
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")
        ctx123 = ctx.message.content[8:]
        print(f"Incident: {ctx123} Author: {ctx.message.author.name} Time: {now}", file=sys.stderr)
        
        sender = email
        receiver = email
        password = "gdpl ekwj erlr jlvv"
        sub = "Incident Report, BFB"
        body = f"Incident: {ctx123} Author: {ctx.message.author.name} Time: {now}"
        message = f"""From, {sender}
        To: {receiver}
        Subject: {sub},
        {body}
        """

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender, password)
        print("Logged in ig")
        server.sendmail(sender, receiver, message)
        print("sent") 


async def setup(bot):
    await bot.add_cog(report(bot))
