import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------')

@bot.command()
async def leek(ctx):
    await ctx.send("Ada yang mau league, @everyone?")

bot.run(os.environ['BOT_TOKEN'])
