import discord
import random
import json
import asyncio
from discord.ext import commands
import os

emos = ["💰", "💸", "🤑", "<:diamond:909092430958186577>", "🔷", "💀"]

ph = "🍆"

adm = [730043363671277638, 821790584829902879]

class Gambling(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["gamble"])
  async def slots(self, ctx):
    if ctx.author.id in adm:
      emos = ["<:diamond:909092430958186577>"]
      ph = "💸"
    if ctx.author.id not in adm:
      emos = ["💰", "💸", "🤑", "<:diamond:909092430958186577>", "🔷", "💀"]
      ph = "🍆"
    await ctx.send(f"{ctx.author.mention}, how many beans do you want to put down?")
    try:
      gambled = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
    except asyncio.TimeoutError:
      await ctx.send("Ok, maybe we can try this another time")
      return
    else:
      if gambled.content.lower() == "cancel":
        await ctx.send("Ok, I will cancel the requested action")
        return
      else:
        try:
          gamb = int(gambled.content)
        except Exception:
          await ctx.send("You need to provide a number")
          return
        with open("accounts.json", "r") as f:
          bals = json.load(f)
          if str(ctx.author.id) not in bals:
            bals[str(ctx.author.id)] = {
              "Wallet":100,
              "Bank":0,
              "Inventory":{}
            }
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
              await ctx.send(f"{ctx.author.mention}\nYour bank account has been opened!")
        if gamb > bals[str(ctx.author.id)]["Wallet"]:
              await ctx.send("You do not have enough money to gamble this much!")
              return
        await ctx.send(f"You put down ${gambled.content}, so let's play slots!")
        with open("accounts.json", "r") as f:
          bals = json.load(f)
          after_Wallet = bals[str(ctx.author.id)]["Wallet"] - gamb
          bals[str(ctx.author.id)]["Wallet"] = after_Wallet
          with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
        await asyncio.sleep(5)
    b1 = random.choice(emos)
    b2 = random.choice(emos)
    b3 = random.choice(emos)
    embed = discord.Embed(
      title="Slots",
      description=f"[ {ph} ][ {ph} ][ {ph} ]",
      colour=discord.Colour.red()
    )
    e = await ctx.send(embed=embed)
    for i in range(1, 5):
      await asyncio.sleep(0.1)
      embed1 = discord.Embed(
        title="Slots",
        description=f"[ {random.choice(emos)} ][ {ph} ][ {ph} ]",
        colour=discord.Colour.red()
      )
      await e.edit(embed=embed1)
    embed1 = discord.Embed(
        title="Slots",
        description=f"[ {b1} ][ {ph} ][ {ph} ]",
        colour=discord.Colour.red()
      )
    await e.edit(embed=embed1)
    for i in range(1, 5):
      await asyncio.sleep(0.1)
      embed1 = discord.Embed(
        title="Slots",
        description=f"[ {b1} ][ {random.choice(emos)} ][ {ph} ]",
        colour=discord.Colour.red()
      )
      await e.edit(embed=embed1)
    embed1 = discord.Embed(
        title="Slots",
        description=f"[ {b1} ][ {b2} ][ {ph} ]",
        colour=discord.Colour.red()
      )
    await e.edit(embed=embed1)
    for i in range(1, 5):
      await asyncio.sleep(0.1)
      embed1 = discord.Embed(
        title="Slots",
        description=f"[ {b1} ][ {b2} ][ {random.choice(emos)} ]",
        colour=discord.Colour.red()
      )
      await e.edit(embed=embed1)
    embed1 = discord.Embed(
        title="Slots",
        description=f"[ {b1} ][ {b2} ][ {b3} ]",
        colour=discord.Colour.red()
      )
    await e.edit(embed=embed1)
    if b1 == "💀":
      if b2 == "💀":
        if b3 == "💀":
          with open("accounts.json", "r") as f:
            bals = json.load(f)
            await ctx.send(f"You lost ${gamb}! ah m8 sorry for that")
            res = gamb
            after_Wallet = bals[str(ctx.author.id)]["Wallet"] - res
            bals[str(ctx.author.id)]["Wallet"] = after_Wallet
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            return
    if b1 == "💸":
      if b2 == "💸":
        if b3 == "💸":
          with open("accounts.json", "r") as f:
            res = gamb * 2
            bals = json.load(f)
            after_Wallet = bals[str(ctx.author.id)]["Wallet"] + res
            bals[str(ctx.author.id)]["Wallet"] = after_Wallet
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send(f"You got ${res} from gambling!")
            return
    if b1 == "💰":
      if b2 == "💰":
        if b3 == "💰":
          with open("accounts.json", "r") as f:
            bals = json.load(f)
            if gamb >= 10000000000:
              res = gamb + 10000000000
            else:
              res = 10000000000
            after_Wallet = bals[str(ctx.author.id)]["Wallet"] + res
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send(f"You recieved ${res} from gambling!")
            return
    if b1 == "🤑":
      if b2 == "🤑":
        if b3 == "🤑":
          with open("accounts.json", "r") as f:
            bals = json.load(f)
            if gamb >= 10000000000:
              res = gamb + 10000000000
            else:
              res = 10000000000
            after_Wallet = bals[str(ctx.author.id)]["Wallet"] + res
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send(f"You recieved ${res} from gambling!")
            return
    if b1 == "<:diamond:909092430958186577>":
      if b2 == "<:diamond:909092430958186577>":
        if b3 == "<:diamond:909092430958186577>":
          with open("accounts.json", "r") as f:
            res = gamb * 7
            bals = json.load(f)
            after_Wallet = bals[str(ctx.author.id)]["Wallet"] + res
            bals[str(ctx.author.id)]["Wallet"] = after_Wallet
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send(f"You got ${res} from gambling!")
            return
    if b1 == "🔷":
      if b2 == "🔷":
        if b3 == "🔷":
          with open("accounts.json", "r") as f:
            res = gamb * 2
            bals = json.load(f)
            after_Wallet = bals[str(ctx.author.id)]["Wallet"] + res
            bals[str(ctx.author.id)]["Wallet"] = after_Wallet
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
              await ctx.send(f"You got ${res} from gambling!")
              return
    await ctx.send("You did not win anything")

def setup(client):
  client.add_cog(Gambling(client))