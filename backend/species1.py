from interval import *
from scale import *
import random
import math

# Checks if the notes in the cantus firmus and counterpoint move in contrary motion
# @param cf1:str the base note of the cantus firmus
# @param cf2:str the note of the cantus firmus moved into
# @param counter1:str the base note of the counterpoint
# @param counter2:str the note of the counterpoint moved into
# @return True if the motion was in opposite directions
def checkContrary(cf1, cf2, counter1, counter2):
	cfup = isFirstNoteHigher(cf1, cf2)
	counterup = isFirstNoteHigher(counter1, counter2)
	return (cfup and not counterup) or (not cfup and counterup) # xor

# Checks the rules of first species counterpoint, requires cf and counter to have the same length
# @param cf:list<str> the cantus firmus, a list of notes
# @param counter:list<str> the counterpoint, a list of notes
# @return (boolean, list<str) True if all of the rules are followed, incidents
# 	where the rules are broken
def checkFirstSpeciesRules(cf, counter): # TODO, check for crossing
	errors = []
	verticalIntervals = []

	# check for crossing
	for i in range(len(cf)):
		if not isFirstNoteHigher(counter[i], cf[i]):
			errors.append("Crossing over of notes into CF at position " + str(i))

	# fill out the vertical intervals
	for i in range(len(cf)):
		verticalInterval = findInterval(cf[i], counter[i])
		verticalIntervals.append(verticalInterval)
		if verticalInterval in ["P4", "A4", "d5"] or verticalInterval[1] in ["2", "7"]:
			errors.append("Vertical Interval of " + verticalInterval + " between " + cf[i] + " and " + counter[i] + " at position " + str(i))

	# fill out the horizontal intervals
	for i in range(len(counter)-1):
		horizontalInterval = findInterval(counter[i], counter[i+1])
		if horizontalInterval in ["A4", "d5"] or horizontalInterval[1] == "7":
			errors.append("Horizontal Interval of " + horizontalInterval + " between " + counter[i] + " and " + counter[i+1] + " at position " + str(i))

	# check for direct/parallel intervals
	for i in range(len(counter)-1):
		contrary = checkContrary(cf[i], cf[i+1], counter[i], counter[i+1])
		if not contrary and ((verticalIntervals[i] == "P5" and verticalIntervals[i+1] == "P5") or 
		(verticalIntervals[i] == "P8" and verticalIntervals[i+1] == "P8") or 
		(verticalIntervals[i] == "P1" and verticalIntervals[i+1] == "P1")):
			errors.append("Parallel " + verticalIntervals[i+1][1] + "th at position " + str(i+1))
		elif not contrary and verticalIntervals[i+1] in ["P5", "P8"]:
			errors.append("Direct " + verticalIntervals[i+1][1] + "th at position " + str(i+1))

	# check start
	if not verticalIntervals[0] in ["M3", "P1", "P5", "P8"]:
		errors.append("Incorrect start of a " + verticalIntervals[0])

	# check end
	if not verticalIntervals[len(verticalIntervals)-1] in ["P1", "P8"]:
		errors.append("Incorrect ending of a " + verticalIntervals[len(verticalIntervals)-1])

	correct = len(errors) == 0
	return correct, errors

# Create a first species counterpoint by brute force (exponential worst case running time)
# @param cf:list<str> the cantus firmus, a list of notes, assumes key is based off of last note
# @param scale:str the type of scale to use
# @return (boolean, list<str) True if all of the rules are followed, incidents
# 	where the rules are broken
def bruteForceFirstSpecies(cf, scale_type="major"):
	scale = majorScale(cf[len(cf)-1]) # get possible notes that can be used
	possible = []
	# put notes an octave higher for less chance of crossing over
	for note in scale:
		possible.append(note[:-1] + str(int(note[-1]) + 1))

	goodHorizontalIntervals = ["m2", "M2", "m3", "M3", "P4", "P5", "m6", "M6", "P8"]
	goodVerticalIntervals = ["P1", "m3", "M3", "P5", "m6", "M6", "P8"]

	allPossible = recursiveAddFirstSpecies(cf, 0, [], possible)
	print allPossible

	# need helper function to recursively add notes
	return allPossible[int(math.floor(random.random()*len(allPossible)))+1]

def recursiveAddFirstSpecies(cf, cfInd, counter, possible):
	allTries = []
	# last call to it
	if cfInd == len(cf)-1:
		for note in possible:
			counterTry = counter + [note]
			if checkFirstSpeciesRules(counterTry, cf)[0]:
				allTries.append(counterTry)
		return allTries
	else:
		# recursively try all of them
		for note in possible:
			counterTry = counter + [note]
			allTries += recursiveAddFirstSpecies(cf, cfInd+1, counterTry, possible)
		return allTries



cf = ["C2", "D2", "E2", "A2", "F2", "E2", "F2", "D2", "D2", "C2"]


print bruteForceFirstSpecies(cf)

