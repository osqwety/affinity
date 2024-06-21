import discord

from discord.ext import commands

x = 0
class alert(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    

    @commands.command() # type: ignore
    async def alert(self,ctx, member:discord.Member,msg,ts):
        global x
        global ts1
        ts1 = ts
        ch2 = member.dm_channel
        if ch2 is None:
            ch2 = await member.create_dm()
            await ctx.reply("Alert Succesful!")
        else:
            #await member.send(f"ALERT!! {member.mention} '{msg}' BY {ctx.author.name}")
            #print(x)
            await ctx.reply("Alert Succesful!")
        for x in range(int(ts)):
            await member.send(f"ALERT!! {member.mention} '{msg}' BY {ctx.author.name}")
            print(x)
            if x >= int(ts):
                break

    @commands.command() #type: ignore
    async def acancel(self,ctx):
        global x
        x = 1 + int(ts1)
        await ctx.send("Cancelled")
            #if msg.content == "acancel":
             #   break
            #if self.client.unload_extension():
             #   break

async def setup(bot):
    await bot.add_cog(alert(bot))