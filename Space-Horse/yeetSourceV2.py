import random
import math
 

# class Mission:
    #def __init__(self, misName, minQual, maxQual):
        #self.misName = misName
        #self.minQual = minQual
        #self.maxQual = maxQual

    #def getMinQual(self):
        #return self.minQual

    #def getMaxQual(self):
        #return self.maxQual

# Mission List

# mis01 = Mission('Commercial Flight Altitude', 0, 4) # 0 launches
# mis02 = Mission('Stratosphere', 1, 6) # 25 "
# mis03 = Mission('Kármán line', 2, 8) # 50 "
# mis04 = Mission('Low Earth Orbit', 3, 10) # 100 "
# mis05 = Mission('Geostationary Orbit', 4, 12) # 250 "
# mis06 = Mission('High Earth Orbit', 5, 14) # 500 "
# mis07 = Mission('Lunar Orbit', 6, 16) # 1000 "
# mis08 = Mission('L2 Orbit', 7, 18) # 2500 "

# misHyper = Mission('Hyperspace', 14, 20) # Special

# missionlist = {
#     'Commercial Flight Altitude': {'minQual': 0, 'maxQual': 4},
#     'Stratosphere': {'minQual': 1, 'maxQual': 6},
#     'Kármán Line': {'minQual': 2, 'maxQual': 8},
#     'Low Earth Orbit': {'minQual': 3, 'maxQual': 10},
#     'Geostationary Orbit': {'minQual': 4, 'maxQual': 12},
#     'High Earth Orbit': {'minQual': 5, 'maxQual': 14},
#     'Lunar Orbit': {'minQual': 6, 'maxQual': 16},
#     'L2 Orbit': {'minQual': 7, 'maxQual': 18},
#     'Hyperspace': {'minQual': 14, 'maxQual': 20}
#     }


class Artifact:
    def __init__(self, artTier, artRare, artName, artSlots, artQuality, artChance):
        self.artTier = artTier
        self.artRare = artRare
        self.artName = artName
        self.artSlots = artSlots
        self.artQuality = artQuality
        self.artChance = artChance

    def artTitle(self):
        return "{} {} {}".format(self.artTier, self.artRare, self.artName)

# In generating odds, multiply by 10000 so that we get integers.
# Puzzle Cube
artifactDict = {

'artid01' : Artifact('T1', 'Common', 'Puzzle Cube', 0, 0.5, 0.900),
'artid02' : Artifact('T2', 'Common', 'Puzzle Cube', 0, 2.6, 0.900),
'artid03' : Artifact('T2', 'Epic', 'Puzzle Cube', 2, 2.6, 0.011),
'artid04' : Artifact('T3', 'Common', 'Puzzle Cube', 0, 6.8, 0.900),
'artid05' : Artifact('T3', 'Rare', 'Puzzle Cube', 1, 6.8, 0.090),
'artid06' : Artifact('T4', 'Common', 'Puzzle Cube', 0, 11.1, 0.720),
'artid07' : Artifact('T4', 'Rare', 'Puzzle Cube', 1, 11.1, 0.014),
'artid08' : Artifact('T4', 'Epic', 'Puzzle Cube', 2, 11.1, 0.004),
'artid09' : Artifact('T4', 'Legendary', 'Puzzle Cube', 3, 11.1, 0.0009),

# Lunar Totem

'artid10' : Artifact('T1', 'Common', 'Lunar Totem', 0, 0.7, 0.900),
'artid11' : Artifact('T2', 'Common', 'Lunar Totem', 0, 2.4, 0.900),
'artid12' : Artifact('T2', 'Rare', 'Lunar Totem', 1, 2.4, 0.030),
'artid13' : Artifact('T3', 'Common', 'Lunar Totem', 0, 5.2, 0.900),
'artid14' : Artifact('T3', 'Rare', 'Lunar Totem', 0, 5.2, 0.045),
'artid15' : Artifact('T4', 'Common', 'Lunar Totem', 0, 8.1, 0.900),
'artid16' : Artifact('T4', 'Rare', 'Lunar Totem', 1, 8.1, 0.030),
'artid17' : Artifact('T4', 'Epic', 'Lunar Totem', 2, 8.1, 0.004),

# Demeters Necklace

'artid18' : Artifact('T1', 'Common', 'Demeters Necklace', 0, 1.2, 0.900),
'artid19' : Artifact('T2', 'Common', 'Demeters Necklace', 0, 3.2, 0.900),
'artid20' : Artifact('T2', 'Rare', 'Demeters Necklace', 1, 3.2, 0.030),
'artid21' : Artifact('T3', 'Common', 'Demeters Necklace', 0, 5.8, 0.900),
'artid22' : Artifact('T3', 'Rare', 'Demeters Necklace', 1, 5.8, 0.045),
'artid23' : Artifact('T3', 'Epic', 'Demeters Necklace', 2, 5.8, 0.009),
'artid24' : Artifact('T4', 'Common', 'Demeters Necklace', 0, 8.9, 0.900),
'artid25' : Artifact('T4', 'Rare', 'Demeters Necklacee', 1, 8.9, 0.023),
'artid26' : Artifact('T4', 'Epic', 'Demeters Necklace', 2, 8.9, 0.006),
'artid27' : Artifact('T4', 'Legendary', 'Demeters Necklace', 3, 8.9, 0.0009),

# Vial of Martian Dust

'artid28' : Artifact('T1', 'Common', 'Vial of Martian Dust', 0, 1.75, 0.900),
'artid29' : Artifact('T2', 'Common', 'Vial of Martian Dust', 0, 4.8, 0.900),
'artid30' : Artifact('T2', 'Rare', 'Vial of Martian Dust', 1, 4.8, 0.090),
'artid31' : Artifact('T3', 'Common', 'Vial of Martian Dust', 0, 7.9, 0.090),
'artid32' : Artifact('T3', 'Epic', 'Vial of Martian Dust', 1, 7.9, 0.009),
'artid33' : Artifact('T4', 'Common', 'Vial of Martian Dust', 0, 12.5, 0.090),
'artid34' : Artifact('T4', 'Rare', 'Vial of Martian Dust', 1, 12.5, 0.023),
'artid35' : Artifact('T4', 'Legendary', 'Vial of Martian Dust', 2, 12.5, 0.0009),

# Aurelian Brooch

'artid36' : Artifact('T1', 'Common', 'Aurelian Brooch', 0, 1.9, 0.900),
'artid37' : Artifact('T2', 'Common', 'Aurelian Brooch', 0, 3.9, 0.900),
'artid38': Artifact('T3', 'Common', 'Aurelian Brooch', 0, 6.7, 0.900),
'artid39': Artifact('T3', 'Rare', 'Aurelian Brooch', 1, 6.7, 0.090),
'artid40' : Artifact('T3', 'Epic', 'Aurelian Brooch', 2, 6.7, 0.009),
'artid41' : Artifact('T4', 'Common', 'Aurelian Brooch', 0, 9.8, 0.900),
'artid42' : Artifact('T4', 'Rare', 'Aurelian Brooch', 0, 9.8, 0.023),
'artid43' : Artifact('T4', 'Epic', 'Aurelian Brooch', 0, 9.8, 0.005),
'artid44' : Artifact('T4', 'Legendary', 'Aurelian Brooch', 0, 9.8, 0.0009),

# Tungsten Ankh

'artid45' : Artifact('T1', 'Common', 'Tungsten Ankh', 0, 2, 0.900),
'artid46' : Artifact('T2', 'Common', 'Tungsten Ankh', 0, 5, 0.900),
'artid47' : Artifact('T2', 'Rare', 'Tungsten Ankh', 1, 5, 0.036),
'artid48' : Artifact('T3', 'Common', 'Tungsten Ankh', 0, 7.8, 0.900),
'artid49' : Artifact('T3', 'Rare', 'Tungsten Ankh', 1, 7.8, 0.090),
'artid50' : Artifact('T3', 'Legendary', 'Tungsten Ankh', 3, 7.8, 0.0009),
'artid51' : Artifact('T4', 'Common', 'Tungsten Ankh', 0, 11.7, 0.900),
'artid52' : Artifact('T4', 'Rare', 'Tungsten Ankh', 1, 11.7, 0.023),
'artid53' : Artifact('T4', 'Legendary', 'Tungsten Ankh', 3, 11.7, 0.0009),

# Gusset

'artid54' : Artifact('T1', 'Common', 'Gusset', 0, 2.5, 0.900),
'artid55' : Artifact('T2', 'Common', 'Gusset', 0, 5.3, 0.900),
'artid56' : Artifact('T2', 'Epic', 'Gusset', 2, 5.3, 0.009),
'artid57' : Artifact('T3', 'Common', 'Gusset', 0, 8.1, 0.900),
'artid58' : Artifact('T3', 'Rare', 'Gusset', 1, 8.1, 0.090),
'artid59' : Artifact('T4', 'Common', 'Gusset', 0, 13.1, 0.900),
'artid60' : Artifact('T4', 'Epic', 'Gusset', 2, 13.1, 0.006),
'artid61' : Artifact('T4', 'Legendary', 'Gusset', 3, 13.1, 0.0009),

# Neodymium Medallion

'artid62' : Artifact('T1', 'Common', 'Neodymium Medallion', 0, 3, 0.900),
'artid63' : Artifact('T2', 'Common', 'Neodymium Medallion', 0, 5, 0.900),
'artid64' : Artifact('T2', 'Rare', 'Neodymium Medallion', 1, 5, 0.075),
'artid65' : Artifact('T3', 'Common', 'Neodymium Medallion', 0, 7, 0.900),
'artid66' : Artifact('T3', 'Epic', 'Neodymium Medallion', 2, 7, 0.006),
'artid67' : Artifact('T4', 'Common', 'Neodymium Medallion', 0, 9.8, 0.900),
'artid68' : Artifact('T4', 'Rare', 'Neodymium Medallion', 1, 9.8, 0.023),
'artid69' : Artifact('T4', 'Epic', 'Neodymium Medallion', 2, 9.8, 0.005),
'artid70' : Artifact('T4', 'Legendary', 'Neodymium Medallion', 3, 9.8, 0.0009),

# Mercury's Lens

'artid71' : Artifact('T1', 'Common', "Mercury's Lens", 0, 3.3, 0.900),
'artid72' : Artifact('T2', 'Common', "Mercury's Lens", 0, 5.7, 0.900),
'artid73' : Artifact('T2', 'Rare', "Mercury's Lens", 1, 5.7, 0.090),
'artid74' : Artifact('T3', 'Common', "Mercury's Lens", 0, 8.2, 0.900),
'artid75' : Artifact('T3', 'Rare', "Mercury's Lens", 1, 8.2, 0.900),
'artid76' : Artifact('T4', 'Common', "Mercury's Lens", 0, 13.5, 0.450),
'artid77' : Artifact('T4', 'Rare', "Mercury's Lens", 1, 13.5, 0.011),
'artid78' : Artifact('T4', 'Epic', "Mercury's Lens", 2, 13.5, 0.002),
'artid79' : Artifact('T4', 'Legendary', "Mercury's Lens", 2, 13.5, 0.0005),

# Beak of Midas

'artid80' : Artifact('T1', 'Common', "Beak of Midas", 0, 3.5, 0.900),
'artid81' : Artifact('T2', 'Common', "Beak of Midas", 0, 5.5, 0.900),
'artid82' : Artifact('T3', 'Common', "Beak of Midas", 0, 7.7, 0.900),
'artid83' : Artifact('T3', 'Rare', "Beak of Midas", 1, 7.7, 0.082),
'artid84' : Artifact('T4', 'Common', "Beak of Midas", 0, 10.9, 0.900),
'artid85' : Artifact('T4', 'Rare', "Beak of Midas", 1, 10.9, 0.018),
'artid86' : Artifact('T4', 'Legendary', "Beak of Midas", 2, 10.9, 0.0006),

# Carved Rainstick

'artid87' : Artifact('T1', 'Common', "Carved Rainstick", 0, 4.2, 0.900),
'artid88' : Artifact('T2', 'Common', "Carved Rainstick", 0, 6.2, 0.900),
'artid89' : Artifact('T3', 'Common', "Carved Rainstick", 0, 8.8, 0.900),
'artid90' : Artifact('T4', 'Common', "Carved Rainstick", 0, 13.2, 0.900),
'artid91' : Artifact('T4', 'Epic', "Carved Rainstick", 1, 13.2, 0.0053),
'artid92' : Artifact('T4', 'Legendary', "Carved Rainstick", 2, 13.2, 0.0009),

# Interstellar Compass

'artid93' : Artifact('T1', 'Common', "Interstellar Compass", 0, 4.32, 0.900),
'artid94' : Artifact('T2', 'Common', "Interstellar Compass", 0, 6.1, 0.900),
'artid95' : Artifact('T3', 'Common', "Interstellar Compass", 0, 8.7, 0.900),
'artid96' : Artifact('T3', 'Rare', "Interstellar Compass", 1, 8.7, 0.090),
'artid97' : Artifact('T4', 'Common', "Interstellar Compass", 0, 12.5, 0.450),
'artid98' : Artifact('T4', 'Rare', "Interstellar Compass", 1, 12.5, 0.0113),
'artid99' : Artifact('T4', 'Epic', "Interstellar Compass", 2, 12.5, 0.0023),
'artid100' : Artifact('T4', 'Legendary', "Interstellar Compass", 3, 12.5, 0.0005),

# Chalice

'artid101' : Artifact('T1', 'Common', "Chalice", 0, 4.5, 0.900),
'artid102' : Artifact('T2', 'Common', "Chalice", 0, 6, 0.900),
'artid103' : Artifact('T2', 'Epic', "Chalice", 2, 6, 0.0113),
'artid104' : Artifact('T3', 'Common', "Chalice", 0, 8.2, 0.900),
'artid105' : Artifact('T3', 'Rare', "Chalice", 0, 8.2, 0.090),
'artid106' : Artifact('T3', 'Epic', "Chalice", 2, 8.2, 0.009),
'artid107' : Artifact('T4', 'Common', "Chalice", 0, 12.5, 0.900),
'artid108' : Artifact('T4', 'Epic', "Chalice", 2, 12.5, 0.006),
'artid109' : Artifact('T4', 'Legendary', "Chalice", 3, 12.5, 0.0009),

# Phoenix Feather

'artid110' : Artifact('T1', 'Common', "Phoenix Feather", 0, 5, 0.900),
'artid111' : Artifact('T2', 'Common', "Phoenix Feather", 0, 7, 0.900),
'artid112' : Artifact('T3', 'Common', "Phoenix Feather", 0, 9.4, 0.900),
'artid113' : Artifact('T3', 'Rare', "Phoenix Feather", 1, 9.4, 0.090),
'artid114' : Artifact('T4', 'Common', "Phoenix Feather", 0, 14.6, 0.900),
'artid115' : Artifact('T4', 'Rare', "Phoenix Feather", 1, 14.6, 0.0225),
'artid116' : Artifact('T4', 'Legendary', "Phoenix Feather", 2, 14.6, 0.0009),

# Quantum Metronome

'artid117' : Artifact('T1', 'Common', "Quantum Metronome", 0, 5.3, 0.900),
'artid118' : Artifact('T2', 'Common', "Quantum Metronome", 0, 7.2, 0.900),
'artid119' : Artifact('T2', 'Rare', "Quantum Metronome", 1, 7.2, 0.060),
'artid120' : Artifact('T3', 'Common', "Quantum Metronome", 0, 10.2, 0.900),
'artid121' : Artifact('T3', 'Rare', "Quantum Metronome", 1, 10.2, 0.090),
'artid122' : Artifact('T3', 'Epic', "Quantum Metronome", 2, 10.2, 0.0113),
'artid123' : Artifact('T4', 'Common', "Quantum Metronome", 0, 14.5, 0.630),
'artid124' : Artifact('T4', 'Rare', "Quantum Metronome", 1, 14.5, 0.0191),
'artid125' : Artifact('T4', 'Epic', "Quantum Metronome", 2, 14.5, 0.0039),
'artid126' : Artifact('T4', 'Legendary', "Quantum Metronome", 3, 14.5, 0.0006),

# Dilithium Monocle

'artid127' : Artifact('T1', 'Common', "Dilithium Monocle", 0, 5.45, 0.900),
'artid128' : Artifact('T2', 'Common', "Dilithium Monocle", 0, 7.75, 0.900),
'artid129' : Artifact('T3', 'Common', "Dilithium Monocle", 0, 10.7, 0.900),
'artid130' : Artifact('T4', 'Common', "Dilithium Monocle", 0, 15.2, 0.900),
'artid131' : Artifact('T4', 'Epic', "Dilithium Monocle", 2, 15.2, 0.006),
'artid132' : Artifact('T4', 'Legendary', "Dilithium Monocle", 3, 15.2, 0.0009),

# Titanium Actuator

'artid133' : Artifact('T1', 'Common', 'Titanium Actuator', 0, 5.5, 0.900),
'artid134' : Artifact('T2', 'Common', 'Titanium Actuator', 0, 7.9, 0.900),
'artid135' : Artifact('T3', 'Common', 'Titanium Actuator', 0, 11, 0.900),
'artid136' : Artifact('T3', 'Rare', 'Titanium Actuator', 1, 11, 0.090),
'artid137' : Artifact('T4', 'Common', 'Titanium Actuator', 0, 14.2, 0.900),
'artid138' : Artifact('T4', 'Epic', 'Titanium Actuator', 1, 14.2, 0.0045),
'artid139' : Artifact('T4', 'Legendary', 'Titanium Actuator', 2, 14.2, 0.0009),

# Ship in a Bottle

'artid140' : Artifact('T1', 'Common', "Ship in a Bottle", 0, 6.2, 0.900),
'artid141' : Artifact('T2', 'Common', "Ship in a Bottle", 0, 8.6, 0.900),
'artid142' : Artifact('T3', 'Common', "Ship in a Bottle", 0, 11.8, 0.900),
'artid143' : Artifact('T3', 'Rare', "Ship in a Bottle", 1, 11.8, 0.090),
'artid144' : Artifact('T4', 'Common', "Ship in a Bottle", 0, 15.2, 0.450),
'artid145' : Artifact('T4', 'Rare', "Ship in a Bottle", 1, 15.2, 0.0045),
'artid146' : Artifact('T4', 'Epic', "Ship in a Bottle", 2, 15.2, 0.0011),
'artid147' : Artifact('T4', 'Legendary', "Ship in a Bottle", 3, 15.2, 0.0004),

# Tachyon Deflector

'artid148' : Artifact('T1', 'Common', "Tachyon Deflector", 0, 7.25, 0.630),
'artid149' : Artifact('T2', 'Common', "Tachyon Deflector", 0, 9.25, 0.450),
'artid150' : Artifact('T3', 'Common', "Tachyon Deflector", 0, 13, 0.450),
'artid151' : Artifact('T3', 'Rare', "Tachyon Deflector", 1, 13, 0.045),
'artid152' : Artifact('T4', 'Common', "Tachyon Deflector", 0, 17, 0.090),
'artid153' : Artifact('T4', 'Rare', "Tachyon Deflector", 1, 17, 0.0008),
'artid154' : Artifact('T4', 'Epic', "Tachyon Deflector", 2, 17, 0.0002),
'artid155' : Artifact('T4', 'Legendary', "Tachyon Deflector", 3, 17, 0.0001), # Good luck getting this one.

# Book of Basan

'artid156' : Artifact('T1', 'Common', "Book of Basan", 0, 8, 0.900),
'artid157' : Artifact('T2', 'Common', "Book of Basan", 0, 10.3, 0.450),
'artid158' : Artifact('T3', 'Common', "Book of Basan", 0, 13.3, 0.270),
'artid159' : Artifact('T3', 'Epic', "Book of Basan", 1, 13.3, 0.0027),
'artid160' : Artifact('T4', 'Common', "Book of Basan", 0, 16.8, 0.180),
'artid161' : Artifact('T4', 'Epic', "Book of Basan", 1, 16.8, 0.0012),
'artid162' : Artifact('T4', 'Legendary', "Book of Basan", 2, 16.8, 0.0002),

# Light of Eggendil

'artid163' : Artifact('T1', 'Common', "Light of Eggendil", 0, 8.2, 0.900),
'artid164' : Artifact('T2', 'Common', "Light of Eggendil", 0, 10.2, 0.900),
'artid165' : Artifact('T2', 'Rare', "Light of Eggendil", 1, 10.2, 0.060),
'artid166' : Artifact('T3', 'Common', "Light of Eggendil", 0, 13.2, 0.900),
'artid167' : Artifact('T3', 'Rare', "Light of Eggendil", 1, 13.2, 0.090),
'artid168' : Artifact('T4', 'Common', "Light of Eggendil", 0, 16.1, 0.900),
'artid169' : Artifact('T4', 'Epic', "Light of Eggendil", 0, 16.1, 0.009),
'artid170' : Artifact('T4', 'Legendary', "Light of Eggendil", 0, 16.1, 0.0009),
}
def launch(currentMission):
  ######
  # Artifact generation

  ## Choosing Mission

  if currentMission == 'Commercial Flight Altitude':
    minQual = 0
    maxQual = 4
  if currentMission == 'Stratosphere':
    minQual = 1
    maxQual = 6
  if currentMission == 'Kármán Line':
    minQual = 2
    maxQual = 8
  if currentMission == 'Low Earth Orbit':
    minQual = 3
    maxQual = 10
  if currentMission == 'Geostationary Orbit':
    minQual = 4
    maxQual = 12
  if currentMission == 'High Earth Orbit':
    minQual = 5
    maxQual = 14
  if currentMission == 'Lunar Orbit':
    minQual = 6
    maxQual = 16
  if currentMission == 'L2 Orbit':
    minQual = 7
    maxQual = 18
  if currentMission == 'Hyperspace':
    minQual = 14
    maxQual = 20
  
  ## Collecting artifact pool (Determined by picking artifacts whose artQual)
  
  missionArtList = []

  for artifact in artifactDict.values():
    missionQual = round(random.uniform(minQual, maxQual), 2)
    if minQual <= artifact.artQuality <= missionQual:
      minArtQty = int(math.ceil(artifact.artChance * 1000))
      for i in range(minArtQty + 1):
        missionArtList.append(artifact.artTitle())
  
  chosenArt = random.choice(missionArtList)
  returnMessage = f"Congratulations! Horse returned with a **{chosenArt}**!" # Welcome back to earth, Horse.

  poolSize = len(missionArtList)

  returnObj = (returnMessage, missionQual, poolSize)

  return returnObj

def shinylaunch(currentMission):
  ######
  # Artifact generation

  ## Choosing Mission

  if currentMission == 'Commercial Flight Altitude':
    minQual = 0
    maxQual = 4
  if currentMission == 'Stratosphere':
    minQual = 1
    maxQual = 6
  if currentMission == 'Kármán Line':
    minQual = 2
    maxQual = 8
  if currentMission == 'Low Earth Orbit':
    minQual = 3
    maxQual = 10
  if currentMission == 'Geostationary Orbit':
    minQual = 4
    maxQual = 12
  if currentMission == 'High Earth Orbit':
    minQual = 5
    maxQual = 14
  if currentMission == 'Lunar Orbit':
    minQual = 6
    maxQual = 16
  if currentMission == 'L2 Orbit':
    minQual = 7
    maxQual = 18
  if currentMission == 'Hyperspace':
    minQual = 14
    maxQual = 20
  
  ## Collecting artifact pool (Determined by picking artifacts whose artQual)
  
  missionArtList = []

  for artifact in artifactDict.values():
    missionQual = round(random.uniform(minQual, maxQual), 2)
    if minQual <= artifact.artQuality <= missionQual:
      minArtQty = int(math.ceil(artifact.artChance * 1000))
      if artifact.artRare != "Common":
        for i in range(minArtQty + 1):
          missionArtList.append(artifact.artTitle())
  
  chosenArt = random.choice(missionArtList)
  returnMessage = f"Congratulations! Horse returned with a **{chosenArt}**!" # Welcome back to earth, Horse.

  poolSize = len(missionArtList)

  returnObj = (returnMessage, missionQual, poolSize)

  return returnObj
