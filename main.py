import discord
import os
import asyncio
from dataBase import getBatch, role_list
from classTracker import additionalReq
from schedule import schedule

#Activate the Discord Client
client = discord.Client(intents=discord.Intents.all())
#Import the private token from Environment Variables
token = os.environ['TOKEN']


#Indicate that client is activated
@client.event
async def on_ready():
    print("Bot is online")


#Message reading service
@client.event
async def on_message(message):
    channel = message.channel
    print(message.content)
    # if (message.author == client.user):
    #     return

    if message.content.startswith('$hi'):
        await message.channel.send('Hello!')

    if message.content.startswith('$hmm'):
        await message.channel.send('SUUUUUUUUUUUUUUUUUS')

    if message.content.startswith('$help'):
        batch_id = None
        author_roles = message.author.roles
        #To check role of message author to determine Batch
        for role in author_roles:
            if role.name in role_list:
                batch_id = role.name
                break

        if batch_id == None:
            #The user has no role indicating Batch
            await message.author.send("Contact Admin to get roles!")

        #Get complete information about a schedule of a batch
        cache = getBatch(batch_id)
        time_table = cache["time_table"]
        subject_list = cache["subject_list"]
        startDate, endDate = cache["dates"]

        #Get the hours attended across all subjects
        await message.channel.send(
            'Enter the classes you have attended in the required order :')
        await channel.send(', '.join(subject_list))
        response_valid = True

        def check(msg):
            #if message is sent by user in other channel
            if (msg.channel != channel):
                return False
            #if message is not sent by same user
            if (msg.author != message.author):
                return False
            #if incorrect parameters are passed
            if (len(msg.content.split(' ')) != len(subject_list)):
                return False

            return True

        try:
            #We wait 30 sec for user to provide current attendance
            msg = await client.wait_for('message', check=check, timeout=30)
            if not response_valid:
                return 'Please enter a valid response'

        except asyncio.TimeoutError:
            return 'Sorry, you took too long to respond'

        att = msg.content.split()
        attendance = {}
        for i in range(0, len(subject_list)):
            attendance[subject_list[i]] = int(att[i])

        #Extract classes to be attended
        classes = additionalReq(time_table, subject_list, attendance,
                                startDate, endDate)

        print("classes: ", classes)
        #Extract optimal schedule
        best_schedule = schedule(time_table, classes, startDate, endDate)
        print("best: ", best_schedule)
        schedule_txt = ""
        for weekday, cnt in best_schedule.items():
            schedule_txt += f"{weekday}: {str(cnt)}\n"

        await message.channel.send(
            "Your customized schedule is on the way *winks")
        await message.author.send(schedule_txt)


# from discord.ext import commands

# intents = discord.Intents.all()
# client = commands.Bot(command_prefix="!", intents=intents)


# @client.event
# async def on_ready():
#     print("Im Ready")


# @client.command()
# async def dm_all(ctx, *, args=None):
#     if args != None:
#         members = ctx.guild.members
#         for members in members:
#             try:
#                 await member.send(args)
#             except:
#                 print("Didn't Work!!!")
#     else:
#         await ctx.send("Please provide an argument!")


client.run(token)
