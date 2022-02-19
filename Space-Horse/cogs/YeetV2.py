import discord
import random
import yeetSourceV2
import yeetUtil
from pymongo import MongoClient
from discord.ext import commands

cluster = MongoClient(" ")

horseyStats = cluster["shbot"]["stats"]

class YeetV2(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(name = "stats", aliases = ["s"])
  async def stats(self, ctx):
    id = ctx.message.author.id

    # Get user's stats from id
    uStats = horseyStats.find_one({"id": id})
    mission = uStats["mission"]
    launches = uStats["launches"]
    legendary = uStats["legendary"]
    epic = uStats["epic"]
    rare = uStats["rare"]

    embed = discord.Embed(title = f"Stats of {ctx.message.author.name}")
    embed.add_field(name="Mission", value=str(mission), inline = False)
    embed.add_field(name="Launches", value=str(launches), inline = False)
    embed.add_field(name="Legendary", value=str(legendary), inline = True)
    embed.add_field(name="Epic", value=str(epic), inline = True)
    embed.add_field(name="Rare", value=str(rare), inline = True)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    if launches > 1000 and legendary == 0:
        embed.set_footer(text=f'💩 {launches} launches, 0 Legendary 💩')
    await ctx.send(embed = embed)

  # Main yeeting command
  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.command(name = "yeet", aliases = ["y"])
  async def yeet(self, ctx):
    id = ctx.message.author.id
    uStats = horseyStats.find_one({"id": id})
    shinyMode = uStats["stmode"]
    if uStats is None: # creates new user stats for new user
      newuser = {
        "id": id,
        "mission": "Commercial Flight Altitude",
        "hyperspace eggs": 0,
        "shiny tickets": 0,
        "launches": 0,
        "legendary": 0,
        "epic": 0,
        "rare": 0,
        "prostats": "false",
        "hsmode": "false",
        "stmode": "false"
        }
      horseyStats.insert_one(newuser)
      newEmbed = discord.Embed(title=f"Hi {ctx.message.author.name}!", description = "Welcome to Space Horse! To start, yeet Space Horse with `!yeet`!")
      await ctx.send(embed=newEmbed)
      
    else: # yeets Horsey if user stats exist
      currentMission = uStats["mission"]
      if shinyMode == "true":
        # Update "shiny tickets" count (decreasing as it's spent)
        newSTcount = uStats["shiny tickets"] - 1
        horseyStats.update_one({"id":id}, {"$set":{"shiny tickets":newSTcount}})

        # Exit shiny mode if newSTcount falls to zero.
        if newSTcount == 0:
          horseyStats.update_one({"id":id}, {"$set":{"stmode":"false"}})
          await ctx.channel.send("You have run out of Shiny Tickets! Shiny Mode **OFF**.")
        
        # Shiny yeet!
        yeetReturn = yeetSourceV2.shinylaunch(currentMission)

      else: # If shiny mode is off, do a normal yeet.
        yeetReturn = yeetSourceV2.launch(currentMission) # Returns a tuple of 3 items

      (launchresult, missionQual, poolSize) = yeetReturn # assigns each item a variable
  
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

      # Generate a shiny ticket
      shinyRoll = random.randint(1, 100)
      if 1 <= shinyRoll <= 10:
        newSTcount = uStats["shiny tickets"] + 1
        horseyStats.update_one({"id":id}, {"$set":{"shiny tickets":newSTcount}})
        shinyEmbed = discord.Embed(description="Horse found a **Shiny Ticket**!")
        await ctx.send(embed=shinyEmbed)

      # Generate a hyperspace egg
      shinyRoll = random.randint(1, 100)
      if 1 <= shinyRoll <= 5:
        newHScount = uStats["hyperspace eggs"] + 1
        horseyStats.update_one({"id":id}, {"$set":{"hyperspace eggs":newHScount}})
        shinyEmbed = discord.Embed(description="Horse found a **Hyperspace Egg**!")
        await ctx.send(embed=shinyEmbed)

      # Deduct one hyperspace egg if hsmode is on.
      if uStats["hsmode"] == "true":
        hsEggs = uStats["hyperspace eggs"]
        uLaunches = uStats["launches"]
        newHScount = hsEggs - 1
        horseyStats.update_one({"id":id}, {"$set":{"hyperspace eggs":newHScount}})
        
      if newHScount == 0:
        horseyStats.update_one({"id":id}, {"$set":{"hsmode":"false"}})
  
        normalMission = yeetUtil.returnHyperspace(uLaunches)
  
        horseyStats.update_one({"id":id}, {"$set":{"launches":uLaunches}})
        horseyStats.update_one({"id":id}, {"$set":{"mission":str(normalMission)}})
        await ctx.channel.send("You have run out of Hyperspace Eggs! Exiting **Hyperspace**.")

      # Update current mission ONLY IF NOT IN HYPERSPACE
      if currentMission != "Hyperspace":
      
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

  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      coolembed = discord.Embed(description=f'Horse is on cooldown. You can yeet again in **{round(error.retry_after, 1)}** seconds.')
      await ctx.send(embed=coolembed)

def setup(bot):
  bot.add_cog(YeetV2(bot))
    
