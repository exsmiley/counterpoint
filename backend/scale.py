from interval import findNoteFromInterval

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
