import discord
import yeetSource
import json
import os
from discord.ext import commands

os.chdir("./cogs")

class Yeet(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # Stats
    @commands.command()
    async def stats(self, ctx):
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        launches = users[str(id)]['launches']
        legendary = users[str(id)]['legendary']
        epic = users[str(id)]['epic']
        rare = users[str(id)]['rare']

        embed = discord.Embed(title = f"Stats of {ctx.message.author.name}")
        embed.add_field(name="Launches", value=str(launches), inline = False)
        embed.add_field(name="Legendary", value=str(legendary), inline = True)
        embed.add_field(name="Epic", value=str(epic), inline = True)
        embed.add_field(name="Rare", value=str(rare), inline = True)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        if launches > 500 and legendary == 0:
            embed.set_footer(text=f'💩 {launches} launches, 0 Legendary 💩')
        await ctx.send(embed = embed)

    # Main Yeeting command
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(name = "yeet", aliases = ["y"])
    async def yeet(self, ctx):
        with open('users.json', 'r') as f:
            users = json.load(f)

        launchresult = yeetSource.launch() # Yeets the horse. This function returns the "Congratulations! Horse returned with a" message.
        # print(launchresult)

        if "Legendary" in launchresult:
            embed = discord.Embed(description = launchresult, color = 0xf1c40f)
            users[f'{ctx.message.author.id}']['legendary'] += 1
        elif "Epic" in launchresult:
            embed = discord.Embed(description = launchresult, color = 0x9b59b6)
            users[f'{ctx.message.author.id}']['epic'] += 1
        elif "Rare" in launchresult:
            embed = discord.Embed(description = launchresult, color = 0x3498db)
            users[f'{ctx.message.author.id}']['rare'] += 1
        elif "Common" in launchresult:
            embed = discord.Embed(description = launchresult, color = 0xffffff)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


        await self.update_data(users, ctx.message.author)
        await self.add_launches(users, ctx.message.author, 1)

        with open('users.json', 'w') as f:
            json.dump(users, f)

# Stat tracker


    async def update_data(self, users, user):
        if not f'{user.id}' in users:
            users[f'{user.id}'] = {}
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
