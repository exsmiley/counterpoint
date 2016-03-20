semitones = {"C": 0, "C#": 1, "Db" : 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "Fb":4, "E#":5, "F": 5, "F#": 6, "Gb" : 6, 
				"G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11, 'Cb':11, 'B#':12}

intervalMap = {0: "P8", 1: "m2", 2: "M2", 3: "m3", 4: "M3", 5: "P4", 6: "A4", 7:"P5", 8:"m6", 9:"M6", 10:"m7", 11:"M7"}

distanceBetweenIntervals = {} # an inverse version of intervalMap

# invert the intervalMap
for distance in intervalMap.keys():
	distanceBetweenIntervals[intervalMap[distance]] = distance

# missing the case of a unison
distanceBetweenIntervals["P1"] = 0

# Finds the size of the interval between two note but ignores the enharmonic equivalents
# @param note1:str the name of a note
# @param note2:str the name of a note
# @return int representing the size of the interval
def findIntervalSize(note1, note2):
	# weird edge case when the notes are B and F
	if note1[0] == 'B' and note2[0] == 'F':
		return 5
	if note1[0] == 'F' and note2[0] == 'B':
		return 3
	return int(intervalMap[(semitones[note2[0]] - semitones[note1[0]]) % 12][1])

# Finds the correct quality of the interval based on the interval size, previously wrong quality,
# 	and how wrong the quality was.
# @param intervalSize:int the size of the interval
# @param wrongQuality:str the kind of interval it tried to be (ie. d, m, M, P, A, etc.)
# @param delta:int the error in wrongQuality including the direction based on positive/negative
# @return str the correct quality for this interval
def fixQuality(intervalSize, wrongQuality, delta):
	quality = "wrong"
	if intervalSize == 4 or intervalSize == 5 or intervalSize == 8:
		if wrongQuality == 'M':
			wrongQuality = 'P'
		elif wrongQuality == 'm':
			wrongQuality = 'd'
		qualities = ['dd', 'd', 'P', 'A','AA']
		index = qualities.index(wrongQuality) + delta
		quality = qualities[index]
	else:
		if wrongQuality == 'P':
			wrongQuality = 'M'
		qualities = ['dd', 'd', 'm', 'M', 'A','AA']
		index = qualities.index(wrongQuality) + delta
		quality = qualities[index]
	return quality

# Finds the quality of the interval between note1 and note2
# @param note1:str the name of a note
# @param note2:str the name of a note
# @return str the quality of the interval between the two notes (ie. d, m, M, P, A, etc.)
def findQuality(note1, note2):
	intervalSize = findIntervalSize(note1, note2)
	# what the interval sounds like regardless of its formal name
	soundsLike = intervalMap[(semitones[note2[0]] - semitones[note1[0]]) % 12]
	wrongQuality = soundsLike[0]
	# weird edge case when the notes are B and F
	if note1[0] == 'B' and note2[0] == 'F':
		wrongQuality = 'd'
	if note1[0] == 'F' and note2[0] == 'B':
		wrongQuality = 'A'
	delta = 0
	if len(note1) > 1:
		if note1[1] == '#':
			delta -= 1
		elif note1[1] == 'b':
			delta += 1
	if len(note2) > 1:
		if note2[1] == '#':
			delta += 1
		elif note2[1] == 'b':
			delta -= 1
	if delta >= 12 or delta <= -12:
		delta = delta % 12
	return fixQuality(intervalSize, wrongQuality, delta)

# Finds the size and quality of the interval between note1 and note2
# @param note1:str the name of a note
# @param note2:str the name of a note
# @return str the quality of the interval between the two notes and the size (ie. d7, m2, M3, P5, A4, etc.)
def findInterval(note1, note2):
	if not findQuality(note1, note2):
		return "bob"
	return findQuality(note1, note2) + str(findIntervalSize(note1, note2))