import discord
from discord.ext import commands
import sys
import time

sys.path.append(r"*\BFB-Bot\ai_request.py")
from ai_request import main_ai2

class ask(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command() #type: ignore
    async def ask(self, ctx):
        if ctx.guild.id == 1054890085331509379:
            await ctx.reply("This server is not allowed to use this comamnd.")
        else:
            y = str(ctx.message.content)
            print(y[5:])
            x = main_ai2(y[5:])
            if len(x) >= 2000:
                f1 = open(r"\BFB-Bot\AI_Response.txt", "w")
                f1.write(x)
                f1.close()
                await ctx.reply(file=discord.File(r"\BFB-Bot\AI_Response.txt"))
            else:
                await ctx.reply(x)
        #await message.author.send(f"{x}")



async def setup(bot):
    await bot.add_cog(ask(bot))
        