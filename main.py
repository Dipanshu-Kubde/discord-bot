import os

from discord.ext import commands

from settings import *


bot = commands.Bot(command_prefix="&&")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

# bot.load_extension(f'cogs.test')
# bot.load_extension(f'cogs.basic')

# print(DISCORD_BOT_TOKEN)
bot.run('')

# https://discord.gg/CcXKd9wKz4
# https://discord.gg/gqwhn3NVuX
# https://discord.gg/zhp9KwkpjN