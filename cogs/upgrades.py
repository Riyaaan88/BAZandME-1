import discord 
from discord.ext import commands
import json
import asyncio
import random

class Upgrade(commands.Cog):

  def __init__(self, client):

    self.client = client

  @commands.command()
  async def use(self, ctx, item = None):
    if item is None:
      await ctx.send("you need to provide an item")
      return
    with open("accounts.json", "r") as f:
      bals = json.load(f)
      if item.lower() == "note" or item.lower() == "bank":
        if "note" in bals[str(ctx.author.id)]["Inventory"]: 
          if bals[str(ctx.author.id)]["Inventory"]["note"] < 1:
            await ctx.send("You don't have enough notes to do this!")
            return
          await ctx.send(f"You have {bals[str(ctx.author.id)]['Inventory']['note']}  notes, how many do you want to use?")
          try:
            confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
          except asyncio.TimeoutError:
            await ctx.send(f"I don't know where you went, so looks like you're not going to pull a  cracker")
            
          else:
            if confirm.content.lower() == "cancel":
              await ctx.send("Cancelled!")
              return
            else:
              amt = int(confirm.content)
          if amt == 1:
            i = random.randint(1000, 50000)
            bef = bals[str(ctx.author.id)]["bs"] + i
            bals[str(ctx.author.id)]["bs"] = bef
            if (bals[str(ctx.author.id)]["Inventory"]["note"] - 1) == 0:
              bals[str(ctx.author.id)]["Inventory"].pop("note")
            else:
              bals[str(ctx.author.id)]["Inventory"]["note"] -= amt
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
              await ctx.send(f"You used {amt} notes and got an extra {i} in space!")
            if bals[str(ctx.author.id)]["Inventory"]["note"]:
              bals[str(ctx.author.id)]["Inventory"]["note"].pop()
              with open("accounts.json", "w") as f:
                json.dump(bals, f, indent=4)
                return
            return
          else:
            tot = 0
            for n in range(1, amt):
              i = random.randint(1000, 50000)
              bef = bals[str(ctx.author.id)]["bs"] + i
              bals[str(ctx.author.id)]["bs"] = bef
              tot += i 
              with open("accounts.json", "w") as f:
                json.dump(bals, f, indent=4)
            if (bals[str(ctx.author.id)]["Inventory"]["note"] - int(amt)) == 0:
              bals[str(ctx.author.id)]["Inventory"].pop("note")
            else:
              bals[str(ctx.author.id)]["Inventory"]["note"] -= amt
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
            await ctx.send(f"You used {amt} notes and got an extra {tot} in space!")
            return
          

def setup(client):
  client.add_cog(Upgrade(client))