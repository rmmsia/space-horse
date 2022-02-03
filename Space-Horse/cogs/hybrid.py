import discord
from pymongo import MongoClient
from discord.ext import commands

cluster = MongoClient("<connection string>")

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

def setup(bot):
  bot.add_cog(hybrid(bot))
