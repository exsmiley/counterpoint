from interval import findNoteFromInterval, enharmonicSwitch

# Gives a major scale based on the specified note
# @param note:str the name of a note
# @return list<str> a list of notes that makes up the major scale of note 
def majorScale(note):
	notes = [note]
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes

# Gives a natural minor scale based on the specified note
# @param note:str the name of a note
# @return list<str> a list of notes that makes up the natural minor scale of note 
def minorScale(note):
	notes = [note]
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes

# Gives the first half of the melodic minor scale based on the specified note
# @param note:str the name of a note
# @return list<str> a list of notes that makes up the ascending half of the melodic minor scale of note 
def melodicMinorScale(note):
	notes = [note]
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes

# Gives a harmonic minor scale based on the specified note
# @param note:str the name of a note
# @return list<str> a list of notes that makes up the harmonic minor scale of note 
def harmonicMinorScale(note):
	notes = [note]
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "A2"))
	return notes

# Gives a minor pentatonic scale based on the specified note
# @param note:str the name of a note
# @return list<str> a list of notes that makes up the minor pentatonic scale of note 
def bluesScale(note):
	notes = [note]
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m3"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "A1"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m3"))
	return notes

# Gives a Phrygian Dominant scale based on the specified note
# @param note:str the name of a note
# @return list<str> a list of notes that makes up the Phrygian Dominant scale of note 
def phrygianDominantScale(note):
	notes = [note]
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "A2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes

# Gives a lydian scale based on the specified note
# @param note:str the name of a note
# @return list<str> a list of notes that makes up the lydian scale of note 
def lydianScale(note):
	notes = [note]
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes

# Gives a mixolydian scale based on the specified note
# @param note:str the name of a note
# @return list<str> a list of notes that makes up the lydian scale of note 
def mixolydianScale(note):
	notes = [note]
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	return notes

# Gives a Hungarian minor scale based on the specified note
# @param note:str the name of a note
# @return list<str> a list of notes that makes up the Hungarian minor scale of note 
def hungarianMinorScale(note):
	notes = [note]
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "A2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "A2"))
	return notes

# Gives the notes of the Locrian mode based on the specified note.
#	also called Greek mixolydian
# @param note:str the name of a note
# @return list<str> a list of notes that makes up the Hungarian minor scale of note 
def locrianScale(note):
	notes = [note]
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes

# Gives a diminished scale based on the specified note
# @param note:str the name of a note
# @return list<str> a list of notes that makes up the diminished scale of note 
def diminishedScale(note):
	notes = [note]
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-2], "A2"))
	notes.append(enharmonicSwitch(findNoteFromInterval(notes[len(notes)-1], "M2"), 1))
	notes.append(findNoteFromInterval(enharmonicSwitch(notes[len(notes)-1], -1), "m2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "M2"))
	notes.append(findNoteFromInterval(notes[len(notes)-1], "m2"))
	return notes

