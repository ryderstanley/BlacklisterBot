# connection.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('YOKbMQoAiJNuNqH5-iQC29MhpPhUdPsh')
GUILD = os.getenv('https://discord.gg/JaW49Q')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

client.run(YOKbMQoAiJNuNqH5-iQC29MhpPhUdPsh)
