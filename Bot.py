import discord
from discord.ext import commands
import asyncio

bot=commands.Bot(command_prefix='!')
@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name='Fortnite!' , type=1))
    print('--------------------')


	 	 	 
@bot.command()
async def pings():
	await bot.say('ping_pong')
	
@bot.command()
async def leef():
	await bot.say('Amin is 10')
	
@bot.command()
async def epic():
	await bot.say('TTV hapxz')
	
@bot.command()
async def yt():
	await bot.say('Soon!')
	
@bot.command()
async def staf():
	await bot.say('Clearly White jokerlol smicha')
	
@bot.command()
async def mage():
	await bot.say('Clearly White')

@bot.command(pass_context=True)
async def mute(ctx,target:discord.Member):
	role=discord.utils.get(ctx.message.server.roles,name='Muted')

	await bot.add_roles(target,role)
	
	
@bot.command(pass_context=True)
async def warn(ctx,target:discord.Member):
	await bot.send_message(target,'warning!!')
	
@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member):
	await bot.kick(target)
	await bot.say(f'{target} Has been Kicked!')
	
@bot.command(pass_context=True)
async def rank(ctx,target:discord.Member):
	await bot.send_message(target,'your staf!!')
	
@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
	await bot.ban(target)   
	await bot.say(f'{target} Has been Banned!')

@bot.command(pass_context=True)
async def Member(ctx,target:discord.Member):
	role=discord.utils.get(ctx.message.server.roles,name='Member')

	await bot.add_roles(target,role)

@bot.command(pass_context=True)
async def ping(ctx):
    t = await bot.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await bot.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))

    
       
                
@bot.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number: int):
  purge = await bot.purge_from(ctx.message.channel, limit = number+1)
                            
    
@bot.event
async def on_message(message):
    if message.content.startswith('C!lolbu'):
        embed = discord.Embed(title="HELP", description="You got LoLed On!")
        embed.add_field(name="everyone", value="ping leef epic yt staf mage", inline=False)
        embed.add_field(name="LoL", value="LoL", inline=False)
        await bot.send_message(message.channel, embed=embed)    
    
    
    
   
    
bot.run('NTUwOTc1MzQ0ODI4NzQzNjgx.D1qPbA.FFtHM_V87K4GGbgHBvP5seRNUYU')
