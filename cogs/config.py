import discord
from discord.ext import commands
import json

async def switch(variable):
  if variable == True:
    variable = "On"
  else:
    variable = "Off"

async def spassive(ctx):
  import json
  with open("accounts.json", "r") as f:
    bals = json.load(f)
    sets = bals[str(ctx.author.id)]["Settings"]
    if sets["passive"] == True:
      await ctx.send("You cannot perform this action as this user is in passive mode")
      return

class Config(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def settings(self, ctx, operation = None):
    with open("accounts.json", "r") as f:
      sets = json.load(f)
      if "Settings" not in sets[str(ctx.author.id)]:
        await ctx.send("Your settings are being set to default, if you want to change them, type ?settings or ?settings update to change them well you **should** know this but you dont")
        sets[str(ctx.author.id)]["Settings"] = {"passive":False, "allow_trades":True}
        with open("accounts.json", "w") as f:
          json.dump(sets, f, indent=4)
      setconf = sets[str(ctx.author.id)]["Settings"]
      if operation == None:
        if setconf["passive"] == True and setconf["allow_trades"] == True:
          embed = discord.Embed(
            title="Current Settings",
            description="Currently using the Default Settings",
            colour=discord.Colour.blurple()
          )
        else:
          embed = discord.Embed(
            title="Current Settings",
            description="Not currently using the Default Settings",
            colour=discord.Colour.blurple()
          )
        spas = await switch(setconf["passive"])
        at = await switch(setconf["allow_trades"])
        embed.add_field(name=f"Passive Mode: {spas}", value="This means that you cannot rob or be robbed or have any other action taken against you, good or bad.", inline=True)
        embed.add_field(name=f"Allow Trades: {at}", value="This means that you cannot recieve trade requests from others", inline=True)
        await ctx.send(embed=embed)
      else:
        await ctx.send("The settings update feature is not ready yet")
        

def setup(client):
  client.add_cog(Config(client))