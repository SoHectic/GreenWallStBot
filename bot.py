import discord
import random
import os
import shutil
from discord.ext import commands, tasks
from discord.utils import get

client = commands.Bot(command_prefix = '-')
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is Ready!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Developed By Hectic'))

@client.event
async def on_message(message):
    if message.channel.id == client.get_channel(os.environ['listen-channel']):
        target_channel = client.get_channel(os.environ['target-channel'])
        await target_channel.send(message.content)
    else:
        await client.process_commands(message)
client.run(os.environ['TOKEN'])