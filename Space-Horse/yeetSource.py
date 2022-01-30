import random
import discord
from discord.ext import commands

# Yeet horse into space and have him return with an artifact
async def yeet(ctx):
    chosenArt = random.choice(var_list)

# Now that we (Horse) have (has) selected an artifact, now we need to determine the
# tier and rarity of said artifact. Each artifact has its own probabilities for tier
# and rarity, and they're included as methods in each artifact class.

    chosenArt.incTier() # Pray it's T4
    chosenArt.incRare() # Pray it's Legendary
    
    returnMessage = f"Congratulations! Horse returned with a **{chosenArt.artTitle()}**!" # Welcome back to earth, Horse.
    if "Legendary" in returnMessage:
        embed = discord.Embed(description = returnMessage, color = 0xf1c40f)
    elif "Epic" in returnMessage:
        embed = discord.Embed(description = returnMessage, color = 0x9b59b6)
    elif "Rare" in returnMessage:
        embed = discord.Embed(description = returnMessage, color = 0x3498db)
    elif "Common" in returnMessage:
        embed = discord.Embed(description = returnMessage, color = 0xffffff)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

# Now, the mess of SPACE HORSE.py. No clue how to get it to run by simply importing it from GitHub. Any help is appreciated.

class Artifact:

    def __init__(self, artName, artTier, artRare):
        self.artName = artName
        self.artTier = artTier
        self.artRare = artRare

    def artTitle(self):
        return "{} {} {}".format(self.artTier, self.artRare, self.artName)

# Each of the 21 artifacts is a subclass of the Artifact class.
# They each have their own methods for calculating rarity and tier.

# I'll admit that the blocks aren't pretty, but I can't think of any other way
# to give each artifact its own personalised R/E/L chance and tier probabilities.

# Hey, it beats V1 of SPACE HORSE that is more procedural compared to V2's object-oriented approach.
# That version offered me less control over individual artifacts' probabilities and is more painful to read.

# For the T4 artifacts that are normally craft-only, I simply made their drop rate exceedingly low (1%). Good luck!

class Cube(Artifact): # Puzzle Cube

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 985 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 890 < rareRoll <= 985:
                self.artRare = "Epic"
            elif 750 < rareRoll <= 890:
                self.artRare = "Rare"
            elif rareRoll <= 750:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 750 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 750:
                self.artRare = "Common"
        elif self.artTier == "T2":
            if 900 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif rareRoll <= 900:
                self.artRare = "Common"
        elif self.artTier == "T1":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 90:
            self.artTier = "T4"
        elif 65 < tierRoll <= 90:
            self.artTier = "T3"
        elif 30 < tierRoll <= 65:
            self.artTier = "T2"
        elif tierRoll <= 30:
            self.artTier = "T1"


class Totem(Artifact): # Lunar Totem

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 890 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif 750 < rareRoll <= 890:
                self.artRare = "Rare"
            elif rareRoll <= 750:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 750 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 750:
                self.artRare = "Common"
        elif self.artTier == "T2":
            if 750 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 750:
                self.artRare = "Common"
        elif self.artTier == "T1":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 90:
            self.artTier = "T4"
        elif 65 < tierRoll <= 90:
            self.artTier = "T3"
        elif 30 < tierRoll <= 65:
            self.artTier = "T2"
        elif tierRoll <= 30:
            self.artTier = "T1"


class DemetersNecklace(Artifact): # Demeters Necklace

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 970 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 900 < rareRoll <= 970:
                self.artRare = "Epic"
            elif 760 < rareRoll <= 900:
                self.artRare = "Rare"
            elif rareRoll <= 760:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 850 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif 700 < rareRoll <= 850:
                self.artRare = "Rare"
            elif rareRoll <= 700:
                self.artRare = "Common"
        elif self.artTier == "T2":
            if 800 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 800:
                self.artRare = "Common"
        elif self.artTier == "T1":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 90:
            self.artTier = "T4"
        elif 65 < tierRoll <= 90:
            self.artTier = "T3"
        elif 35 < tierRoll <= 65:
            self.artTier = "T2"
        elif tierRoll <= 35:
            self.artTier = "T1"


class Vial(Artifact): # Vial of Martian Dust

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 980 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 800 < rareRoll <= 980:
                self.artRare = "Rare"
            elif rareRoll <= 800:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 875 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif rareRoll <= 875:
                self.artRare = "Common"
        elif self.artTier == "T2":
            if 775 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 775:
                self.artRare = "Common"
        elif self.artTier == "T1":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 95:
            self.artTier = "T4"
        elif 70 < tierRoll <= 95:
            self.artTier = "T3"
        elif 35 < tierRoll <= 70:
            self.artTier = "T2"
        elif tierRoll <= 35:
            self.artTier = "T1"


class Brooch(Artifact): # Aurelian Brooch

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 975 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 900 < rareRoll <= 975:
                self.artRare = "Epic"
            elif 760 < rareRoll <= 900:
                self.artRare = "Rare"
            elif rareRoll <= 760:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 850 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif 700 < rareRoll <= 850:
                self.artRare = "Rare"
            elif rareRoll <= 700:
                self.artRare = "Common"
        elif self.artTier == "T1" or self.artTier == "T2":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 90:
            self.artTier = "T4"
        elif 65 < tierRoll <= 90:
            self.artTier = "T3"
        elif 35 < tierRoll <= 65:
            self.artTier = "T2"
        elif tierRoll <= 35:
            self.artTier = "T1"

class Ankh(Artifact): # Tungsten Ankh

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 980 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 800 < rareRoll <= 980:
                self.artRare = "Rare"
            elif rareRoll <= 800:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 965 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 700 < rareRoll <= 965:
                self.artRare = "Rare"
            elif rareRoll <= 700:
                self.artRare = "Common"
        elif self.artTier == "T2":
            if 800 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 800:
                self.artRare = "Common"
        elif self.artTier == "T1":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 90:
            self.artTier = "T4"
        elif 60 < tierRoll <= 90:
            self.artTier = "T3"
        elif 25 < tierRoll <= 60:
            self.artTier = "T2"
        elif tierRoll <= 25:
            self.artTier = "T1"

class Gusset(Artifact): # Gusset

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 985 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 880 < rareRoll <= 985:
                self.artRare = "Epic"
            elif rareRoll <= 880:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 750 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 750:
                self.artRare = "Common"
        elif self.artTier == "T2":
            if 800 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif rareRoll <= 800:
                self.artRare = "Common"
        elif self.artTier == "T1":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 93:
            self.artTier = "T4"
        elif 65 < tierRoll <= 93:
            self.artTier = "T3"
        elif 30 < tierRoll <= 65:
            self.artTier = "T2"
        elif tierRoll <= 30:
            self.artTier = "T1"

class Medallion(Artifact): # Neodymium Medallion

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 975 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 900 < rareRoll <= 975:
                self.artRare = "Epic"
            elif 760 < rareRoll <= 900:
                self.artRare = "Rare"
            elif rareRoll <= 760:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 850 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif rareRoll <= 850:
                self.artRare = "Common"
        elif self.artTier == "T2":
            if 750 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 750:
                self.artRare = "Common"
        elif self.artTier == "T1":
            self.artRare = "Common"


    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 90:
            self.artTier = "T4"
        elif 70 < tierRoll <= 90:
            self.artTier = "T3"
        elif 40 < tierRoll <= 70:
            self.artTier = "T2"
        elif tierRoll <= 40:
            self.artTier = "T1"

class Lens(Artifact): # Mercury's Lens

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 970 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 900 < rareRoll <= 970:
                self.artRare = "Epic"
            elif 760 < rareRoll <= 900:
                self.artRare = "Rare"
            elif rareRoll <= 760:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 850 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif 700 < rareRoll <= 850:
                self.artRare = "Rare"
            elif rareRoll <= 700:
                self.artRare = "Common"
        elif self.artTier == "T2":
            if 800 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 800:
                self.artRare = "Common"
        elif self.artTier == "T1":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 95:
            self.artTier = "T4"
        elif 65 < tierRoll <= 95:
            self.artTier = "T3"
        elif 30 < tierRoll <= 65:
            self.artTier = "T2"
        elif tierRoll <= 30:
            self.artTier = "T1"

class Beak(Artifact): # Beak of Midas

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 970 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 770 < rareRoll <= 970:
                self.artRare = "Rare"
            elif rareRoll <= 770:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 700 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 700:
                self.artRare = "Common"
        elif self.artTier == "T1" or self.artTier == "T2":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 90:
            self.artTier = "T4"
        elif 60 < tierRoll <= 90:
            self.artTier = "T3"
        elif 30 < tierRoll <= 60:
            self.artTier = "T2"
        elif tierRoll <= 30:
            self.artTier = "T1"

class Rainstick(Artifact): # Carved Rainstick

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 970 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 900 < rareRoll <= 970:
                self.artRare = "Epic"
            elif rareRoll <= 900:
                self.artRare = "Common"
        elif self.artTier == "T1" or self.artTier == "T2" or self.artTier == "T3":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 93:
            self.artTier = "T4"
        elif 70 < tierRoll <= 93:
            self.artTier = "T3"
        elif 40 < tierRoll <= 70:
            self.artTier = "T2"
        elif tierRoll <= 40:
            self.artTier = "T1"

class Compass(Artifact): # Interstellar Compass

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 980 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 920 < rareRoll <= 980:
                self.artRare = "Epic"
            elif 800 < rareRoll <= 920:
                self.artRare = "Rare"
            elif rareRoll <= 800:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 725 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 725:
                self.artRare = "Common"
        elif self.artTier == "T1" or self.artTier == "T2":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 93:
            self.artTier = "T4"
        elif 70 < tierRoll <= 93:
            self.artTier = "T3"
        elif 40 < tierRoll <= 70:
            self.artTier = "T2"
        elif tierRoll <= 40:
            self.artTier = "T1"

class Chalice(Artifact): # Chalice

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 980 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 920 < rareRoll <= 980:
                self.artRare = "Epic"
            elif rareRoll <= 920:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 850 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif 625 < rareRoll <= 850:
                self.artRare = "Rare"
            elif rareRoll <= 625:
                self.artRare = "Common"
        elif self.artTier == "T2":
            if 825 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif rareRoll <= 825:
                self.artRare = "Common"
        elif self.artTier == "T1":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 93:
            self.artTier = "T4"
        elif 75 < tierRoll <= 93:
            self.artTier = "T3"
        elif 35 < tierRoll <= 75:
            self.artTier = "T2"
        elif tierRoll <= 35:
            self.artTier = "T1"

class Feather(Artifact): # Phoenix Feather

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 980 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 800 < rareRoll <= 980:
                self.artRare = "Rare"
            elif rareRoll <= 800:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 750 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 750:
                self.artRare = "Common"
        elif self.artTier == "T1" or self.artTier == "T2":
            self.artRare = "Common"


    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 99:
            self.artTier = "T4"
        elif 75 < tierRoll <= 99:
            self.artTier = "T3"
        elif 40 < tierRoll <= 75:
            self.artTier = "T2"
        elif tierRoll <= 40:
            self.artTier = "T1"

class Metronome(Artifact): # Quantum Metronome

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 980 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 900 < rareRoll <= 980:
                self.artRare = "Epic"
            elif 770 < rareRoll <= 900:
                self.artRare = "Rare"
            elif rareRoll <= 770:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 885 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif 750 < rareRoll <= 885:
                self.artRare = "Rare"
            elif rareRoll <= 750:
                self.artRare = "Common"
        elif self.artTier == "T2":
            if 750 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 750:
                self.artRare = "Common"
        elif self.artTier == "T1":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 99:
            self.artTier = "T4"
        elif 75 < tierRoll <= 99:
            self.artTier = "T3"
        elif 40 < tierRoll <= 75:
            self.artTier = "T2"
        elif tierRoll <= 40:
            self.artTier = "T1"

class Monocle(Artifact): # Dilithium Monocle

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 980 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 900 < rareRoll <= 980:
                self.artRare = "Epic"
            elif rareRoll <= 900:
                self.artRare = "Common"
        elif self.artTier == "T1" or self.artTier == "T2" or self.artTier == "T3":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 99:
            self.artTier = "T4"
        elif 75 < tierRoll <= 99:
            self.artTier = "T3"
        elif 45 < tierRoll <= 75:
            self.artTier = "T2"
        elif tierRoll <= 45:
            self.artTier = "T1"

class XD(Artifact): # haha actuator bad

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 980 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 920 < rareRoll <= 980:
                self.artRare = "Epic"
            elif rareRoll <= 920:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 750 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 750:
                self.artRare = "Common"
        elif self.artTier == "T1" or self.artTier == "T2":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 99:
            self.artTier = "T4"
        elif 75 < tierRoll <= 99:
            self.artTier = "T3"
        elif 45 < tierRoll <= 75:
            self.artTier = "T2"
        elif tierRoll <= 45:
            self.artTier = "T1"

class SiaB(Artifact): # Ship in a Bottle

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 985 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 900 < rareRoll <= 985:
                self.artRare = "Epic"
            elif 775 < rareRoll <= 900:
                self.artRare = "Rare"
            elif rareRoll <= 775:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 825 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 825:
                self.artRare = "Common"
        elif self.artTier == "T1" or self.artTier == "T2":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 99:
            self.artTier = "T4"
        elif 75 < tierRoll <= 99:
            self.artTier = "T3"
        elif 45 < tierRoll <= 75:
            self.artTier = "T2"
        elif tierRoll <= 45:
            self.artTier = "T1"

class Deflector(Artifact): # Tachyon Deflector

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 985 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 900 < rareRoll <= 985:
                self.artRare = "Epic"
            elif 775 < rareRoll <= 900:
                self.artRare = "Rare"
            elif rareRoll <= 775:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 800 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 800:
                self.artRare = "Common"
        elif self.artTier == "T1" or self.artTier == "T2":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 99:
            self.artTier = "T4"
        elif 75 < tierRoll <= 99:
            self.artTier = "T3"
        elif 45 < tierRoll <= 75:
            self.artTier = "T2"
        elif tierRoll <= 45:
            self.artTier = "T1"

class Basan(Artifact): # Book of Basan

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 990 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 940 < rareRoll <= 990:
                self.artRare = "Epic"
            elif rareRoll <= 940:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 900 < rareRoll <= 1000:
                self.artRare = "Epic"
            elif rareRoll <= 900:
                self.artRare = "Common"
        elif self.artTier == "T1" or self.artTier == "T2":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 99:
            self.artTier = "T4"
        elif 85 < tierRoll <= 99:
            self.artTier = "T3"
        elif 60 < tierRoll <= 85:
            self.artTier = "T2"
        elif tierRoll <= 60:
            self.artTier = "T1"

class LoE(Artifact): # Light of Eggendil

    def incRare(self):
        rareRoll = random.randint(1, 1000)
        if self.artTier == "T4":
            if 990 < rareRoll <= 1000:
                self.artRare = "Legendary"
            elif 950 < rareRoll <= 990:
                self.artRare = "Epic"
            elif rareRoll <= 950:
                self.artRare = "Common"
        elif self.artTier == "T3":
            if 825 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 825:
                self.artRare = "Common"
        elif self.artTier == "T2":
            if 825 < rareRoll <= 1000:
                self.artRare = "Rare"
            elif rareRoll <= 825:
                self.artRare = "Common"
        elif self.artTier == "T1":
            self.artRare = "Common"

    def incTier(self):
        tierRoll = random.randint(1, 100)
        if tierRoll > 99:
            self.artTier = "T4"
        elif 75 < tierRoll <= 99:
            self.artTier = "T3"
        elif 45 < tierRoll <= 75:
            self.artTier = "T2"
        elif tierRoll <= 45:
            self.artTier = "T1"

# Variables for the artifacts and their corresponding classes

puzzleCube = Cube("Puzzle Cube", "T1", "Common")
lunarTotem = Totem("Lunar Totem", "T1", "Common")
demetersNecklace = DemetersNecklace("Demeters Necklace", "T1", "Common")
vialOfMartianDust = Vial("Vial of Martian Dust", "T1", "Common")
aurelianBrooch = Brooch("Aurelian Brooch", "T1", "Common")
tungstenAnkh = Ankh("Tungsten Ankh", "T1", "Common")
habGusset = Gusset("Gusset", "T1", "Common")

neoMedallion = Medallion("Neodymium Medallion", "T1", "Common")
mercuryLens = Lens("Mercury's Lens", "T1", "Common")
beakMidas = Beak("Beak of Midas", "T1", "Common")
carvedRainstick = Rainstick("Carved Rainstick", "T1", "Common")
interCompass = Compass("Interstellar Compass", "T1", "Common")
theChalice = Chalice("Chalice", "T1", "Common")
phoenixFeather = Feather("Phoenix Feather", "T1", "Common")

quantMetronome = Metronome("Quantum Metronome", "T1", "Common")
diliMonocle = Monocle("Dilithium Monocle", "T1", "Common")
actuator = XD("Titanium Actuator", "T1", "Common")
shipBottle = SiaB("Ship in a Bottle", "T1", "Common")
tachyonDeflector = Deflector("Tachyon Deflector", "T1", "Common")
bookofBasan = Basan("Book of Basan", "T1", "Common")
eggendil = LoE("Light of Eggendil", "T1", "Common")

# Randomise everything! Some variables appear less frequently than others, making them
# drop less often compared to others. I also don't know how to make this list any cleaner and more compact
# because random.choices() gives an output with square brackets and quotation marks
# and random.choice() doesn't let me use weights / probabilities.

# Eventually var_list contains 1000 objects. I divided the 21 artifacts into three distinct and neatly divisible levels.
# Higher levels mean they're rarer.

lv1arts = [puzzleCube, lunarTotem, demetersNecklace, vialOfMartianDust, aurelianBrooch, tungstenAnkh, habGusset] * 70
lv2arts = [neoMedallion, mercuryLens, beakMidas, carvedRainstick, interCompass, theChalice, phoenixFeather] * 50
lv3arts = [quantMetronome, diliMonocle, actuator, shipBottle, tachyonDeflector] * 25
specialArts = [bookofBasan, eggendil] * 17 + [bookofBasan] # 18 instances of BoB, 17 instances of LoE in a 1000-strong pool.

var_list = lv1arts + lv2arts + lv3arts + specialArts