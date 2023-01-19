import discord
from dotenv import load_dotenv
import os

#Credentials
load_dotenv('.env')


intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')


client.run(os.getenv('discordToken'))