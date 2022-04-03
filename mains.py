import discord

COMMAND_PREFIX = '*'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))


    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        # don't respond to ourselves
        if message.author.bot:
            return

        

        if message.content[0] != COMMAND_PREFIX:
            return

        cmd_arg = message.content.split(" ")
        cmd = cmd_arg[0]
        args = list()
        if len(cmd_arg) > 1:
            args = cmd_arg[1]

        if cmd == "*hello":
            await message.channel.send(args)

        elif cmd == '*ping':
            await message.channel.send('pong')


client = MyClient()
client.run(DISCORD_BOT_TOKEN)