from interval import *
from scale import *
import random
import math



# Checks the rules of first species counterpoint, requires cf and counter to have the same length
# @param cf:list<str> the cantus firmus, a list of notes
# @param counter:list<str> the counterpoint, a list of notes
# @return (boolean, list<str) True if all of the rules are followed, incidents
# 	where the rules are broken
def checkFirstSpeciesRules(cf, counter):
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
		errors.append("Incorrect start of a " + verticalIntervals[0] + " at position 0")

	# check end
	if not verticalIntervals[len(verticalIntervals)-1] in ["P1", "P8"]:
		errors.append("Incorrect ending of a " + verticalIntervals[len(verticalIntervals)-1] + " at position " + str(len(counter)-1))

	correct = len(errors) == 0
	return correct, errors


def findFirstSpecies(cf, scale_type="major"):
	scale = majorScale(cf[len(cf)-1]) # get possible notes that can be used
	possible = []
	# put notes an octave higher for less chance of crossing over
	for note in scale:
		possible.append(note[:-1] + str(int(note[-1]) + 1))

	goodHorizontalIntervals = ["m2", "M2", "m3", "M3", "P4", "P5", "m6", "M6", "P8"]
	goodVerticalIntervals = ["P1", "m3", "M3", "P5", "m6", "M6", "P8"]

	counter = [{"possible": [] + possible, "chosen": None} for i in range(len(cf))]

	# first handle beginning
	for i in range(len(counter[0]["possible"])):
		note = counter[0]["possible"][i]
		verticalInterval = findInterval(cf[0], note)
		if verticalInterval not in ["M3", "P1", "P5", "P8"]:
			counter[0]["possible"][i] = None
	# get rid of impossible notes
	counter[0]["possible"] = [note for note in counter[0]["possible"] if note]

	if len(counter[0]["possible"]) == 0:
		return None
	counter[0]["chosen"] = counter[0]["possible"][int(math.floor(random.random()*len(counter[0]["possible"])))]
	
	# now handle ending
	for i in range(len(counter[len(counter)-1]["possible"])):
		note = counter[len(counter)-1]["possible"][i]
		verticalInterval = findInterval(cf[0], note)
		if verticalInterval not in ["P1", "P8"]:
			counter[len(counter)-1]["possible"][i] = None

	counter[len(counter)-1]["possible"] = [note for note in counter[len(counter)-1]["possible"] if note]
	if len(counter[len(counter)-1]["possible"]) == 0:
		return None
	counter[len(counter)-1]["chosen"] = counter[len(counter)-1]["possible"][int(math.floor(random.random()*len(counter[len(counter)-1]["possible"])))]

	return counter


def alpha_beta():
	pass


cf = ["C2", "D2", "E2", "A2", "F2", "E2", "F2", "D2", "D2", "C2"]

print findFirstSpecies(cf)
