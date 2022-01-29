import discord
from discord.ext import commands, tasks
import asyncio
from itertools import cycle
import os
import json
import random

async def bspace(ctx):
  with open("accounts.json", "r") as f:
    bals = json.load(f)
    if bals[str(ctx.author.id)]["Bank"] >= bals[str(ctx.author.id)]["bs"]:
      if bals[str(ctx.author.id)]["bs"] == 0:
        return
      else:
        await ctx.send("You bank account is full!")
        return

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

async def create_account(ctx):
  with open("accounts.json", "r") as f:
        bals = json.load(f)
        if str(ctx.author.id) not in bals:
          bals[str(ctx.author.id)] = {
          "Wallet":100,
          "Bank":0,
          "Inventory":{},
          "bs" : 1000
        }
        with open("accounts.json", "w") as f:
              await ctx.send(f"{ctx.author.mention}, your bank account has been opened!")
    
class Economy(commands.Cog):

  def __init__(self, client):
    self.client = client
    
  @commands.command(aliases=["bal"])
  async def balance(self, ctx, member : discord.Member = None):
    await vibe_check(ctx, "Let's be honest, you only looked at this cos ur probably in debt")
    if not member == None and not member == ctx.author:
      check_account = False
      ctx.author = member
    with open("accounts.json", "r") as f:
      bals = json.load(f)
      if str(ctx.author.id) not in bals:
        return await ctx.send("Sorry, but the member you specified is not in my database!")
      else:
        check_account = True
      
      with open("accounts.json", "r") as f:
        bals = json.load(f)
        if str(ctx.author.id) not in bals and check_account == True:
          bals[str(ctx.author.id)] = {
            "Wallet":100,
            "Bank":0,
            "Inventory":{}
          }
          with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
            await ctx.send(f"{ctx.author.mention}\nYour bank account has been opened!")
        else:
          embedBal = discord.Embed(
            title=f"{ctx.author.name}'s Balance",
            description="Wallet: ${0:,}\nBank: ${1:,}/{3:,}\nNet Worth: ${2:,}".format(bals[str(ctx.author.id)]["Wallet"], bals[str(ctx.author.id)]["Bank"], bals[str(ctx.author.id)]["Bank"] + bals[str(ctx.author.id)]["Wallet"], bals[str(ctx.author.id)]["bs"]),
            colour=discord.Colour.blue()
          )
          await ctx.send(embed=embedBal)

  @balance.error
  async def problem_xd(self, ctx, error):
    print(error)
    
  @commands.command(aliases=["w"])
  @commands.cooldown(1, 60, commands.BucketType.user) 
  async def work(self, ctx):
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
      
        else:
      
          amt = random.randint(500,800)
          after_work = bals[str(ctx.author.id)]["Wallet"] + amt
          bals[str(ctx.author.id)]["Wallet"] = after_work
          embed = discord.Embed(
            title="Work",
            description=f"For working, you recieved {amt}!",
            colour=discord.Colour.red()
          )
          await ctx.send(embed=embed)
          with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
         
  @commands.Cog.listener()
  async def on_command_error(self, ctx,error):
              
       if isinstance(error,commands.CommandOnCooldown):
        msg =f"wow, slow down, wait {error.retry_after:.0f} seconds, you idiot"
        await ctx.send(msg)
       
  @commands.command()
  @commands.cooldown(1, 86400, commands.BucketType.user)
  async def daily(self, ctx):
       await vibe_check(ctx, "In the words of Mr Krabs, `money`")
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
         

      
        else:
      
          amt = 10000
          after_work = bals[str(ctx.author.id)]["Wallet"] + amt
          bals[str(ctx.author.id)]["Wallet"] = after_work
          embed = discord.Embed(
            title="Daily Reward",
            description=f"For daily command, you recieved {amt}!",
            colour=discord.Colour.red()
          )
          await ctx.send(embed=embed)
          with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)


  @commands.command()  
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def beg(self,ctx):
      await vibe_check(ctx, "please sir, i want some more")
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
       
        else:

          amt = random.randint(0,120)
          searched = ["at your dads house","in the white house","on the street","in your car","under your sofa","MRBEaST howse","piggybannnnk"]
          after_work = bals[str(ctx.author.id)]["Wallet"] + amt
          bals[str(ctx.author.id)]["Wallet"] = after_work
          embed = discord.Embed(
            title="Beg",
            description = f"You begged {random.choice(searched)} and some idiot gave you {amt}",
          colour=discord.Colour.blue()
          )      
          await ctx.send(embed=embed)
          with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)
            

  @commands.command()
  async def buy(self, ctx, item = None, amount = 1):
      await vibe_check(ctx, "buying for the sake of buying, thats how i ended up here")
      if item == None:
        await ctx.send(f"{ctx.author.mention}\nHey you can't buy nothing unfortunately\nNow get out of my shop or buy a can of pepsi")
        return "404 Not found"
      if item == ctx.author:
        await ctx.send("mate you sure your ok? have u been buying beers? we might have to keep your keys mate its not safe")
        return "umm i dont think you can buy yourself"
      if type(item) == discord.Member:
       await ctx.send("umm i dont think you can buy this person hes not a slave lmao")
       return "lol thats a human being"
      with open("shop.json", "r") as f:
       dashop = json.load(f)
      if item not in dashop:
          for pro in dashop:
            if item in dashop[pro]["aliases"]:
              with open("accounts.json", "r") as f:
                acc = json.load(f)
                if acc[str(ctx.author.id)]["Wallet"] == 0:
                  await ctx.send("hey get a f*cking job and then i might be able to give it to you")
                  return "this guy is in debt real bad bro almost feel srry for u"
                price = amount * dashop[pro]["price"]
                if item in acc[str(ctx.author.id)]["Inventory"]:
                  if acc[str(ctx.author.id)]["Wallet"] < price:
                    await ctx.send("hey bro you need a lil more cash to buy dis")
                    return "poor"
                  acc[str(ctx.author.id)]["Wallet"] -= dashop[pro]["price"] * amount
                  acc[str(ctx.author.id)]["Inventory"][pro] += amount
                  await ctx.send(f"you bought {amount} {item}s for a bargain price of ${price}")
                else:
                  if acc[str(ctx.author.id)]["Wallet"] < price:
                    await ctx.send("hey bro you need a lil more cash to buy dis")
                    return "poor"
                  acc[str(ctx.author.id)]["Wallet"] -= dashop[pro]["price"] * amount
                  acc[str(ctx.author.id)]["Inventory"][pro] = amount
                  await ctx.send(f"you bought {amount} {pro}s for a bargain price of ${price}")
              with open("accounts.json", "w") as f:
                json.dump(acc, f, indent=4)
                return "used aliases"
          await ctx.send("hey how you going to buy that if it doesn't exist")
          return "404 Item not found"
      if item in dashop:
          with open("accounts.json", "r") as f:
            acc = json.load(f)
            if acc[str(ctx.author.id)]["Wallet"] == 0:
              await ctx.send("hey get a f*cking job and then i might be able to give it to you")
              return "this guy is in debt real bad bro almost feel srry for u"
            price = amount * dashop[item]["price"]
            if item in acc[str(ctx.author.id)]["Inventory"]:
              if acc[str(ctx.author.id)]["Wallet"] < price:
                await ctx.send("hey bro you need a lil more cash to buy dis")
                return "poor"
              acc[str(ctx.author.id)]["Wallet"] -= dashop[item]["price"] * amount
              acc[str(ctx.author.id)]["Inventory"][item] += amount
              await ctx.send(f"you bought {amount} {item}s for a bargain price of ${price}")
            else:
              if acc[str(ctx.author.id)]["Wallet"] < price:
                await ctx.send("hey bro you need a lil more cash to buy dis")
                return "poor"
              acc[str(ctx.author.id)]["Wallet"] -= dashop[item]["price"] * amount
              acc[str(ctx.author.id)]["Inventory"][item] = amount
              await ctx.send(f"you bought {amount} {item}s for a bargain price of ${price}")
      with open("accounts.json", "w") as f:
          json.dump(acc, f, indent=4)

  @commands.command()
  async def shop(self, ctx, *, item = None):
       with open("shop.json", "r") as f:
        shop = json.load(f)
        if item is None:
          em = discord.Embed(title = "Shop", colour=discord.Colour.blue())
          with open("shop.json", "r") as f:
            mainshop = json.load(f)
            for key in mainshop:
                emo = str(mainshop[key]["emoji"])
                desc = mainshop[key]["description"]
                pric = str(mainshop[key]["price"])
                if mainshop[key]["nfs"] == True:
                  continue
                  pric = "Not for Sale" 
                else:
                  pric = str(mainshop[key]["price"])
                emo = mainshop[key]["emoji"]
                em.add_field(name=f"{str(key)} | {str(emo)}", value=f"**Description:**\n{desc}\n**Price:**\n{pric}\n**Aliases:**\n{mainshop[key]['aliases']}", inline=True)
            await ctx.send(embed=em)
        elif item in shop:
              pric = shop[item]["price"]
              if shop[item]["nfs"] == True:
                pric = "Not for Sale"
              em = discord.Embed(
                title=str(item),
                colour=discord.Colour.blue()
              )
              em.add_field(name="Description:", value=str(shop[item]["description"]), inline=True)
              em.add_field(name="Appearance:", value=str(shop[item]["emoji"]), inline=True)
              em.add_field(name="Price:", value=str(pric), inline=True)
              em.add_field(name="Aliases:", value=f'{shop[item]["aliases"]}', inline=True)
              await ctx.send(embed=em)
        elif item not in shop:
          for pro in shop:
            if item in shop[pro]["aliases"]:
              pric = shop[pro]["price"]
              if shop[pro]["nfs"] == True:
                pric = "Not for Sale"
              em = discord.Embed(
                title=str(item),
                colour=discord.Colour.blue()
              )
              em.add_field(name="Description:", value=str(shop[pro]["description"]), inline=True)
              em.add_field(name="Appearance:", value=str(shop[pro]["emoji"]), inline=True)
              em.add_field(name="Price:", value=str(pric), inline=True)
              em.add_field(name="Aliases:", value=f'{shop[pro]["aliases"]}', inline=True)
              await ctx.send(embed=em)

  @commands.command(aliases=["inventory"])
  async def inv(self, ctx, user : commands.MemberConverter = None):
      if user == None:
        user = ctx.author
      with open("accounts.json", "r") as f:
       uac = json.load(f)
      if str(user.id) not in uac:
        await ctx.send("You do not have an account, please run a task command to setup your account\n e.g. ?beg")
        return
      embed=discord.Embed(
        title="{}'s Inventory".format(user.name), colour=discord.Colour.red()
      )
      for item in uac[str(user.id)]["Inventory"]:
        embed.add_field(name=f"Item: {item}", value=f"Amount: {uac[str(user.id)]['Inventory'][item]}", inline=True)
      await ctx.send(embed=embed)

  @commands.command(aliases=["deposit"])
  async def dep(self, ctx, money = 0):
      money = int(money)
      if money < 1:
       await ctx.send("hey you gotta at least deposit something lol u not gonna go to the bank to deposit nothing are you?")
       return "little pp amount"
      elif money > 0:
        await bspace(ctx)
        with open("accounts.json", "r") as f:
         bals = json.load(f)
        
         if str(ctx.author.id) not in bals:
           bals[str(ctx.author.id)] = {
          "Wallet":100,
          "Bank":0,
          "Inventory":{},
          "bs":1000
          }
           with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
              await ctx.send(f"{ctx.author.mention}\nYour bank account has been opened!")
         else:
          if money > bals[str(ctx.author.id)]["Wallet"]:
            await ctx.send("hey ur not mr beast now GET A F*CKING JOB")
          elif bals[str(ctx.author.id)]["Bank"] >= bals[str(ctx.author.id)]["bs"]:
            if bals[str(ctx.author.id)]["bs"] == 0:
              return
            return
          else:
            bals[str(ctx.author.id)]["Wallet"] -= money
            bals[str(ctx.author.id)]["Bank"] += money
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
              await ctx.send(f"{ctx.author.mention}, you successfully deposited {money}!")
      else:
        await vibe_check(ctx, "The fact that you got this makes you ultimate hecker")
        await ctx.send("STOP: SYSTEM_SERVICE_EXCEPTION\nAn unexpected error has occurred and Windows has been shutdown to prevent damage to your PC")

  @commands.command(aliases=["with"])
  async def withdraw(self, ctx, money = 0):
    money = int(money)
    if money < 0:
      await ctx.send("hey you gotta at least deposit something lol u not gonna go to the bank to deposit nothing are you?")
      return "little pp amount"
    elif money > 0:
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
        else:
          if money > bals[str(ctx.author.id)]["Bank"]:
            await ctx.send("hey ur not mr beast now GET A F*CKING JOB")
          else:
            bals[str(ctx.author.id)]["Wallet"] += money
            bals[str(ctx.author.id)]["Bank"] -= money
            with open("accounts.json", "w") as f:
              json.dump(bals, f, indent=4)
              await ctx.send(f"{ctx.author.mention}, you successfully withdrew {money}!")
    else:
      await vibe_check(ctx, "The fact that you got this makes you ultimate hecker")
      await ctx.send("STOP: SYSTEM_THREAD_EXCEPTION_NOT_HANDLED\nAn unexpected error has occurred and Windows has been shutdown to prevent damage to your PC this may result in a nyan cat virus")

  @commands.command(aliases=["find"])
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def search(self, ctx):
    places = ["in the bush", "up ur bum bum", "somewhere", "uhh imma keep this family friendly","your phone case","ma dad","krusty krab","home"]
    
    with open("accounts.json", "r")as f:
      bals = json.load(f)
      amt = random.randint(200,800)
      after_search = bals[str(ctx.author.id)]["Wallet"] + amt
      bals[str(ctx.author.id)]["Wallet"] = after_search
      embed = discord.Embed(
            title="Search",
            description = f"You searched {random.choice(places)} and you found {amt}",
          colour=discord.Colour.blue()
          )      
      await ctx.send(embed=embed)
    with open("accounts.json", "w") as f:
            json.dump(bals, f, indent=4)


  @commands.command()
  #@commands.cooldown(1, 30, commands.BucketType.user)
  async def rob(self, ctx, user:discord.Member = None):
    await vibe_check(ctx, "i wont tell anyone but you must be soo sick to annoy a 9 yr old that spends 2 hours a day grinding")
    if user == None:
      await ctx.send("hey try mentioning someone next time, at least then ill know who you want to rob")
      return "you cant rob nobody"
    if user == ctx.author:
      await ctx.send("you cant rob your self, now thats a bit silly isnt it if u rlly want someone to rob you ask me")
      return "im a dum dum"
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
        if str(user.id) not in bals or bals[str(user.id)]["Wallet"] < 1:
          await ctx.send("you shouldn't do this cos this person got none of dat cash")
          return
    await ctx.send("are you sure you want to do this, there is a 40% chance you get caught and lose money (y/N) - i think you should **risk it for the biscuit**")
    try:
      confirm = await self.client.wait_for("message", check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=20.0)
    except asyncio.TimeoutError:
      await ctx.send("It seems you have gone for some milk, so if you ever come back i will be waiting")
    else:
      if confirm.content[0].lower() == "y":
        pass
      elif confirm.content[0].lower() == "n":
        await ctx.send("ok you poopy head god i love bullying 9 year old kids")
        return
      else:
        await ctx.send("i dont understand what you mean me give 2 options man me naa do dis sh*t with you man")
        return
    chances = random.randint(1, 10)
    if chances <= 4:
      with open("accounts.json", "r") as f:
        acc = json.load(f)
        loss = random.randint(1, 1000000)
        if acc[str(ctx.author.id)]["Wallet"] <= loss:
          await ctx.send("you now bankrupt cos u forgor ur ninja suit i almost feel bad for you")
          await asyncio.sleep(2)
          await ctx.send("not really **poopy head** <:mlg:926864500454486107><:mlg:926864500454486107><:mlg:926864500454486107><:mlg:926864500454486107><:mlg:926864500454486107><:mlg:926864500454486107><:mlg:926864500454486107><:mlg:926864500454486107>")
          t = acc[str(ctx.author.id)]["Wallet"]
          loss = t
          acc[str(ctx.author.id)]["Wallet"] = 0
          acc[str(user.id)]["Wallet"] += loss
          with open("accounts.json", "w") as f:
            json.dump(acc, f, indent=4)
        else:
          await ctx.send(f"welp you got caught and lost ${loss}, do the crime pay the time i think thats how it goes")
          acc[str(ctx.author.id)]["Wallet"] -= loss
          acc[str(user.id)]["Wallet"] += loss
          with open("accounts.json", "w") as f:
            json.dump(acc, f, indent=4)
    elif chances > 4:
      with open("accounts.json", "r") as f:
        acc = json.load(f)
        loss = random.randint(1, 1000000)
        if acc[str(user.id)]["Wallet"] <= loss:
          await ctx.send(f"wow you actually got something, and luckily for you you robbed everything from {user}")
          t = acc[str(user.id)]["Wallet"]
          loss = t
          acc[str(user.id)]["Wallet"] = 0
          acc[str(ctx.author.id)]["Wallet"] += loss
          with open("accounts.json", "w") as f:
            json.dump(acc, f, indent=4)
        else:
          await ctx.send(f"wow you actually managed to rob ${loss} without getting caught")
          acc[str(ctx.author.id)]["Wallet"] += loss
          acc[str(user.id)]["Wallet"] -= loss
          with open("accounts.json", "w") as f:
            json.dump(acc, f, indent=4)
          # lol poopy head is the bots no 1 words now lmao lol
    else:
      await ctx.send("FATAL: \n01000001 01101110 00100000 01110101 01101110 01101011 01101110 01101111 01110111 01101110 00100000 01100101 01110010 01110010 01101111 01110010 00100000 01101111 01100011 01100011 01110101 01110010 01110010 01100101 01100100 00101100 00100000 01110000 01101100 01100101 01100001 01110011 01100101 00100000 01101010 01101111 01101001 01101110 00100000 01101101 01111001 00100000 01110011 01110101 01110000 01110000 01101111 01110010 01110100 00100000 01110011 01100101 01110010 01110110 01100101 01110010 00100000 01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01100100 01110011 01100011 00101110 01100111 01100111 00101111 01110011 01100011 01110010 01100001 01110000 01110000 01101001 01100101")
    
  @commands.command()
  async def sell(self, ctx, item=None, amount = 1):
    if item == None:
      await ctx.send(f"{ctx.author.mention}\nHey you can't sell nothing unfortunately, what did you expect you would get?")
      return "404 Not found"
    if item == ctx.author:
      await ctx.send("umm no")
      return "umm i dont think you can buy yourself"
    if type(item) == discord.Member:
      await ctx.send("umm i dont think you can buy this person hes not a slave lmao")
      return "lol thats a human being"
    with open("shop.json", "r") as f:
      dashop = json.load(f)
      if item not in dashop:
        for pro in dashop:
          if item in dashop[pro]["aliases"]:
            with open("accounts.json", "r") as f:
              acc = json.load(f)
              pr = dashop[pro]["price"] * 0.8
              price = amount * pr
              if item in acc[str(ctx.author.id)]["Inventory"]:
                acc[str(ctx.author.id)]["Wallet"] += price
                acc[str(ctx.author.id)]["Inventory"][pro] -= amount
                await ctx.send(f"you bought {amount} {item}s for a bargain price of ${price}")
              else:
                await ctx.send("You cant sell something you don't have")
                return
            with open("accounts.json", "w") as f:
              json.dump(acc, f, indent=4)
              return "used aliases"
        await ctx.send("hey how you going to sell that if it doesn't exist")
        return "404 Item not found"
      if item in dashop:
        with open("accounts.json", "r") as f:
          acc = json.load(f)
          price = amount * dashop[item]["price"]
          if item in acc[str(ctx.author.id)]["Inventory"]:
            acc[str(ctx.author.id)]["Wallet"] += dashop[item]["price"] * amount
            acc[str(ctx.author.id)]["Inventory"][item] -= amount
            await ctx.send(f"you sold {amount} {item}s for a bargain price of ${price}")
          else:
            await ctx.send("You can't sell something you don't have")
        with open("accounts.json", "w") as f:
          json.dump(acc, f, indent=4)
          
          wisk = [821790584829902879]


  @commands.command(aliases=["lawbreak"])
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def crime(self, ctx):
   places = ["robbed a bank","lit a house on fire","killed a bounty","did drugs YUM","lied to the police","scammed someone on the phone","hacked an indian","didnt vote for @theimposter come on man what u thinking"]
  #wisk = [821790584829902879]
  
   with open("accounts.json", "r")as f:
     bals = json.load(f)
     cbt = random.randint(1200,1500)
     after_crime = bals[str(ctx.author.id)]["Wallet"] + cbt
     bals[str(ctx.author.id)]["Wallet"] = after_crime
     #if ctx.author.id in wisk:
      # after_crime = bals[str(ctx.author.id)]["Wallet"] + 100000

     embed = discord.Embed(
           title="crime!",
           description = f"You {random.choice(places)} and you found and earnt {cbt}",
         colour=discord.Colour.blue()
         )     
     await ctx.send(embed=embed)
   with open("accounts.json", "w") as f:
           json.dump(bals, f, indent=4)

def setup(client):
    client.add_cog(Economy(client))