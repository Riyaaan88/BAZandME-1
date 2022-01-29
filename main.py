#no problem its ur bot as well as mine afterall u did most of the coddeing lmao
import discord 
from discord.ext import commands, tasks
from colorama import Fore
import os
from keep_alive import keep_alive
import json
import random
import asyncio

with open("config.json", "r") as f:
  c = json.load(f)
  cver = c["version"]

client = commands.Bot(command_prefix=commands.when_mentioned_or("?"))
client.remove_command("help")

@client.event
async def on_guild_join(guild):
  print(Fore.GREEN + f"I have joined {guild}" + Fore.RESET)
  channel = client.get_channel(904020552275099658)
  console = discord.Embed(
    title="Console",
    description=f"I have joined {guild} with {guild.member_count}"
  )
  await channel.send(embed=console)

@client.event
async def on_guild_remove(guild):
  print(Fore.GREEN + f"I have left {guild}" + Fore.RESET)
  channel = client.get_channel(904020552275099658)
  console = discord.Embed(
    title="Console",
    description=f"I have left {guild} with {guild.member_count}"
  )
  await channel.send(embed=console)

@client.event
async def on_ready():
  print(Fore.BLUE + f'Successful login to {client.user}\nBot is in {len(client.guilds)} servers\nClient ID: {client.user.id}')
  change_status.start()
  channel = client.get_channel(904020552275099658)
  console = discord.Embed(
    title="Console",
    description=f"Bot has started in {len(client.guilds)} servers\nID: {client.user.id}"
  )
  await channel.send(embed=console)
  for filename in os.listdir("./cogs"):
	  if filename.endswith(".py"):
		  client.load_extension(f"cogs.{filename[:-3]}")
  for guild in client.guilds:
    with open("servers.json", "r") as f:
      guilds = json.load(f)
      if guild.id not in guilds:
        guilds[str(guild.id)] = {"Name" : guild.name, "ID": str(guild.id), "Number of users" : guild.member_count}
        with open("servers.json", "w") as f:
          json.dump(guilds, f, indent=4)
      else:
        pass
        
@client.command()
@commands.is_owner()
async def reload(ctx):
  for filename in os.listdir("./cogs"):
	  if filename.endswith(".py"):
		  client.reload_extension(f"cogs.{filename[:-3]}")

@client.command()
@commands.is_owner()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")
  
@tasks.loop(seconds=600)
async def change_status():
  await client.change_presence(activity=random.choice(activities))
  #await client.change_presence(activity=discord.Game("Under maintenance"))
  print(Fore.GREEN + "Successfully changed status!")

status = ["Made by Breadwinners and Baz!", "Invest in the Future!"]

activities = [discord.Game(name=random.choice(status)), discord.Activity(type=discord.ActivityType.competing, name=random.choice(status)), discord.Activity(type=discord.ActivityType.watching, name=random.choice(status)), discord.Activity(type=discord.ActivityType.listening, name=random.choice(status)), discord.Streaming(name=random.choice(status), url="https://twitch.tv/itzbazlol")]

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
  
@client.command()
async def unban(ctx,user: discord.User):
  guild = ctx.guild
  embed = discord.Embed(
    title = "SCORE!",
    description = f"{user} was unbanned OK!"
  )
  if ctx.author.guild_permissions.ban_members:
    await ctx.send(embed=embed)
    await guild.unban(user=user)

@client.command()
async def timer(ctx, amt, opt = None):
  amt = int(amt)
  if opt[0].lower() == "m":
    amt = amt * 60
  elif opt == None:
    await ctx.send("Nothing provided, defaulting to seconds")
  elif opt[0].lower() == "h":
    amt = amt * 3600
  elif opt[0].lower() == "d":
    amt = amt * 86400
  await asyncio.sleep(amt)
  await ctx.send("Timer has ended!")

  #shcsuhcsuhcushcus


keep_alive()
client.run(os.getenv("TOKEN"))