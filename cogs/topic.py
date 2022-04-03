import discord
from discord.ext import commands

from utils import questions


class Topic(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def topic(self, ctx):
       topic = await questions()
    #    if member is not None:
    #        print("1")
    #        await ctx.send("%s %s " % (topic))
    #    else:
       print("we are in here")
       await ctx.send(topic)
    #  await ctx.send(insult)



def setup(bot):
    bot.add_cog(Topic(bot))