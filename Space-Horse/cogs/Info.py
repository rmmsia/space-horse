import discord
import random
from pymongo import MongoClient
from discord.ext import commands

cluster = MongoClient("mongodb+srv://spacehorse:MzfF2JWiycVs2o@space-horse.sjxri.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

horseyStats = cluster["shbot"]["stats"]

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
  
  @commands.command(name="inventory", aliases=["b", "i", "inv"])
  async def bag(self, ctx):
    id = ctx.message.author.id
    uStats = horseyStats.find_one({"id": id})
    tix = uStats["shiny tickets"]
    hseggs = uStats["hyperspace eggs"] 

    embed = discord.Embed(title = f"Special items of {ctx.message.author.name}")
    embed.add_field(name="Shiny Tickets", value=str(tix), inline = True)
    embed.add_field(name="Hyperspace Eggs", value=str(hseggs), inline = True)
    await ctx.send(embed = embed)
  
  @commands.command(name="prostats", aliases=["ps"])
  async def prostats(self, ctx):
    id = ctx.message.author.id
    uStats = horseyStats.find_one({"id": id})
    psMode = uStats["prostats"]

    # turns on prostats if true
    if psMode == "false":
      horseyStats.update_one({"id":id}, {"$set":{"prostats":"true"}})
      await ctx.channel.send("Pro stats mode turned **ON**")
    if psMode == "true":
      horseyStats.update_one({"id":id}, {"$set":{"prostats":"false"}})
      await ctx.channel.send("Pro stats mode turned **OFF**")
    


    
  
def setup(bot):
  bot.add_cog(Info(bot))