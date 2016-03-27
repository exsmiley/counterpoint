semitones = {"C": 0, "C#": 1, "Db" : 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "Fb":4, "E#":5, "F": 5, "F#": 6, "Gb" : 6, 
				"G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11, 'Cb':11, 'B#':12}

intervalMap = {0: "P8", 1: "m2", 2: "M2", 3: "m3", 4: "M3", 5: "P4", 6: "A4", 7:"P5", 8:"m6", 9:"M6", 10:"m7", 11:"M7"}

# Finds the size of the interval between two note but ignores the enharmonic equivalents
# @param note1:str the name of a note
# @param note2:str the name of a note
# @return int representing the size of the interval
def findIntervalSize(note1, note2):
	# weird edge case when the notes are B and F
	if note1[0] == 'B' and note2[0] == 'F':
		return 5
	if note1[0] == 'F' and note2[0] == 'B':
		return 4
	if note1[0] == note2[0] and note1[len(note1)-1] == note2[len(note2)-1]:
		return 1
	return int(intervalMap[(semitones[note2[0]] - semitones[note1[0]]) % 12][1])

# Finds the correct quality of the interval based on the interval size, previously wrong quality,
# 	and how wrong the quality was.
# @param intervalSize:int the size of the interval
# @param wrongQuality:str the kind of interval it tried to be (ie. d, m, M, P, A, etc.)
# @param delta:int the error in wrongQuality including the direction based on positive/negative
# @return str the correct quality for this interval
def fixQuality(intervalSize, wrongQuality, delta):
	quality = "wrong"
	if intervalSize in [1, 4, 5, 8]:
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
# @param note1:str the name of a note and the number of its octave
# @param note2:str the name of a note and the number of its octave
# @return str the quality of the interval between the two notes and the size (ie. d7, m2, M3, P5, A4, etc.)
def findInterval(note1, note2):
	if isFirstNoteHigher(note1, note2):
		return findQuality(note2, note1) + str(findIntervalSize(note2, note1))
	else:
		return findQuality(note1, note2) + str(findIntervalSize(note1, note2))

# Determines if the pitch of the first note is higher than the second note
# @param note1:str the name of a note and the number of its octave
# @param note2:str the name of a note and the number of its octave
# @return bool true if the first note is higher, otherwise false
def isFirstNoteHigher(note1, note2):
	note1num = int(note1[len(note1)-1])
	note2num = int(note2[len(note2)-1])
	name1 = note1[:len(note1)-1]
	name2 = note2[:len(note2)-1]
	# conditional: assumes that you are not comparing double sharps/flats or more...
	return note1num > note2num or (semitones[name1[:2]] >= semitones[name2[:2]] and note1num == note2num)


# data structure to known the semitone distance from tonic for a specified interval
distanceBetweenIntervals = {}

# invert the intervalMap
for distance in intervalMap.keys():
	distanceBetweenIntervals[intervalMap[distance]] = distance

# missing the case of a unison
distanceBetweenIntervals["P1"] = 0
# P8 is incorrect
distanceBetweenIntervals["P8"] = 12

# Finds the semitone distance of a specified interval
# @param interval:str the name of an interval (ie. d7, m2, M3, P5, A4, etc.)
# @return int the semitone distance between notes with that interval
def semitoneDistanceFromInterval(interval):
	distance = 0
	# handle intervals that were perfect
	if interval[len(interval)-1] == '4' or interval[len(interval)-1] == '5' or interval[len(interval)-1] == '8' or interval[len(interval)-1] == '1':
		distance = distanceBetweenIntervals['P' + interval[len(interval)-1]]
		if interval.find('d') > -1:
			return distance - len(interval) + 1 # scales with the number of diminisheds
		elif interval.find('A') > -1:
			return distance + len(interval) - 1 # scales with the number of augmenteds
		# that means it's perfect!
		else:
			return distance

	else:
		# minor/diminished handling
		if interval.find("m") > -1 or interval.find("d") > -1:
			distance = distanceBetweenIntervals['m' + interval[len(interval)-1]]
			if interval.find('d') > -1:
				return distance - len(interval) + 1 # scales with the number of diminisheds
			# that means it's minor!
			else:
				return distance
		# major/augmented handling
		else:
			distance = distanceBetweenIntervals['M' + interval[len(interval)-1]]
			if interval.find('A') > -1:
				return distance + len(interval) - 1 # scales with the number of augmenteds
			# that means it's minor!
			else:
				return distance

# data structure to allow us to find the relation between notes via semitones
reverseSemitoneFinder = {}
for note in semitones.keys():
	if note.find('b') == -1 and note != "E#" and note != "B#":
		reverseSemitoneFinder[semitones[note]] = note

# Finds the enharmonic equivalent of this note
# @param note:str the name of a note
# @param up:int the direction of the letter name you want to switch
# @return str the note that is the enharmonic equivalent of this note
def enharmonicSwitch(note, up):
	names = ["C", "D", "E", "F", "G", "A", "B"]
	noteIndex = 0
	for i in range(len(names)):
		if names[i] == note[0]:
			noteIndex = i
	otherNote = names[(noteIndex + up) % 7]
	# use relative positions to find the equivalent enharmonic name
	position = semitones[note[0]]
	# add sharps/flats
	for i in range(len(note)):
		if note[i] == "#":
			position += 1
		elif note[i] == "b":
			position -= 1
	# deal with wrapping around in semitones
	if noteIndex + up != (noteIndex + up) % 7 and (noteIndex + up) > 0:
		position -= 12
	elif noteIndex + up != (noteIndex + up) % 7 and (noteIndex + up) < 0:
		position += 12
	otherNotePosition = semitones[otherNote]
	change = position - otherNotePosition
	# now add sharps and flats as needed to otherNote
	if change > 0:
		for i in range(change):
			otherNote += "#"
	else:
		for i in range(-change):
			otherNote += "b"

	return otherNote

# Finds the note above that is the given interval away
# @param note:str the name of a note and the number of its octave
# @param interval:str the name of an interval (ie. d7, m2, M3, P5, A4, etc.) up to 8ths
# @return str the name of a note that is the specified interval away
def findNoteFromInterval(note, interval):
	distance = semitoneDistanceFromInterval(interval)
	initialPosition = semitones[note[0]]
	# add sharps/flats
	for i in range(len(note)-1):
		if note[i] == "#":
			initialPosition += 1
		elif note[i] == "b":
			initialPosition -= 1
	otherNote = reverseSemitoneFinder[(initialPosition + distance) % 12]
	if (initialPosition + distance) % 12 == initialPosition + distance:
		otherNote += note[len(note)-1]
	else:
		otherNote += str(int(note[len(note)-1])+1)
	currentInterval = findInterval(note, otherNote)
	# make sure the note is the harmonic note that it is supposed to be
	enharmonicChange = (int(interval[len(interval)-1]) - int(currentInterval[len(currentInterval)-1])) 
	return enharmonicSwitch(otherNote[:-1], enharmonicChange) + otherNote[len(otherNote)-1]
