import discord
import json
import os
from discord.ext import commands



class Info(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
  
  @commands.command()
  async def ping(self, ctx):
    await ctx.channel.send(f"Pong!")

  @commands.command()
  async def botinfo(self, ctx):
    embed = discord.Embed(title="Space Horse", description = "I am a horse that collects Egg Inc. artifacts, one at a time!")
    embed.set_footer(text="Created by hybridlives#4282")
    await ctx.send(embed=embed)

  @commands.command()
  async def t4lbob(self, ctx):
    await ctx.channel.send("Lol")

  


def setup(bot):
  bot.add_cog(Info(bot))