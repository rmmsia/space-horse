import discord
from pymongo import MongoClient
#from discord.ext import commands

cluster = MongoClient("mongodb+srv://spacehorse:MzfF2JWiycVs2o@space-horse.sjxri.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

horseyStats = cluster["shbot"]["stats"]

class Mission:
  def __init__(self, name, minMissions, minQual, maxQual, hsStatus):
    self.name = name
    self.minMissions = minMissions

mis01 = Mission("Commercial Space Flight", 0, 0, 4, "false")
mis02 = Mission("Stratosphere", 25, 1, 6, "false")
mis03 = Mission("Stratosphere", 50, 2, 8, "false")
mis04 = Mission("Kármán Line", 100, 3, 10, "false")
mis05 = Mission("Low Earth Orbit", 250, 4, 12, "false")
mis06 = Mission("Geostationary Orbit", 500, 5, 14, "false")
mis07 = Mission("Lunar Orbit", 1000, 6, 16, "false")
mis08 = Mission("L2 Orbit", 2500, 7, 18, "false")

mis99 = Mission("Hyperspace", 0, 14, 20, "true")

missionList = [mis01, mis02, mis03, mis04, mis05, mis06, mis07, mis08, mis99]

def updateMission(newLaunchCount, currentMission): # Updates mission based on launch count, if not in Hyperspace
  if currentMission != "Hyperspace":
    if 0 <= newLaunchCount < 25:
      newMission = "Commercial Flight Altitude"
      
    if 25 <= newLaunchCount < 50:
      newMission = "Stratosphere"
      
    if 50 <= newLaunchCount < 100:
      newMission = "Kármán Line"
      
    if 100 <= newLaunchCount < 250:
      newMission = "Low Earth Orbit"
      
    if 250 <= newLaunchCount < 500:
      newMission = "Geostationary Orbit"
      
    if 500 <= newLaunchCount < 1000:
      newMission = "High Earth Orbit"
      
    if 1000 <= newLaunchCount < 2500:
      newMission = "Lunar Orbit"
      
    if 2500 <= newLaunchCount:
      newMission = "L2 Orbit"
  
  else:
    newMission = "Hyperspace"
  
  return newMission

def returnHyperspace(launches):
  if 0 <= launches < 25:
    newMission = "Commercial Flight Altitude"
    
  if 25 <= launches < 50:
    newMission = "Stratosphere"
    
  if 50 <= launches < 100:
    newMission = "Kármán Line"
    
  if 100 <= launches < 250:
    newMission = "Low Earth Orbit"
    
  if 250 <= launches < 500:
    newMission = "Geostationary Orbit"
    
  if 500 <= launches < 1000:
    newMission = "High Earth Orbit"
    
  if 1000 <= launches < 2500:
    newMission = "Lunar Orbit"
    
  if 2500 <= launches:
    newMission = "L2 Orbit"

  return newMission


