import discord
from discord.ext import commands
import random
import json

with open("config.json", "r") as f:
  c = json.load(f)
  cver = c["version"]

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

class Basic(commands.Cog):

  def __init__(self, client):
    self.client = client
  

  @commands.command(aliases=["h"])
  async def help(self, ctx):
    embedH = discord.Embed(
      title="Help",
      description=f"Invite Me: https://dsc.gg/scrappie\nJoin my support server: https://dsc.gg/scrappiesupport",
      colour=discord.Colour.blue()
    )
    for command in self.client.commands:
      embedH.add_field(name=command.name, value="{}\nAliases: {}".format(command.description, command.aliases))
    await ctx.send(embed=embedH)

  @commands.command(aliases=["latency"])
  async def ping(self, ctx):
    png = await ctx.send("Pinging...")
    await png.edit(content=f"**Pong!**\nYour ping is {round(self.client.latency * 1000)}!")

  @commands.command(aliases=["guilds"])
  async def servers(self, ctx):
    await ctx.send("I am in {} servers".format(len(self.client.guilds)))
  

  @commands.command()
  async def hug(self, ctx, member : discord.Member):
    await vibe_check(ctx, "uwu hug")
    if member is None:
      return await ctx.send("You need to tell me who you want to hug...")
    await ctx.send(f"{ctx.author.mention} hugged {member.mention}! 🤗")
    
  @commands.command()
  async def welcome(self,ctx, member : discord.Member):
    if member is None:
     return await ctx.send("tell me who to welcome so i can make their day")
    await ctx.send(f"{ctx.author.mention} welcome  {member.mention}! 🤗")

    @commands.command(aliases=["8ball","test","eight","ask"])
    async def _8ball(ctx, *,question):
     responses = ["yes","no","maybe","possibly","idk","could be true","only god can tell","have to keep this one hidden ofc"]
     await ctx.send(f"question: {question}\nAnswer: {random.choice(responses)}")


  @commands.command(aliases=["badges"])
  async def achievements(self, ctx, user:commands.MemberConverter):
    embed = discord.Embed(
      title=f"{user.name}'s Badges",
      colour=discord.Colour.blue()
    )
    embed.set_footer(text="Scrappie - Invest in the Future - Breadwinners and Baz")
    with open("badges.json", "r") as f:
      ach = json.load(f)
      if str(user.id) in ach:
        embed.add_field(name="Total number of badges", value=f"{len(ach[str(user.id)])}", inline=True)
        for badge in ach[str(user.id)]:
          embed.add_field(name=str(badge), value=None, inline=True)
      else:
        return "User has no badges"
    await ctx.send(embed=embed)

  @achievements.error
  async def userbadges(self, ctx, error):
    if isinstance(error, commands.MissingRequiblueArgument):
      embed = discord.Embed(
      title=f"{ctx.author.name}'s Badges",
      colour=discord.Colour.blue()
      )
      embed.set_footer(text="Scrappie - Invest in the Future - Breadwinners and Baz")
      with open("badges.json", "r") as f:
        ach = json.load(f)
        if str(ctx.author.id) in ach:
          embed.add_field(name="Total number of badges", value=f"{len(ach[str (ctx.author.id)])}", inline=True)
          for badge in ach[str(ctx.author.id)]:
            embed.add_field(name=str(badge), value=None, inline=True)
        else:
          return "User has no badges"
      await ctx.send(embed=embed)
  
    #roles = random.randint(1,100)
  
  @commands.command(aliases=["dice", "die"])
  async def diceroll(self, ctx): # here is your error  why self (s
    roles = random.randint(1, 6)
    await ctx.send(f":game_die: you rolled {roles} :game_die:")

  @commands.command()
  async def slap(self, ctx, member: discord.Member = None):
    await ctx.send(f"{ctx.author.mention} slapped {member.mention} OOF")

    # i have a dice roll

  @commands.command(aliases=["8ball","test","eight","ask"])
  async def _8ball(self, ctx, *,question):
     responses = ["yes","no","maybe","possibly","idk","could be true","only god can tell","have to keep this one hidden ofc"]
     await ctx.send(f"question: {question}\nAnswer: {random.choice(responses)}")

  @commands.command(aliases=["ver"])
  async def version(self, ctx):
    embed = discord.Embed(
      title=f"Current Version of Scrappie: {cver}",
      url="https://dsc.gg/scrappiesupport",
      colour=discord.Colour.blurple()
    )
    embed.add_field(name="What we added:", value="Nothing", inline=True)
    embed.add_field(name="What we removed:", value="Nothing", inline=True)
    await ctx.send(embed=embed)

    
def setup(client):
  client.add_cog(Basic(client))