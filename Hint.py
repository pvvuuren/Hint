import discord
import asyncio
import random
from messages import messages_list
from copy import deepcopy

var key = process.env.BOT_TOKEN;
#key = open("ID.txt","r").readline()
client = discord.Client()

async def background_loop():
    await client.wait_until_ready()
    await client.change_presence(game=discord.Game(name="Cloak & Dagger"))
    messages = deepcopy(messages_list)
    cleanmessages = deepcopy(messages_list)
    while not client.is_closed:
        channel = client.get_channel("242956769503084544")
        if not messages:
            messages = deepcopy(cleanmessages)
        await client.send_message(channel, messages.pop(random.randrange(0, len(messages))))
        await asyncio.sleep(21600)

client.loop.create_task(background_loop())
client.run(key)