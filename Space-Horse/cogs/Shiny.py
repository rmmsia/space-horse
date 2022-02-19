# import discord
import yeetUtil
# import random
from pymongo import MongoClient
from discord.ext import commands

cluster = MongoClient(" ")

horseyStats = cluster["shbot"]["stats"]

class Shiny(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name = "shiny mode", aliases=["st"])
  async def shinymode(self, ctx):
    id = ctx.message.author.id
    uStats = horseyStats.find_one({"id": id})
    stMode = uStats["stmode"]
    stix = uStats["shiny tickets"]

    # turns on shiny mode if true
    if stMode == "false":
      if stix == 0:
        await ctx.channel.send("You don't have enough **Shiny Tickets**!")
      else:
        horseyStats.update_one({"id":id}, {"$set":{"stmode":"true"}})
        
        await ctx.channel.send("Shiny Mode **ON**.")
    if stMode == "true":
      horseyStats.update_one({"id":id}, {"$set":{"stmode":"false"}})

      await ctx.channel.send("Shiny Mode **OFF**.")

def setup(bot):
  bot.add_cog(Shiny(bot))
