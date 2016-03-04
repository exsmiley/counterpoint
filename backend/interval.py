semitones = {"C": 0, "C#": 1, "Db" : 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "Fb":4, "E#":5, "F": 5, "F#": 6, "Gb" : 6, 
				"G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11, 'Cb':11, 'B#':12}

intervalMap = {0: "P8", 1: "m2", 2: "M2", 3: "m3", 4: "M3", 5: "P4", 6: "A4", 7:"P5", 8:"m6", 9:"M6", 10:"m7", 11:"M7"}

# Finds the size of the interval between two note but ignores the enharmonic equivalents
# @return int representing the size of the interval
def findIntervalSize(note1, note2):
	return int(intervalMap[(semitones[note2[0]] - semitones[note1[0]]) % 12][1])

def fixQuality(intervalSize, wrongQuality, delta):
	quality = "bob"
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

def findQuality(note1, note2):
	intervalSize = findIntervalSize(note1, note2)
	# what the interval sounds like regardless of its formal name
	soundsLike = intervalMap[(semitones[note2[0]] - semitones[note1[0]]) % 12]
	otherInterval = int(soundsLike[1])
	wrongQuality = soundsLike[0]
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
	print note1, note2, intervalSize, delta, wrongQuality
	return fixQuality(intervalSize, wrongQuality, delta)


def findInterval(note1, note2):
	if not findQuality(note1, note2):
		return "bob"
	return findQuality(note1, note2) + str(findIntervalSize(note1, note2))

a = (5 - 11) % 13
print a
print intervalMap[a]