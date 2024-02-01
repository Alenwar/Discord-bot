import os
import aiohttp
import discord
import random
from discord.ext import commands

API_KEY ="YOUR IP"

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} has connected to Discord!')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello")

@bot.command()
async def info(ctx, arg=None):
    author = ctx.message.author
    if arg == None:
        await ctx.send(f"{author.mention} Please enter:: \n!info movie \n!info about")
    elif arg == "movie":
        await ctx.send(f"{author.mention} Random movie")
    elif arg == "about":
        await ctx.send(f"{author.mention} I'm a bot for finding a random movie")
    else:
        await ctx.send(f"{author.mention} Сommand not recognized")

@bot.command()
async def movie(ctx):
    async with aiohttp.ClientSession() as session:
        movie_id = random.randint(1, 551)
        movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
        async with session.get(movie_url) as response:
            data = await response.json()

        if 'original_title' in data:
            title_name = data['original_title']
            release_date = data['release_date']
            overview = data['overview']
            message = f"Random Movie: {title_name} ({release_date})\nOverview: {overview}"
            await ctx.send(message)
        else:
            await ctx.send("Error fetching movie information.")


@bot.event
async def on_member_join(member):
    await member.send("hello, i`m bot")
    for ch in bot.get_guild(member.guild.id).channels:
        if ch.name == "chat":
            await bot.get_channel(ch.id).send(f"{member.mention} hi, nice to meet you!")

@bot.event
async def on_member_remove(member):
    for ch in bot.get_guild(member.guild.id).channels:
        if ch.name == "chat":
            await bot.get_channel(ch.id).send(f"{member.mention} ...")



#комманда авторизации бота
bot.run(os.getenv("TOKEN"))


