import discord
import os
import asyncio
from cse24 import time_table, subject_list

client = discord.Client(intents=discord.Intents.all())
token = os.environ['TOKEN']


@client.event
async def on_ready():
    print('The Bot is up and running to help you Bunk classes as {0.user}'.
          format(client))


@client.event
async def on_message(message):
    channel = message.channel
    print(message.content)
    if (message.author == client.user):
        return

    if message.content.startswith('$hi'):
        await message.channel.send('Hello!')

    if message.content.startswith('$hmm'):
        await message.channel.send('SUUUUUUUUUUUUUUUUUS')

    if message.content.startswith('$help'):
        await message.channel.send(
            'Enter the classes you have attended in the required order :')
        await channel.send(', '.join(subject_list))

        l = len(subject_list)

        def check(m):
            #print(m.content)
            if (m.channel != channel):
                return False
            if (m.author != message.author):
                return False
            str = m.content.split(' ')
            if len(str) != l:
                return False

            return True

        try:
            msg = await client.wait_for('message', check=check, timeout=40.0)
        except asyncio.TimeoutError:
            return await channel.send('Sorry, you took too long to respond')
        # batch = msg[0:1]
        # branch = msg[3:]
        await channel.send(msg)

        await message.channel.send(f'User Choosed {msg.content}')

        #Now we have Branch and year details which we will use to reference to time table
        #


client.run(token)
