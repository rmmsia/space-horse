import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

client = discord.Client()
bot = commands.Bot(command_prefix="!")

# Startup things...
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="$yeet"))
  print("Space Horse Online. {0.user}".format(bot))

# Cog loading
initial_extensions = []

for filename in os.listdir("./cogs"): # Look through files in cogs folder, then add to initial_extensions list if ending with .py
  if filename.endswith('.py'):
    initial_extensions.append("cogs." + filename[:-3]) # Take out .py so it'll work.

if __name__ == '__main__':
  for extension in initial_extensions:
    bot.load_extension(extension)



keep_alive()
bot.run(os.environ["TOKEN"])