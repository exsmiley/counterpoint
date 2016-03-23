from interval import *
from scale import *

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
def checkFirstSpeciesRules(cf, counter):
	errors = []
	verticalIntervals = []

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

	correct = len(errors) == 0
	return correct, errors