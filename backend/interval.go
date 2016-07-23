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


// findIntervalSize finds the size of the interval (ie. 2nd) between two notes
// note1 and note2 are strings with specific note value (ie. C3)
func findIntervalSize(note1 string, note2 string) int{
	// weird edge case when notes are B and F
	if string(note1[0]) == "B" && string(note2[0]) == "F" {
		return 5
	} else if string(note1[0]) == "F" && string(note2[0]) == "B" {
		return 4
	} else if note1[0] == note2[0] && note1[len(note1)-1] == note2[len(note2)-1] {
		return 1
	}
	// uses mod in weird way since go can return negative mod values
	size := intervalMap[((semitones[string(note2[0])] - semitones[string(note1[0])] % 12) + 12) % 12]
	sizeInt, _ := strconv.Atoi(string(size[1]))
	
	return sizeInt
}

// fixQuality returns the correct quality of the interval based on how wrong the quality was
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
		qualities := []string{'dd', 'd', 'm', 'M', 'A','AA'}
		quality = string(qualities[indexInArray(qualities, wrongQuality) + delta])
	}
	return quality
}

func main() {
	a := []int{1,2,3,5,5,}
	fmt.Println(a)
}