import discord
import yeetSourceV2
from pymongo import MongoClient
from discord.ext import commands

cluster = MongoClient("mongodb+srv://spacehorse:MzfF2JWiycVs2o@space-horse.sjxri.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

horseyStats = cluster[]

class Yeet(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # Stats
    @commands.command(name = "stats", aliases = ["s", "inv"])
    async def stats(self, ctx):
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        mission = users[str(id)]['mission']
        launches = users[str(id)]['launches']
        legendary = users[str(id)]['legendary']
        epic = users[str(id)]['epic']
        rare = users[str(id)]['rare']

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

    # Main Yeeting command
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(name = "yeet", aliases = ["y"])
    async def yeet(self, ctx):
        with open('users.json', 'r') as f:
            users = json.load(f)
            id = ctx.message.author.id
            await self.update_data(users, ctx.message.author)
            currentMission = users[f'{id}']['mission']

        
        launchresult = yeetSourceV2.launch(currentMission) # Yeets the horse. This function returns the "Congratulations! Horse returned with a" message.
        # print(launchresult)

        if "Legendary" in launchresult:
            embed = discord.Embed(description = launchresult, color = 0xf1c40f)
            users[f'{id}']['legendary'] += 1
        elif "Epic" in launchresult:
            embed = discord.Embed(description = launchresult, color = 0x9b59b6)
            users[f'{id}']['epic'] += 1
        elif "Rare" in launchresult:
            embed = discord.Embed(description = launchresult, color = 0x3498db)
            users[f'{id}']['rare'] += 1
        elif "Common" in launchresult:
            embed = discord.Embed(description = launchresult, color = 0xffffff)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


        # update data in users.json
        #await self.update_data(users, ctx.message.author)
        await self.add_launches(users, ctx.message.author, 1)

        # update current mission
        userLaunches = users[f'{id}']['launches']
        if 0 <= userLaunches < 25:
          newMission = users[f'{id}']['mission'] = 'Commercial Flight Altitude'
        if 25 <= userLaunches < 50:
          newMission = users[f'{id}']['mission'] = 'Stratosphere'
        if 50 <= userLaunches < 100:
          newMission = users[f'{id}']['mission'] = 'Kármán Line'
        if 100 <= userLaunches < 250:
          newMission = users[f'{id}']['mission'] = 'Low Earth Orbit'
        if 250 <= userLaunches < 500:
          newMission = users[f'{id}']['mission'] = 'Geostationary Orbit'
        if 500 <= userLaunches < 1000:
          newMission = users[f'{id}']['mission'] = 'High Earth Orbit'
        if 1000 <= userLaunches < 2500:
          newMission = users[f'{id}']['mission'] = 'Lunar Orbit'
        if 2500 <= userLaunches:
          newMission = users[f'{id}']['mission'] = 'L2 Orbit'

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
        
        
        


        with open('users.json', 'w') as f:
            json.dump(users, f)

# Stat tracker


    async def update_data(self, users, user):
        if not f'{user.id}' in users:
            users[f'{user.id}'] = {}
            users[f'{user.id}']['mission'] = "Commercial Flight Altitude"
            users[f'{user.id}']['launches'] = 0
            users[f'{user.id}']['legendary'] = 0
            users[f'{user.id}']['epic'] = 0
            users[f'{user.id}']['rare'] = 0

    async def add_launches(self, users, user, launch):
        users[f'{user.id}']['launches'] += launch
    


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
      if isinstance(error, commands.CommandOnCooldown):
        coolembed = discord.Embed(description=f'Horse is on cooldown. You can yeet again in **{round(error.retry_after, 1)}** seconds.')
        await ctx.send(embed=coolembed)
    




def setup(bot):
    bot.add_cog(Yeet(bot))
