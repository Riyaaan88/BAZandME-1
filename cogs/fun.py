import discord
from discord.ext import commands
import asyncio
import random
import string

class Fun(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def hack(self, ctx, user : commands.MemberConverter = None):
    webs = ["gmail.com", "outlook.com", "mail.com", "hotmail.com"]
    passw = ["ilikepenis123", "imyourdaddywaddy", "password", "123"]
    m = await ctx.send(f"Beginning hack on {user.name}...")
    await asyncio.sleep(3)
    await m.edit(content="Recieving account login details...")
    await asyncio.sleep(4)
    email = f"{user.name}{random.randint(0, 10000)}@{random.choice(webs)}"
    pwd = random.choice(passw)
    await m.edit(content=f"Email: `{email}`\nPassword `{pwd}`")
    await asyncio.sleep(4)
    tok = ""
    for i in range(1, 100):
      tok = tok + random.choice(string.ascii_letters)
    await m.edit(content=f"Discord Token: {tok}")
    await asyncio.sleep()

  @commands.command()
  async def windows(self, ctx):
    wininit = await ctx.send("```\nMS-DOS Executive 7.06\n\nC:\\WIN98\\>winload.exe```")
    await asyncio.sleep(5)
    await wininit.edit(content="```\nMS-DOS Executive 7.06\n\nC:\\WIN98\\System32\\>winload.exe\n\nStarting Windows 98...```") # <:oldwin:919541654921281586>
    await asyncio.sleep(3)
    await wininit.edit(content="https://tenor.com/view/microsoft-windows98-bill-gates-windows98vaporwave-start-up-gif-14688825")
    await asyncio.sleep(7)
    await wininit.edit(content="https://tenor.com/view/bsod-gif-19406617")
    await asyncio.sleep(5)
    await wininit.edit(content="https://tenor.com/view/pc-computer-shutting-down-off-windows-computer-gif-17192330")
    await asyncio.sleep(10)
    await wininit.delete()
    await ctx.message.delete()

def setup(client):
  client.add_cog(Fun(client))