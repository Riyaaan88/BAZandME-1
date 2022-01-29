import discord
from discord.ext import commands
import json
import time

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

async def is_admin(ctx):
  with open("admins.json", "r") as f:
    admins = json.load(f)
    if str(ctx.author.id) in admins:
      return True
    else:
      await ctx.send("hey kid you aren't special enough to be mod :sunglasses:")
      return False

class Admin(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.command(aliases=["clear", "delete"])
  async def purge(self, ctx, amount=1):
    if amount == None:
      await ctx.send("input a value")
      bb = await ctx.channel.purge(amount=amount)
      await ctx.send(f"{amount} messages have been purged by {ctx.author.mention}")
      time.sleep(2)
      await ctx.messages.delete()

  @commands.command()
  async def ban(self, ctx,member:discord.Member,*,reason=None):
    if not ctx.author.guild_permissions.administrator:
      await ctx.send("listen kid if u hate the person that much just report him ur not admin dont even think about it")
      return "403 Forbidden"
    if  ctx.author.guild_permissions.administrator:
      if reason is None:
        reason = "no reason specified"
      await vibe_check(ctx, "The power of the ban hammer compells you!")
      await member.ban()
      await ctx.send(f"{member.mention} was banned for `{reason}` cya later {member.mention}")

  @commands.command()
  async def give(self, ctx, money, user : discord.Member = None):
    if not await is_admin(ctx):
      return False
    money = int(money)
    if user is None:
      user = ctx.author
    if money == 0:
      await ctx.send("You have to give someone something")
      return "scrooge mcduck from ducktales"
    with open("accounts.json", "r") as f:
      acc = json.load(f)
      acc[str(user.id)]["Wallet"] += money
      await ctx.send(f"{user.mention} has been given {money}!")
    with open("accounts.json" , "w") as f:
      json.dump(acc, f, indent=4)
    
  @commands.command()
  async def remove(self, ctx, money = 1000, user : discord.Member = None):
    if not await is_admin(ctx):
      return False
    money = int(money)
    if money == 0:
      await ctx.send("hey you gotta take away something")
      return "scrooge mcduck from ducktales"
    with open("accounts.json", "r") as f:
      acc = json.load(f)
      acc[str(user.id)]["Wallet"] -= money
      await ctx.send(f"{user.mention} has lost {money}!")
    with open("accounts.json" , "w") as f:
      json.dump(acc, f, indent=4)

''''
@commands.command()
async def unban(self, ctx,user: discord.User):
  guild = ctx.guild
  embed = discord.Embed(
    title = "SCORE!",
    description = f"{user} was unbanned OK!"
  )
  if ctx.author.guild_permissions.ban_members:
    await ctx.send(embed=embed)
    await guild.unban(user=user) 
  '''

  
def setup(client):
  client.add_cog(Admin(client))