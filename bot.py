import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord.ext import commands


bot = commands.Bot(command_prefix='>')

bot.remove_command('help')

@bot.event
async def on_ready():
    print(discord.__version__)
    print ("Initializing")
    print ("Loading Commands")
    print ("Succesful Startup!")
    print ("Recovery Bot online")
    await bot.change_presence(game=discord.Game(name=">help | Version 0.1.5"))



@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id='488015963049033728')
    await bot.add_roles(member, role)

@bot.event
async def on_member_join(member):
    embed=discord.Embed(title=" :wave: Thank you for joining the Rocket Store discord!", color=0x04FF00)
    embed.add_field(name="Please use >help to see what Rocket Bot has to offer you!", value="Enjoy your stay!", inline=True)
    await bot.send_message(member, embed=embed)

@bot.command(pass_context = True)
@commands.has_role('Dev')
async def dm(ctx, member : discord.Member, *, content: str):
    await bot.send_message(member, content)

@bot.command(pass_context=True)
@commands.has_role('Dev')
async def message_role(ctx, role: discord.Role, *, message):
    for member in ctx.message.server.members:
        if role in member.roles:
            await bot.send_message(member, message)

@bot.command(pass_context=True)
@commands.has_role('Dev')
async def clear(ctx, amount):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Messages cleared!")

@bot.command(pass_context = True)
@commands.has_role('Dev')
async def receipt(ctx, *, member : discord.Member):
    embed=discord.Embed(title=" :white_check_mark: Confirmation receipt", color=0x04FF00)
    embed.add_field(name="Your order has been processed and confirmed!", value="Thank you for using Galaxy's Services!", inline=True)
    await bot.send_message(member, embed=embed)

@bot.command(pass_context = True)
@commands.has_role('Dev')
async def update(ctx):
        embed = discord.Embed(title="Update notes for Version 0.1.5", color=0xffffff)
        embed.add_field(name="Added >ask command", value="Simply use >ask 'your question' in my DM's to ask us a question!", inline=True)
        embed.add_field(name="Added >faq command", value="Displays the Frequently asked questions (In developement)", inline=True)
        embed.add_field(name="Updated AI aspect of Rocket Bot", value="New goodies!", inline=True)
        await bot.say(embed=embed)
        

@bot.command(pass_context=True)
@commands.has_role('Dev')
async def mg(ctx, channel : discord.Channel, *, content):
    await bot.send_message(channel, content)

@bot.command(pass_context=True)
async def ask(ctx, content):
    user = discord.utils.get(bot.get_all_members(), id='487961373918363667')
    await bot.send_message(user, f"USERID: {ctx.message.author.id} Asked the following: {content}")
@bot.event
async def on_message(message):
    await bot.process_commands(message) 

    channel = bot.get_channel('488346032552411156')
    if message.server is None and message.author != bot.user:
        await bot.send_message(channel, f"USERID: {message.author.id} Said: {message.content}")
    if message.content.startswith('>help'):   
        embed=discord.Embed(title="Help", color=0xd533b5)
        embed.add_field(name="Type '>request' and then the package you desire", value="use '>packages' to display all available packages", inline=True)
        await bot.send_message(message.author, embed=embed)

    if message.content.startswith('>packages'):
        embed = discord.Embed(title="Packages", description="If interested in either of these packages type >request 'package name here' ", color=0xEE16F8)
        embed.add_field(name="Starter Recovery ($2,50)", value="- $100,000,000 in game currency \n - Level 120 \n - Unlock all (does not include stats)", inline=False)
        embed.add_field(name="Planetary Recovery ($5,00)", value="- $250,000,000 in game currency \n - Level 180 \n - Unlock all (Cars, clothing, weapons and stats)", inline=False)
        embed.add_field(name="Solar Recovery ($7,50)", value="- $500,000,000 in game currency \n - Level 240 \n - Unlock all (Cars, clothing, weapons and stats)", inline=False)
        embed.add_field(name="Galaxy Recovery ($10,00)", value="- Custom amount of in game currency \n - Custom level \n - Unlock all (Cars, clothing, weapons and stats)", inline=False)
        embed.add_field(name="Money drop ($12,00/hour)", value="- Drop rate: $9,000,000/hour \n - Will not affect your level \n - Does not include unlock all \n - Ban rate = 0%", inline=False)
        await bot.send_message(message.author, embed=embed)
    
    user = discord.utils.get(bot.get_all_members(), id='487961373918363667')
   
    if message.content.startswith('>request starter'):
        embed=discord.Embed(title="Request confirmation", color=0x04FF00)
        embed.add_field(name="Your request for the starter recovery is being processed", value="Please be patient while waiting for the recovery bot to respond with your reciept", inline=True)
        await bot.send_message(message.author, embed=embed)
        await bot.send_message(user, f"USERID: {message.author.id} Requested a Starter recovery")
        
    
    if message.content.startswith('>request planetary'):
        embed=discord.Embed(title="Request confirmation", color=0x04FF00)
        embed.add_field(name="Your request for the planetary recovery is being processed", value="Please be patient while waiting for the recovery bot to respond with your reciept", inline=True)
        await bot.send_message(message.author, embed=embed)
        await bot.send_message(user, f"USERID: {message.author.id} Requested a Planetary recovery")
        
    
    if message.content.startswith('>request solar'):
        embed=discord.Embed(title="Request confirmation", color=0x04FF00)
        embed.add_field(name="Your request for the Solar recovery is being processed", value="Please be patient while waiting for the recovery bot to respond with your reciept", inline=True)
        await bot.send_message(message.author, embed=embed)
        await bot.send_message(user, f"USERID: {message.author.id} Requested a Solar recovery")
        
    
    if message.content.startswith('>request galaxy'):
        embed=discord.Embed(title="Request confirmation", color=0x04FF00)
        embed.add_field(name="Your request for the Galaxy recovery is being processed", value="Please be patient while waiting for the recovery bot to respond with your reciept", inline=True)
        await bot.send_message(message.author, embed=embed)
        await bot.send_message(user, f"USERID: {message.author.id} Requested a Galaxy recovery")
    

        
bot.run(os.environ['BOT_TOKEN'])
