#write a discord bot using the discord.py library
import discord

#initialize the bot
intents = discord.Intents.all()
client = discord.Client(intents=intents)

#when the bot is ready
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#when a message is sent
@client.event
async def on_message(message):
    #if the message is from the bot itself, ignore it
    if message.author == client.user:
        return

    #if the message is "hello"
    if message.content.startswith('hello'):
        #send a message back
        await message.channel.send('Hello!')

#run the bot
client.run('token')

