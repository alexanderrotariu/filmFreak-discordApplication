import discord
from dotenv import load_dotenv
import os

#Credentials
load_dotenv('.env')


intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('bot online')
    
@client.event
async def on_message(message):
    #read the contents of a message

    #channel = client.get_channel(1030698526075785298)
    #await channel.send('testing')
    if message.author == client.user:
        return
    
    if message.content.startswith("!ping"):
        await message.channel.send("pong")

    print(message.author, message.content, message.channel.id)
    await message.channel.send("hello!")
#     pass

'''
@client.command()
async def hello(ctx):
    channel = client.get_channel(1033759192596619386)
    await channel.send(f'hello there {ctx.author.mention}')
'''

client.run(os.getenv('discordToken'))