import discord
import yeetSourceV2
from pymongo import MongoClient
from discord.ext import commands

cluster = MongoClient("<connection string>")

horseyStats = cluster["shbot"]["stats"]

class shinyTicket(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.command(name = "shinyTicket", aliases = ["st"])
  async def shinyticket(self, ctx):
    id = ctx.message.author.id
    uStats = horseyStats.find_one({"id": id})
    currentTix = uStats["shiny tickets"]
    if currentTix == 0: # rejects attempt to shiny ticket
      newEmbed = discord.Embed(title="Uh oh...", description = "You need at least 1 shiny ticket to proceed!")
      await ctx.send(embed=newEmbed)

    else: # yeets Horsey for a shiny quest!
      currentMission = uStats["mission"]
      styReturn = yeetSourceV2.shinylaunch(currentMission) # returns a tuple of 3 items

      (launchresult, missionQual, poolSize) = styReturn # assigns the 3 items to variables
  
      # Set up the embed and update shiny stats
      if "Legendary" in launchresult:
        embed = discord.Embed(description = launchresult, color = 0xf1c40f)
        newLegCount = uStats["legendary"] + 1
        horseyStats.update_one({"id":id}, {"$set":{"legendary":newLegCount}})
      elif "Epic" in launchresult:
        embed = discord.Embed(description = launchresult, color = 0x9b59b6)
        newEpicCount = uStats["epic"] + 1
        horseyStats.update_one({"id":id}, {"$set":{"epic":newEpicCount}})
      elif "Rare" in launchresult:
        embed = discord.Embed(description = launchresult, color = 0x3498db)
        newRareCount = uStats["rare"] + 1
        horseyStats.update_one({"id":id}, {"$set":{"rare":newRareCount}})
      elif "Common" in launchresult:
        embed = discord.Embed(description = launchresult, color = 0xffffff)
      # Adds embed footer for pro stats (if on)
      if uStats["prostats"] == "true":
        embed.set_footer(text=f"Mission Quality: {missionQual}, Item Pool: {poolSize}")
      embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed) # Send the embed

      # Update "launches" count
      newLaunchCount = uStats["launches"] + 1
      horseyStats.update_one({"id":id}, {"$set":{"launches":newLaunchCount}})

      # Update "shiny tickets" count (decreasing as it's spent)
      newSTcount = uStats["shiny tickets"] - 1
      horseyStats.update_one({"id":id}, {"$set":{"shiny tickets":newSTcount}})

      # Update current mission
      if 0 <= newLaunchCount < 25:
        newMission = "Commercial Flight Altitude"
        horseyStats.update_one({"id":id}, {"$set":{"mission":newMission}})
      if 25 <= newLaunchCount < 50:
        newMission = "Stratosphere"
        horseyStats.update_one({"id":id}, {"$set":{"mission":newMission}})
      if 50 <= newLaunchCount < 100:
        newMission = "Kármán Line"
        horseyStats.update_one({"id":id}, {"$set":{"mission":newMission}})
      if 100 <= newLaunchCount < 250:
        newMission = "Low Earth Orbit"
        horseyStats.update_one({"id":id}, {"$set":{"mission":newMission}})
      if 250 <= newLaunchCount < 500:
        newMission = "Geostationary Orbit"
        horseyStats.update_one({"id":id}, {"$set":{"mission":newMission}})
      if 500 <= newLaunchCount < 1000:
        newMission = "High Earth Orbit"
        horseyStats.update_one({"id":id}, {"$set":{"mission":newMission}})
      if 1000 <= newLaunchCount < 2500:
        newMission = "Lunar Orbit"
        horseyStats.update_one({"id":id}, {"$set":{"mission":newMission}})
      if 2500 <= newLaunchCount:
        newMission = "L2 Orbit"
        horseyStats.update_one({"id":id}, {"$set":{"mission":newMission}})
      
      missionThe = ['Stratosphere', 'Kármán Line']

      if newMission != currentMission:
        if newMission not in missionThe: # Good English by removing 'the'
          embed=discord.Embed(title='Rank up!', description=f'You can now send Space Horse to {newMission}!')
          embed.set_footer(text='Look forward to better artifact drops!')
          await ctx.send(embed=embed)
        else:
          embed=discord.Embed(title='Rank up!', description=f'You can now send Space Horse to the {newMission}!')
          embed.set_footer(text='Look forward to better artifact drops!')
          await ctx.send(embed=embed)

  

def setup(bot):
  bot.add_cog(shinyTicket(bot))
    
