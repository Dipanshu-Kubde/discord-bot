import discord
from discord.ext import commands

from utils import truthdare,truthdares


class Game(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def truth(self, ctx):
       truth = await truthdare()
    #    if member is not None:
    #        print("1")
    #        await ctx.send("%s %s " % (truth))
    #    else:
       print("we are in here")
       await ctx.send(truth)
    #  await ctx.send(insult)

    @commands.command()
    async def dare(self, ctx):
       dare = await truthdare()
    #    if member is not None:
    #        print("1")
    #        await ctx.send("%s %s " % (dare))
    #    else:
       print("we are in here")
       await ctx.send(dare)
    #  await ctx.send(insult)



def setup(bot):
    bot.add_cog(Game(bot))