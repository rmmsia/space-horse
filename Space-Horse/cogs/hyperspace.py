# import discord
import yeetUtil
# import random
from pymongo import MongoClient
from discord.ext import commands

cluster = MongoClient(" ")

horseyStats = cluster["shbot"]["stats"]

class Hyperspace(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name = "hyperspace", aliases=["hs"])
  async def hyperspace(self, ctx):
    id = ctx.message.author.id
    uStats = horseyStats.find_one({"id": id})
    hsMode = uStats["hsmode"]
    hsEggs = uStats["hyperspace eggs"]
    uLaunches = uStats["launches"]

    # turns on hyperspace mode if true
    if hsMode == "false":
      if hsEggs == 0:
        await ctx.channel.send("You don't have enough **Hyperspace Eggs**!")
      else:
        horseyStats.update_one({"id":id}, {"$set":{"hsmode":"true", "mission":"Hyperspace"}})
        
        await ctx.channel.send("Horse is now entering **Hyperspace!**")
    if hsMode == "true":
      horseyStats.update_one({"id":id}, {"$set":{"hsmode":"false"}})

      normalMission = yeetUtil.returnHyperspace(uLaunches)

      horseyStats.update_one({"id":id}, {"$set":{"launches":uLaunches}})
      horseyStats.update_one({"id":id}, {"$set":{"mission":str(normalMission)}})

      await ctx.channel.send("Horse is exiting **Hyperspace**.")

def setup(bot):
  bot.add_cog(Hyperspace(bot))
