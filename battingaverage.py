# Batting Average Calculator
# @auth: Brian Kittrell
# @date: 09/08/2021 

def average(atBat, totalHits):
    average = round((totalHits / atBat), 3)
    return average

print("===========================================================")
print("Baseball Team Manager\nThis program calculates the batting average for a player based\non the player's official number of at bats and hits.")
print("===========================================================")

playerName = input("Player's Name: ")
atBat = int(input("Official number of at bats: "))
totalHits = int(input("Number of hits: "))

print(playerName, "'s batting average is ", average(atBat, totalHits), sep='')

input("Press Any Key to Close")