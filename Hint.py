import os
import discord
import asyncio
import random
from messages import messages_list
from copy import deepcopy

key = os.environ['BOT_TOKEN']

client = discord.Client()

async def background_loop():
    await client.wait_until_ready()
    await client.change_presence(game=discord.Game(name="Cloak & Dagger"))
    last_message = None
    messages = deepcopy(messages_list)
    cleanmessages = deepcopy(messages_list)
    while not client.is_closed:
        channel = client.get_channel("360701697963851776")
        if not messages:
            messages = deepcopy(cleanmessages)
        if len([x async for x in client.logs_from(channel, limit=2, after=last_message)]) > 1:
            content = messages.pop(random.randrange(0, len(messages)))
            last_message = await client.send_message(channel, content)
            await asyncio.sleep(60)

client.loop.create_task(background_loop())
client.run(key)