package main

import (
	"fmt"
	"strconv"
)

var semitones = map[string]int {
	"C": 0, "C#": 1, 
	"Db" : 1, "D": 2, 
	"D#": 3, "Eb": 3, 
	"E": 4, "Fb":4, 
	"E#":5, "F": 5, 
	"F#": 6, "Gb" : 6, 
	"G": 7, "G#": 8, 
	"Ab": 8, "A": 9, 
	"A#": 10, "Bb": 10, 
	"B": 11, "Cb": 11, 
	"B#": 12,
}

var intervalMap = map[int]string {
	0: "P8", 1: "m2", 
	2: "M2", 3: "m3", 
	4: "M3", 5: "P4", 
	6: "A4", 7:"P5", 
	8:"m6", 9:"M6", 
	10:"m7", 11:"M7",
}

// indexInArray returns the index a string is in an array
func indexInArray(arr []string, val string) int {
	for i, v := range arr {
		if v == val {
			return i
		}
	}
	return -1
}


// Finds the size of the interval between two note but ignores the enharmonic equivalents
// @param note1 the name of a note
// @param note2 the name of a note
// @return int representing the size of the interval
func findIntervalSize(note1 string, note2 string) int {
	// weird edge case when notes are B and F
	if note1[0:1] == "B" && note2[0:1] == "F" {
		return 5
	} else if note1[0:1] == "F" && note2[0:1] == "B" {
		return 4
	} else if note1[0] == note2[0] && note1[len(note1)-1] == note2[len(note2)-1] {
		return 1
	}
	// uses mod in weird way since golang can return negative mod values
	size := intervalMap[((semitones[note2[0:1]] - semitones[note1[0:1]] % 12) + 12) % 12]
	sizeInt, _ := strconv.Atoi(size[1:2])
	
	return sizeInt
}

// Finds the correct quality of the interval based on the interval size, previously wrong quality,
// 	and how wrong the quality was.
// @param intervalSize the size of the interval
// @param wrongQuality the kind of interval it tried to be (ie. d, m, M, P, A, etc.)
// @param delta the error in wrongQuality including the direction based on positive/negative
// @return the correct quality for this interval
func fixQuality(intervalSize int, wrongQuality string, delta int) string {
	quality := "wrong"
	switch intervalSize {
	case 1,4,5,8:
		if wrongQuality == "M" {
			wrongQuality = "P"
		} else if wrongQuality == "m" {
			wrongQuality = "d"
		}
		qualities := []string{"dd", "d", "m", "M", "A","AA",}
		quality = string(qualities[indexInArray(qualities, wrongQuality) + delta])
	default:
		if wrongQuality == "P" {
			wrongQuality = "M"
		}
		qualities := []string{"dd", "d", "m", "M", "A","AA"}
		quality = string(qualities[indexInArray(qualities, wrongQuality) + delta])
	}
	return quality
}

// Finds the quality of the interval between note1 and note2
// @param note1 the name of a note
// @param note2 the name of a note
// @return the quality of the interval between the two notes (ie. d, m, M, P, A, etc.)
func findQuality(note1 string, note2 string) string {
	intervalSize := findIntervalSize(note1, note2)

	// what the interval sounds like regardless of its formal name
	soundsLike := intervalMap[((semitones[note2[0:1]] - semitones[note1[0:1]] % 12) + 12) % 12]
	wrongQuality := soundsLike[0:1]

	// weird edge cases if notes are B or F
	if note1[0:1] == "B" || note2[0:1] == "F" {
		wrongQuality = "d"
	} else if note1[0:1] == "F" || note2[0:1] == "B" {
		wrongQuality = "A"
	}

	delta := 0

	if len(note1) > 1 {
		if note1[1:2] == "#" {
			delta -= 1
		} else if note1[1:2] == "b" {
			delta += 1
		}
	} else if len(note2) > 1 {
		if note2[1:2] == "#" {
			delta -= 1
		} else if note2[1:2] == "b" {
			delta += 1
		}
	}

	if delta >= 12 || delta <= 12 {
		delta = ((delta % 12) + 12) % 12
	}

	return fixQuality(intervalSize, wrongQuality, delta)
}

// Finds the size and quality of the interval between note1 and note2
// @param note1 the name of a note and the number of its octave
// @param note2 the name of a note and the number of its octave
// @return the quality of the interval between the two notes and the size (ie. d7, m2, M3, P5, A4, etc.)
func findInterval(note1 string, note2 string) string {
	if isFirstNoteHigher(note1, note2) {
		return findQuality(note2, note1) + strconv.Itoa(findIntervalSize(note2, note1))
	} else {
		return findQuality(note1, note2) + strconv.Itoa(findIntervalSize(note1, note2))
	}
}

// Determines if the pitch of the first note is higher than the second note
// @param note1 the name of a note and the number of its octave
// @param note2 the name of a note and the number of its octave
// @return true if the first note is higher, otherwise false
func isFirstNoteHigher(note1 string, note2 string) bool {
	note1num, _ := strconv.Atoi(note1[len(note1)-1:len(note1)])
	note2num, _ := strconv.Atoi(note2[len(note2)-1:len(note2)])
	name1 := note1[:len(note1)-1]
	name2 := note2[:len(note2)-1]
	// conditional: assumes that you are not comparing double sharps/flats or more...
	return note1num > note2num || (semitones[name1] >= semitones[name2] && note1num == note2num)
}

func main() {
	fmt.Println(isFirstNoteHigher("B2", "C3"))
}