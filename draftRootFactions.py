import random
import sys
from itertools import combinations

factionReach = {
	"Marquise de Cat": 10,
	"Underground Duchy": 8,
	"Eyrie Dynasties": 7,
	"Vagabond": 5,
	"Riverfolk Company": 5,
	"Woodland Alliance": 3,
	"Corvid Conspiracy": 3,
	"Second Vagabond": 2,
	"Lizard Cult": 2
}

reachRequirement = [-1, -1, 17, 18, 21, 25, 28]

if len(sys.argv) != 2:
	print("Usage: python draftRootFactions.py [number of players]")
	exit()

players = int(sys.argv[1])

if players < 2 or players > 6:
	print("Only 2-6 players supported.")
	exit()

print("First player picks the map.")
print("Second player picks the deck.")
print("Draft in reverse order.")
print("Each player after the first draws successive additional cards.")
print("After setup, each player discards down to 3 cards and shuffles the remainder back into the deck.")

#will be unnecessary once more high-reach factions are released
if players == 2:
	print("Factions:")
	print(random.choice([["Marquise de Cat", "Underground Duchy"], ["Marquise de Cat", "Eyrie Dynasties"]]))
	exit()

legalCombination = False

finalFactions = []
finalReach = 0

#generate a faction for each player plus one
#ensure that all combinations of draft picks are legal
while not legalCombination:
	factions = [
		"Marquise de Cat",
		"Underground Duchy",
		"Eyrie Dynasties",
		"Vagabond",
		"Riverfolk Company",
		"Woodland Alliance",
		"Corvid Conspiracy",
		"Lizard Cult"
	]
	chosenFactions = []

	for i in range(0, players+1):
		choice = random.choice(factions)
		chosenFactions.append(choice)
		factions.remove(choice)
		if choice == "Vagabond":
			factions.append("Second Vagabond")
	validChoices = True

	allCombinations = list(combinations(chosenFactions, players))
	random.shuffle(allCombinations)
	
	for combination in allCombinations:
		if "Second Vagabond" in combination and "Vagabond" not in combination:
			continue
		reach = 0
		for faction in combination:
			reach = reach + factionReach[faction]
		if(reach < reachRequirement[players]):
			validChoices = False
			break
	if validChoices:
		legalCombination = True
		finalFactions = chosenFactions
		finalReach = reach

finalFactions.sort(key=lambda x: factionReach[x], reverse=True)

print("Factions (one will be leftover):")
print(str(finalFactions))
print("Reach requirement: " + str(reachRequirement[players]))