import discord
from discord.ext import commands
import os
import sys
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("api-token")
host_id = os.environ.get("mem_id")

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.voice_states = True
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command('help')

@bot.command()
async def load(ctx, extension):
    if ctx.author.id == host_id:
        await bot.load_extension(f'cogs.{extension}')
        await ctx.reply(f'{extension} has been loaded')
    else:
        await ctx.reply("no perms")


@bot.command()
async def unload(ctx,extension):
    if ctx.author.id == host_id:
        await bot.unload_extension(f'cogs.{extension}')
        await ctx.reply(f'{extension} has been unloaded')
    else: 
        await ctx.reply("no perms")
        
@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == host_id:
        await bot.reload_extension(f'cogs.{extension}')
        await ctx.reply(f'{extension} has been reloaded')
    else:
        await ctx.reply("no perms")


@bot.command()
async def unloadall(ctx):
    if ctx.author.id == host_id:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.unload_extension(f'cogs.{filename[:-3]}')
        await ctx.send("Unloaded Everything")
    else:
        await ctx.reply("no perms, contact admin")

@bot.command()
async def reloadall(ctx):
    if ctx.author.id != host_id:
        await ctx.reply("no perms, contact admin")
    for filename in os.listdir('./cogs' ):
        if filename.endswith('.py'):
            await bot.unload_extension(f'cogs.{filename[:-3]}')
            await bot.load_extension(f'cogs.{filename[:-3]}')
        await ctx.send("Reloaded Everything")
        

@bot.command()
async def loadall(ctx):
    if ctx.author.id != host_id:
        await ctx.reply("no perms, contact admin")
    else:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')
        await ctx.send("loaded Everything")            

@bot.group(invoke_without_command=True)
async def help(ctx):
    embed = discord.Embed(title = "help", description="use .help <command>")
    embed.add_field(name="Moderation", value="ban, kick")
    embed.add_field(name="Test", value="test")
    embed.add_field(name="Filters", value="chatfilter, emojifilter")
    embed.add_field(name="Fun", value="alert, ask")
    await ctx.reply(embed=embed)
    print("works")


@help.command()
async def ask(ctx):
    embed = discord.Embed(title="Ask", description="Talk to llama3 AI model")
    embed.add_field(name="args", value=".ask <message>")
    await ctx.reply(embed=embed)

@help.command()
async def ban(ctx):
    embed = discord.Embed(title="Ban", description="bans")
    embed.add_field(name = "args", value=".ban <member> <reason>")
    await ctx.reply(embed = embed)

@help.command()
async def chatfilter(ctx):
    embed = discord.Embed(title="Chatfilter", description="Turn it on or off")
    embed.add_field(name="args", value=".unload/load chatfilter")
    await ctx.reply(embed=embed)

@help.command()
async def emojifilter(ctx): 
    embed = discord.Embed(title="emojifilter", description="Turn it on or off")
    embed.add_field(name="args", value=".unload/load emojifilter")
    await ctx.reply(embed=embed)


@help.command()
async def kick(ctx):
    embed = discord.Embed(title="kick", description="kicks")
    embed.add_field(name = "args", value=".kick <member> <reason>")
    await ctx.reply(embed = embed)
    
@help.command()
async def test(ctx):
    embed = discord.Embed(title="test", description="test commmand")
    embed.add_field(name = "args", value=".test")
    await ctx.reply(embed = embed)

@bot.event
async def setup_hook():
    for filename in os.listdir('./cogs'):
        if filename == "ai_request.py":
                continue
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(token)


