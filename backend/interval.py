semitones = {"C": 0, "C#": 1, "Db" : 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6, "Gb" : 6, 
				"G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}

intervalMap = {0: "P1", 1: "m2", 2: "M2", 3: "m3", 4: "M3", 5: "P4", 6: "A4", 7:"P5", 8:"m6", 9:"M6", 10:"m7", 11:"M7"}

# todo make it handle even more notes ie. B#

# return type = int
def findIntervalSize(note1, note2):
	return int(intervalMap[(semitones[note2[0]] - semitones[note1[0]]) % 12][1])

def findQuality(note1, note2):
	intervalSize = findIntervalSize(note1, note2)
	# what the interval sounds like regardless of its formal name
	soundsLike = intervalMap[(semitones[note2] - semitones[note1]) % 12]
	otherInterval = int(soundsLike[1])
	# it's actually the interval that it sounds like
	if otherInterval == intervalSize:
		return soundsLike[0]
	# ie. it sounds like a M6 but it's actually going to be a m7
	elif intervalSize - otherInterval == 1:
		if intervalSize == 4 or intervalSize == 5:
			return "d"
		else:
			return "m"
	elif intervalSize - otherInterval == 2:
		if intervalSize == 4 or intervalSize == 5:
			return "dd"
		else:
			return "d"
	elif intervalSize - otherInterval == -1:
		if intervalSize == 4 or intervalSize == 5:
			return "A"
		else:
			return "A"
	else:
		# no idea what could make it get to here...
		return None


def findInterval(note1, note2):
	return findQuality(note1, note2) + str(findIntervalSize(note1, note2))

# some tests
print findInterval('B', 'C') == 'm2'
print findInterval('D#', 'G') == 'd4'
print findInterval('C', 'B') == 'M7'