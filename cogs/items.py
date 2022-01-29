import discord
from discord.ext import commands
import json
import random

rewards = ["nothing","nothing","gold","nothing","DIAMONDS","nothing","creeper AWW MAAN", "breadwinners GCSE'S","nothing"]

fished = ["mummy fish","daddy fish", "mummy fish","daddy fish", "legendary fish","nothing","nothing","nothing", "nothing","nothing","nothing","nothing","nothing","mummy fish","daddy fish", "mythic gold fish","meedas flooper","meedas flooper","meedas flooper", "wopper"]


#adm = [730043363671277638, 821790584829902879]

adm = []


async def vibe_check(ctx, badge):
  with open("badges.json", "r") as  f:
    ach = json.load(f)
    if str(ctx.author.id) in ach:
      if badge in ach[str(ctx.author.id)]:
        return
      else: 
        ach[str(ctx.author.id)].append(badge)
        await ctx.author.send("You have unlocked the badge [{}]".format(badge))
    elif str(ctx.author.id) not in ach:
      ach[str(ctx.author.id)] = []
  with open("badges.json", "w") as f:
    json.dump(ach, f, indent=4)

class Items(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def fish(self, ctx):
    if ctx.author.id in adm:
      fished = ["mummy fish","daddy fish", "mummy fish","daddy fish", "legendary fish","mummy fish","daddy fish", "mythic gold fish","meedas flooper","meedas flooper","meedas flooper"]
    if ctx.author.id not in adm:
      fished = ["mummy fish","daddy fish", "mummy fish","daddy fish", "legendary fish","nothing","nothing","nothing", "nothing","nothing","nothing","nothing","nothing","mummy fish","daddy fish", "mythic gold fish","meedas flooper","meedas flooper","meedas flooper", "wopper"]
    with open("accounts.json", "r") as f:
      invs = json.load(f)
      if "fishing rod" in invs[str(ctx.author.id)]["Inventory"] or "fishing" in invs[str(ctx.author.id)]["Inventory"] or "rod" in invs[str(ctx.author.id)]["Inventory"]:
        perk = random.choice(fished)
        if perk == "nothing":
          await ctx.send("just like i what i got from my totally existant,rich dad, you got nothing **your dad needs to take you fishing**")
          return "father, what am i?"
        elif perk == "mummy fish":
          await ctx.send("wow you caught a mummy fish!")
          with open("accounts.json", "r") as f:
            dafish = json.load(f)
            if perk not in dafish[str(ctx.author.id)]["Inventory"][perk]:
              dafish[str(ctx.author.id)]["Inventory"][perk] = 1
            else:
              dafish[str(ctx.author.id)]["Inventory"][perk] += 1 
          with open("accounts.json", "w") as f:
            json.dump(dafish, f, indent=4)
            return "mummy fish"
        elif perk == "daddy fish":
          await ctx.send("wow you caught a daddy fish!")
          with open("accounts.json", "r") as f:
            dafish = json.load(f)
            if perk not in dafish[str(ctx.author.id)]["Inventory"][perk]:
              dafish[str(ctx.author.id)]["Inventory"][perk] = 1
            else:
              dafish[str(ctx.author.id)]["Inventory"][perk] += 1
          with open("accounts.json", "w") as f:
            json.dump(dafish, f, indent=4)
            return "daddy fish"
        elif perk == "legendary fish":
          await ctx.send("wow you caught a legendary fish! now this is something to show to da bois")
          with open("accounts.json", "r") as f:
            dafish = json.load(f)
            if perk not in dafish[str(ctx.author.id)]["Inventory"][perk]:
              dafish[str(ctx.author.id)]["Inventory"][perk] = 1
            else:
              dafish[str(ctx.author.id)]["Inventory"][perk] += 1
          with open("accounts.json", "w") as f:
            json.dump(dafish, f, indent=4)
            return "leg fish"
        elif perk == "mythic gold fish":
          await ctx.send("you caught a mythic gold fish! isnt that the thing from fardnite?")
          with open("accounts.json", "r") as f:
            dafish = json.load(f)
            if perk not in dafish[str(ctx.author.id)]["Inventory"][perk]:
              dafish[str(ctx.author.id)]["Inventory"][perk] = 1
            else:
              dafish[str(ctx.author.id)]["Inventory"][perk] += 1
          with open("accounts.json", "w") as f:
            json.dump(dafish, f, indent=4)
            return "fortnut fish"
        elif perk == "meedas flooper":
          await ctx.send("you caught a meedas fish! isnt that the thing from fardnite?")
          with open("accounts.json", "r") as f:
            dafish = json.load(f)
            if perk not in dafish[str(ctx.author.id)]["Inventory"][perk]:
              dafish[str(ctx.author.id)]["Inventory"][perk] = 1
            else:
              dafish[str(ctx.author.id)]["Inventory"][perk] += 1
          with open("accounts.json", "w") as f:
            json.dump(dafish, f, indent=4)
            return "fortnut fish 2"
        elif perk == "wopper":
          await ctx.send("you got a bite, but it was a really big fishy - tiko perhaps - and broke ur rod :smirk:")
          if "fishing rod" not in invs[str(ctx.author.id)]["Inventory"]:
            return

          elif invs[str(ctx.author.id)]["Inventory"]["fishing rod"] > 1:
            invs[str(ctx.author.id)]["Inventory"]["fishing rod"] -= 1
          else:
            invs[str(ctx.author.id)]["Inventory"].pop("fishing rod")
          with open("accounts.json", "w") as f:
            json.dump(invs, f, indent=4)
            return
        else:
          await ctx.send("Problem with item: ",perk)
          return "umm"
      else:
        await ctx.send("hey you gotta buy a fishing rod to use this command are u gonna go jump in the river and use ur hands")
        return "how you gonna do dat? you people make me laugh lmao"




  @commands.command()
  async def dig(self, ctx):
    if ctx.author.id in adm:
      rewards = ["gold","DIAMONDS", "breadwinners GCSE'S"]
    if ctx.author.id not in adm:
      rewards = ["nothing","nothing","gold","nothing","DIAMONDS","nothing","creeper AWW MAAN", "breadwinners GCSE'S","nothing"]
    await vibe_check(ctx, "DIGGIN BABY")
    with open("accounts.json", "r") as f:
      invs = json.load(f)
      if "shovel" in invs[str(ctx.author.id)]["Inventory"]:
        gold = random.choice(rewards)
        if gold == "nothing":
          await ctx.send(f"not ur day today m8")
          return
        if gold == "breadwinners GCSE'S":
          await ctx.send("OMG U FOUND A DEVS GCSES OMG DONT READ THEM THO....")
          if "breadwinner's GCSE'S" not in invs[str(ctx.author.id)]["Inventory"]:
            invs[str(ctx.author.id)]["Inventory"]["breadwinner's GCSE'S"] = 1
          else:
            invs[str(ctx.author.id)]["Inventory"]["breadwinner's GCSE'S"] += 1
          with open("accounts.json", "w") as f:
            json.dump(invs, f, indent=4)
            return
        if gold == "gold":
          await ctx.send("nice you found gold now trade with piglins for pearls")
          if "gold" not in invs[str(ctx.author.id)]["Inventory"]:
            invs[str(ctx.author.id)]["Inventory"]["gold"] = 1
          else:
            invs[str(ctx.author.id)]["Inventory"]["gold"] += 1
          with open("accounts.json", "w") as f:
            json.dump(invs, f, indent=4)
            return
        if gold == " :diamond: DIAMONDS":
          await ctx.send("wow you found diamonds well done!!")
          if "diamond" not in invs[str(ctx.author.id)]["Inventory"]:
            invs[str(ctx.author.id)]["Inventory"]["diamond"] = 1
          else:
            invs[str(ctx.author.id)]["Inventory"]["diamond"] += 1
          with open("accounts.json", "w") as f:
            json.dump(invs, f, indent=4)
            return
        if gold == "creeper AWW MAAN":
          await ctx.send("oh dear you blew up along with your shovel AWWWW man")
          if "shovel" not in invs[str(ctx.author.id)]["Inventory"]:
            return

          elif invs[str(ctx.author.id)]["Inventory"]["shovel"] > 1:
            invs[str(ctx.author.id)]["Inventory"]["shovel"] -= 1
          else:
            invs[str(ctx.author.id)]["Inventory"].pop("shovel")
          with open("accounts.json", "w") as f:
            json.dump(invs, f, indent=4)
            return
        else:
          await ctx.send("Problem with item: ",gold)
          return print("error")
      else:
       await ctx.send("You need a shovel to dig")


def setup(client):
  client.add_cog(Items(client))