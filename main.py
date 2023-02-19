from keep_alive import keep_alive
import random
import time
import discord
from discord.ext import commands
import os
import datetime;
import json

bot = discord.Bot()
my_secret = os.environ['smartyPantsKey']
guild = 1065744363260481676;

intents = discord.Intents.default()
intents.message_content = True
client=discord.Client(intents=intents)
"""
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
"""
def createImages():
	images = ["https://media.discordapp.net/attachments/926186654128037938/1068203173833080862/rn_image_picker_lib_temp_8f529f91-d9b0-44d0-b5c9-fcd1b539c895.jpg?width=507&height=676", "https://media.discordapp.net/attachments/926186654128037938/1074685167341404170/SPOILER_694B024E-6ED7-4596-90CF-F8CD479D7073.png?width=540&height=676", "https://media.discordapp.net/attachments/926186654128037938/1030271290210263061/IMG_20221013_123900.jpg?width=507&height=676", "https://media.discordapp.net/attachments/1065744364300685355/1076660300738203668/uranus-trump.jpg", "https://tenor.com/bPZcS.gif"]
	with open("images.txt", "w") as fp:
		json.dump(images, fp)


with open("images.txt", "r") as fp:
	images = json.load(fp)

@bot.command(guild_ids=[guild], name="list", description = "Return the list of images")
async def list(ctx):
	await ctx.respond(images)
	
@bot.command(name = "ping", description="Sends the bot's latency.")
async def ping(ctx): 
    await ctx.respond(f"Pong! Latency is {bot.latency}")

@bot.command(name="pop", guild_ids=[guild], description = "Remove an image from the list")
async def pop(ctx, index: int):
	images.pop(index)
	with open("images.txt", "w") as fp:
		json.dump(images, fp)
	await bot.get_channel(1076660535573098536).send(images)
	await ctx.respond(index + " popped!")


	

@bot.slash_command(name="append", guild_ids=[guild], description = "Add an image to the list")
async def append(ctx, url: discord.Option(discord.SlashCommandOptionType.string)):
	images.append(url)
	channel = client.get_channel(1076660535573098536)
	with open("images.txt", "w") as fp:
		json.dump(images, fp)
	await bot.get_channel(1076660535573098536).send(images)
	await ctx.respond(url + " appended!")


@bot.slash_command(name="report", description = "Report a problem such as a broken image") 
async def report(ctx, report: discord.Option(discord.SlashCommandOptionType.string)):
	channel = client.get_channel(1076660535573098536)
	x = str(f"{ctx.author}\nReport: " + report)
	await bot.get_channel(1076660535573098536).send(f"{ctx.author}" + '\n' + "Report: " + report)
	await ctx.respond("Problem reported!")


@bot.slash_command(name="image", description = "Generate a random image") 
async def image(ctx):
	c = random.choice(images)
	await ctx.respond(c)
	channel = client.get_channel(1076660535573098536)
	x = datetime.datetime.now()
	strang = x.strftime("%c") + ": " + c
	await bot.get_channel(1076660535573098536).send(strang)

@bot.event
async def on_ready():
	print(f'we have logged in as {bot.user}')

"""
@client.event
async def on_message(message):
	
	if message.author == client.user:
		return

	if message.content.startswith('Smarty Pants is so expensive'):
		iuashisfad = 14678
		while True:
			time.sleep(1)
			await message.channel.send(iuashisfad)
			iuashisfad += 1
	if message.content.startswith("Smarty Pants is my friend"):
		time.sleep(10)
		await message.channel.send("Magic 8 Ball is my friend")
	if message.content.startswith("bals"):
		await message.channel.send("bals")
		while True:
			if time.time()%86400==0:
				await message.channel.send("Good Morning!")
"""


keep_alive()
bot.run(my_secret)