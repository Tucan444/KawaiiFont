import asyncio

import discord
import random
import json
import os
from discord.ext import commands

intents = discord.Intents.all()


client = commands.Bot(command_prefix=lambda x, y: ".", intents=intents)


@client.event
async def on_ready():
    print("KawaiiFont is ready.")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(".your text"))


@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx):
    try:
        for ext in os.listdir("extensions"):
            if ext.endswith(".py"):
                try:
                    await client.unload_extension(f"extensions.{ext[:-3]}")
                except:
                    pass
                await client.load_extension(f"extensions.{ext[:-3]}")
        await ctx.send(f"Reloaded all extensions successfully.")
    except Exception as e:
        await ctx.send(e)


async def loadExtensions():
    try:
        for ext in os.listdir("extensions"):
            if ext.endswith(".py"):
                await client.load_extension(f"extensions.{ext[:-3]}")
    except Exception as e:
        print(e)

asyncio.run(loadExtensions())

client.run("not twice")
