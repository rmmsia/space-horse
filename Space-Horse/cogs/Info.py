import discord
import random
from discord.ext import commands

class Info(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def ping(self, ctx):
    await ctx.channel.send(f"Pong! {round(self.bot.latency * 1000)} ms")

  @commands.command()
  async def botinfo(self, ctx):
    embed = discord.Embed(title="Space Horse", description = "I am a horse that collects Egg Inc. artifacts, one at a time!")
    embed.set_footer(text="Created by hybridlives#4282")
    await ctx.send(embed=embed)

  @commands.command()
  async def t4lbob(self, ctx):
    await ctx.channel.send("Lol")

  
  @commands.command(name="pet", aliases=["p"])
  async def pet(self, ctx):
    petResponse = ['Neigh!', 'Neigh...', 'Neigh.', 'Neigh neigh neigh!', 'Neigh :D', 'Stop.']
    await ctx.channel.send(random.choice(petResponse))
  
def setup(bot):
  bot.add_cog(Info(bot))