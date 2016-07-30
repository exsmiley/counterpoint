package scale

import (
	"counterpoint/interval"
	"strconv"
)

// Gives a major scale starting on the specified note
func MajorScale(note string) []string{
	_, err := strconv.Atoi(note[len(note)-1:len(note)]); if err != nil {
		note = note + "3"
	}
	notes := []string {note,}
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes
}

// Gives a minor scale starting on the specified note
func MinorScale(note string) []string{
	_, err := strconv.Atoi(note[len(note)-1:len(note)]); if err != nil {
		note = note + "3"
	}
	notes := []string {note,}
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes
}

// Gives a melodic minor scale starting on the specified note
func MelodicMinorScale(note string) []string{
	_, err := strconv.Atoi(note[len(note)-1:len(note)]); if err != nil {
		note = note + "3"
	}
	notes := []string {note,}
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes
}

// Gives a harmonic minor scale starting on the specified note
func HarmonicMinorScale(note string) []string{
	_, err := strconv.Atoi(note[len(note)-1:len(note)]); if err != nil {
		note = note + "3"
	}
	notes := []string {note,}
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "A2"))
	return notes
}

// Gives a minor pentatonic blues scale starting on the specified note
func BluesScale(note string) []string{
	_, err := strconv.Atoi(note[len(note)-1:len(note)]); if err != nil {
		note = note + "3"
	}
	notes := []string {note,}
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m3"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "A1"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m3"))
	return notes
}

// Gives a phrygian dominant scale starting on the specified note
func PhrygianDominantScale(note string) []string{
	_, err := strconv.Atoi(note[len(note)-1:len(note)]); if err != nil {
		note = note + "3"
	}
	notes := []string {note,}
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "A2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes
}

// Gives a lydian scale starting on the specified note
func LydianScale(note string) []string{
	_, err := strconv.Atoi(note[len(note)-1:len(note)]); if err != nil {
		note = note + "3"
	}
	notes := []string {note,}
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes
}

// Gives a mixolydian scale starting on the specified note
func MixolydianScale(note string) []string{
	_, err := strconv.Atoi(note[len(note)-1:len(note)]); if err != nil {
		note = note + "3"
	}
	notes := []string {note,}
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	return notes
}

// Gives a Hungarian minor scale starting on the specified note
func HungarianMinorScale(note string) []string{
	_, err := strconv.Atoi(note[len(note)-1:len(note)]); if err != nil {
		note = note + "3"
	}
	notes := []string {note,}
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "A2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "A2"))
	return notes
}

// Gives a locrian scale starting on the specified note
func LocrianScale(note string) []string{
	_, err := strconv.Atoi(note[len(note)-1:len(note)]); if err != nil {
		note = note + "3"
	}
	notes := []string {note,}
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	return notes
}

// Gives a diminished scale starting on the specified note
func DiminishedScale(note string) []string{
	_, err := strconv.Atoi(note[len(note)-1:len(note)]); if err != nil {
		note = note + "3"
	}
	notes := []string {note,}
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "M2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "A2"))
	notes = append(notes, interval.SwitchEnharmonic(interval.FindNoteFromInterval(notes[len(notes)-1], "M2"), 1))
	notes = append(notes, interval.FindNoteFromInterval(interval.SwitchEnharmonic(notes[len(notes)-1], -1), "m2"))
	notes = append(notes, interval.FindNoteFromInterval(notes[len(notes)-1], "m2"))
	return notes
}