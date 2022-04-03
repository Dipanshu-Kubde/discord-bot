# from discord.ext import commands
# import discord
# import os
# import requests
# import json
# import random
# from replit import db
# from keep_alive import keep_alive

import random

import aiohttp
from discord.ext import commands
import discord

import praw



class Tests(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    # def get_quote():
    #     response = requests.get("https://zenquotes.io/api/random")
    #     json_data = json.loads(response.text)
    #     quote = json_data[0]['q'] + " -" + json_data[0]['a']
    #     return(quote)

    # @client.event
    # async def on_message(message):
    #     # if message.content.startswith('$inspire'):
    #         quote = get_quote()
    #         await message.channel.send(quote)

    @commands.command(brief="Random picture of a floofy")
    async def pat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://zenquotes.io/api/random") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Floof")
                    embed.set_image(url=data['image'])
                    embed.set_footer(text="https://randomfox.ca/")

                    await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(Tests(bot))