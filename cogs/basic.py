from discord.ext import commands
from utils import text_to_owo

class Basic(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx,ex):
        print(ex)
        await ctx.send("Please check with *help the usage of this command or talk to administrator")

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("pong")

    @commands.command()
    async def owo(self,ctx):
        await ctx.send(text_to_owo(ctx.message.content))

    @commands.command()
    @commands.guild_only()
    async def invite(self,ctx):
        link = await ctx.channel.create_invite(max_age=1)
        await ctx.send(link)




def setup(bot):
    bot.add_cog(Basic(bot))