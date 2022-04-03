from discord.ext import commands

bot = commands.Bot(command_prefix="*")

@commands.command()
async def ping(ctx):
    await ctx.send("Pong")

bot.add_command(ping)

@commands.command(description="provide arguments" ,brief="this is brief")
async def hello(ctx, *args):
    if len(args) > 0:
        await ctx.send(" ".join(args))
    else:
        await ctx.send("Please refer to help")

bot.add_command(hello)

bot.run(DISCORD_BOT_TOKEN)