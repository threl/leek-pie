import os, discord
from discord.ext import commands

bot = commands.Bot(os.environ['COMMAND_PREFIX'])

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-------')

@bot.command()
async def leek(ctx):
    msg = "Ada yang mau league, " + os.environ['ROLE_LEAGUE'] + "?"
    await ctx.send(msg)

bot.run(os.environ['BOT_TOKEN'])
