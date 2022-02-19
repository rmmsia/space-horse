import discord
from pymongo import MongoClient
from discord.ext import commands

cluster = MongoClient(" ")

horseyStats = cluster["shbot"]["stats"]

class hybrid(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.is_owner()
  @commands.command(name = "givetix", aliases=["gt"])
  async def givetix(self, ctx, user: discord.User, qty): # Hybrid gives free Shiny Tix
    targetID = user.id
    uStats = horseyStats.find_one({"id":targetID})
    newTix = uStats["shiny tickets"] + int(qty)
    
    # Add tickets. Yay philanthropy!
    horseyStats.update_one({"id":targetID}, {"$set":{"shiny tickets":newTix}})
    await ctx.channel.send(f"Successfully given {int(qty)} Shiny Tickets to <@{targetID}>!")
  
  @commands.is_owner()
  @commands.command(name = "givehs", aliases=["ghs"])
  async def givehs(self, ctx, user: discord.User, qty): # Hybrid gives free Shiny Tix
    targetID = user.id
    uStats = horseyStats.find_one({"id":targetID})
    newHSE = uStats["hyperspace eggs"] + int(qty)
    
    # Add tickets. Yay philanthropy!
    horseyStats.update_one({"id":targetID}, {"$set":{"hyperspace eggs":newHSE}})
    await ctx.channel.send(f"Successfully given {int(qty)} Hyperspace Eggs to <@{targetID}>!")
  
  @commands.is_owner()
  @commands.command(name = "changemission", aliases=["cm"])
  async def changemission(self, ctx, loc_num):
    targetID = ctx.message.author.id
    locdict = {
      1 : {"mission": "Commercial Flight Altitude", "launches" : 1},
      2 : {"mission": "Stratosphere", "launches": 26},
      3 : {"mission": "Kármán Line", "launches": 51},
      4 : {"mission": "Low Earth Orbit", "launches": 101},
      5 : {"mission": "Geostationary Orbit", "launches": 251},
      6 : {"mission": "High Earth Orbit", "launches": 501},
      7 : {"mission": "Lunar Orbit", "launches": 1001},
      8 : {"mission": "L2 Orbit", "launches": 2501}
    }
    targetLoc = str(locdict[int(loc_num)]["mission"])
    newMisQty = int(locdict[int(loc_num)]["launches"])

    # Change location
    horseyStats.update_one({"id":targetID}, {"$set":{"mission":targetLoc, "launches":newMisQty}})
    await ctx.channel.send(f"Successfully changed mission to {targetLoc}.")
    


def setup(bot):
  bot.add_cog(hybrid(bot))
