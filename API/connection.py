# connection.py
import os

# imports discord api
import discord
from dotenv import load_dotenv

# loads the api 
load_dotenv()

# sets the default token and guild
TOKEN = os.getenv('NzUzNzE4NTcyNTUwNzE3NTA2.X1qRHw.M8kuXrb6EozDpeNH1Gn6faxnlns')
GUILD = os.getenv('https://discord.gg/JaW49Q')

# sets default client to discord main servers
client = discord.Client()


# creates a new client event 
@client.event
# creates a new function that triggers when the bot is loaded on guild
async def on_ready():
    # enters a loop that checks if the bot is on the correct guild
	for guild in client.guilds:
        if guild.name == GUILD:
            break

	# if it is on the right server it prints out a connection message
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    
# TEST: Will Print Out Message if it works correctly    
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


# runs the bot on our discord guild
client.run(NzUzNzE4NTcyNTUwNzE3NTA2.X1qRHw.M8kuXrb6EozDpeNH1Gn6faxnlns)
