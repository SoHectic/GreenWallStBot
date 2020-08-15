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
    if message.channel.id == client.get_channel(735165097021800571):
        target_channel = client.get_channel(529039796404879370)
        await target_channel.send(message.content)

client.run(os.environ['TOKEN'])