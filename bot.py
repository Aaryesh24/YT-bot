import asyncio 
from asyncio import sleep
import aiohttp
from aiohttp import client
import discord
from discord import channel
from discord.ext import commands, tasks
from discord.ext.commands import bot
from discord.utils import get


# skyblock - 906477129405988934, techno - 905876048112136302

# client = commands.Bot(command_prefix='!')
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot is ready.')
    OnlineCheck.start()

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency = {round(bot.latency * 1000)}ms')

@bot.command()
async def hi(ctx):
    channel = bot.get_channel(905876048112136302)
    await channel.send('Hi there!')

@tasks.loop(seconds = 120)
async def OnlineCheck():
    channel = bot.get_channel(905876048112136302)
    ign = "Technoblade"
    api_key = "f244c238-0430-48f7-a597-23077c05c321"
    uuid = "b876ec32e396476ba1158438d83c67d4"

    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://api.hypixel.net/status?key={api_key}&uuid={uuid}') as response:
            response = await response.json()
            await session.close()
    if (response["session"]["online"] == True):
            await channel.send(f"@everyone {ign} is ONLINE")

@tasks.loop(seconds = 120)
async def OnlineCheck():
    channel = bot.get_channel(905876048112136302)
    ign = "TommyInnit"
    api_key = "f244c238-0430-48f7-a597-23077c05c321"
    uuid = "e80e8194323e414298515e1bcb8a3508"

    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://api.hypixel.net/status?key={api_key}&uuid={uuid}') as response:
            response = await response.json()
            await session.close()
    if (response["session"]["online"] == True):
            await channel.send(f"@everyone {ign} is ONLINE")

@tasks.loop(seconds = 120)
async def OnlineCheck():
    channel = bot.get_channel(905876048112136302)
    ign = "Tubbo"
    api_key = "f244c238-0430-48f7-a597-23077c05c321"
    uuid = "b25efb42bda644138da94eae3d345746"

    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://api.hypixel.net/status?key={api_key}&uuid={uuid}') as response:
            response = await response.json()
            await session.close()
    if (response["session"]["online"] == True):
            await channel.send(f"@everyone {ign} is ONLINE")

@tasks.loop(seconds = 120)
async def OnlineCheck():
    channel = bot.get_channel(905876048112136302)
    ign = "Refraction"
    api_key = "f244c238-0430-48f7-a597-23077c05c321"
    uuid = "28667672039044989b0019b14a2c34d6"

    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://api.hypixel.net/status?key={api_key}&uuid={uuid}') as response:
            response = await response.json()
            await session.close()
    if (response["session"]["online"] == True):
            await channel.send(f"@everyone {ign} is ONLINE")

@tasks.loop(seconds = 120)
async def OnlineCheck():
    channel = bot.get_channel(905876048112136302)
    ign = "56ms"
    api_key = "f244c238-0430-48f7-a597-23077c05c321"
    uuid = "1277d71f338046e298d90c9fe4055f00"

    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://api.hypixel.net/status?key={api_key}&uuid={uuid}') as response:
            response = await response.json()
            await session.close()
    if (response["session"]["online"] == True):
            await channel.send(f"@everyone {ign} is ONLINE")


bot.run('OTA1ODc0NTYzODk0NzQ3MTU3.YYQbbg.P_o8TAarKqRO0Ae4lKmoyeMromo')
