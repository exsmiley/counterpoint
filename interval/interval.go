package interval

import (
    "strconv"
    "strings"
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

var intervalDistanceHelper = map[string]int{
    "M6": 9, "m3": 3, "P4": 5,
    "P5": 7, "P1": 0, "m2": 1,
    "M7": 11, "m7": 10, "m6": 8,
    "A4": 6, "M3": 4, "M2": 2,
    "P8": 12,
}

var semitoneReversed = map[int]string {
    0: "C", 1: "C#", 2: "D",
    3: "D#", 4: "E", 5: "F",
    6: "F#", 7: "G", 8: "G#",
    9: "A", 10: "A#", 11: "B",
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
//  and how wrong the quality was.
// @param intervalSize the size of the interval
// @param wrongQuality the kind of interval it tried to be (ie. d, m, M, P, A, etc.)
// @param delta the error in wrongQuality including the direction based on positive/negative
// @return the correct quality for this interval
func fixQuality(intervalSize int, wrongQuality string, delta int) string {
    quality := "wrong"
    switch intervalSize {
    case 1,4,5,8:
        if wrongQuality == "M" || wrongQuality == "m"{
            wrongQuality = "P"
        } 

        qualities := []string{"dd", "d", "P", "A","AA",}
        index := indexInArray(qualities, wrongQuality) + delta

        if index < 0 {
            index = (index % len(qualities)) + len(qualities)
        } else if index > len(qualities) - 1 {
            index = index % len(qualities)
        }

        quality = string(qualities[index])
    default:
        if wrongQuality == "P" && delta >= 0{
            wrongQuality = "M"
        } else if wrongQuality == "P" {
            wrongQuality = "m"
        }

        qualities := []string{"dd", "d", "m", "M", "A","AA"}
        index := indexInArray(qualities, wrongQuality) + delta

        if index < 0 {
            index = (index % len(qualities)) + len(qualities)
        } else if index > len(qualities) - 1 {
            index = index % len(qualities)
        }

        quality = string(qualities[index])
    }
    return quality
}

// Finds the quality of the interval between note1 and note2
// @param note1 the name of a note
// @param note2 the name of a note
// @return the quality of the interval between the two notes (ie. d, m, M, P, A, etc.)
func findQuality(note1 string, note2 string) string {
    intervalSize := findIntervalSize(note1, note2)

    name1 := note1[:len(note1)-1]
    name2 := note2[:len(note2)-1]
    // what the interval sounds like regardless of its formal name
    soundsLike := intervalMap[((semitones[name2] - semitones[name1] % 12) + 12) % 12]
    wrongQuality := soundsLike[0:1]

    val, _ := strconv.Atoi(soundsLike[1:2])

    delta := val - intervalSize

    if intervalSize == 1 && val == 8 {
        delta = 0
    }

    if name1[:1] == name2[:1] && wrongQuality != "P" {
        wrongQuality = "P"
        delta = 0
        if note1[1:2] == "#" {
            delta -= 1
        } else if note1[1:2] == "b" {
            delta += 1
        }
        if note2[1:2] == "#" {
            delta += 1
        } else if note2[1:2] == "b" {
            delta -= 1
        }
    }

    if delta >= 12 || delta <= -12 {
        delta = ((delta % 12) + 12) % 12
    }

    return fixQuality(intervalSize, wrongQuality, delta)
}

// Finds the size and quality of the interval between note1 and note2
// @param note1 the name of a note and the number of its octave
// @param note2 the name of a note and the number of its octave
// @return the quality of the interval between the two notes and the size (ie. d7, m2, M3, P5, A4, etc.)
func FindInterval(note1 string, note2 string) string {
    if IsFirstNoteHigher(note1, note2) {
        return findQuality(note2, note1) + strconv.Itoa(findIntervalSize(note2, note1))
    } else {
        return findQuality(note1, note2) + strconv.Itoa(findIntervalSize(note1, note2))
    }
}

// Determines if the pitch of the first note is higher than the second note
// @param note1 the name of a note and the number of its octave
// @param note2 the name of a note and the number of its octave
// @return true if the first note is higher, otherwise false
func IsFirstNoteHigher(note1 string, note2 string) bool {
    note1num, _ := strconv.Atoi(note1[len(note1)-1:len(note1)])
    note2num, _ := strconv.Atoi(note2[len(note2)-1:len(note2)])
    name1 := note1[:len(note1)-1]
    name2 := note2[:len(note2)-1]
    if len(name1) > 2 {
        name1 = name1[:2]
    }
    if len(name2) > 2 {
        name2 = name2[:2]
    }

    // conditional: assumes that you are not comparing double sharps/flats or more...
    return note1num > note2num || (semitones[name1] >= semitones[name2] && note1num == note2num)
}

// Finds the semitone distance of a specified interval
// @param interval the name of an interval (ie. d7, m2, M3, P5, A4, etc.)
// @return the semitone distance between notes with that interval
func semitoneDistanceFromInterval(interval string) int {
    distance := 0
    intervalDistance := interval[len(interval)-1:len(interval)]
    // handle possibly perfect intervals
    switch intervalDistance {
    case "1", "4", "5", "8":
        distance = intervalDistanceHelper["P" + intervalDistance]

        if strings.Contains(interval, "d") {
            // scales with the number of diminisheds
            return distance - len(interval) + 1
        } else if strings.Contains(interval, "A") {
            // scales with the number of augmenteds
            return distance + len(interval) - 1
        } else {
            // that means it's actually perfect!
            return distance
        }
    default:
        // minor/diminished handling
        if strings.ContainsAny(interval, "m d") {
            distance = intervalDistanceHelper["m" + intervalDistance]

            if strings.Contains(interval, "d") {
                // scales with the number of diminisheds
                return distance - len(interval) + 1
            } else {
                // that means it's minor!
                return distance
            }
        } else {
            // major/augmented handling
            distance = intervalDistanceHelper["M" + intervalDistance]

            if strings.Contains(interval, "A") {
                // scales with the number of augmenteds
                return distance + len(interval) - 1
            } else {
                // that means it's major!
                return distance
            }
        }
    }
    return 1
}

// Finds the enharmonic equivalent of this note
// @param note the name of a note
// @param up the direction of the letter name you want to switch
// @return the note that is the enharmonic equivalent of this note
func SwitchEnharmonic(note string, up int) string {
    names := []string {"C", "D", "E", "F", "G", "A", "B"}
    noteIndex := 0

    for i, name := range names {
        if name == note[0:1] {
            noteIndex = i
        }
    }

    enharmonicIndex := (((noteIndex + up) % 7) + 7) % 7
    otherNote := names[enharmonicIndex]

    // use relative position to find the equivalent enharmonic name
    position := semitones[note[0:1]]

    // add sharps/flats
    for i := range note {
        if note[i:i+1] == "#" {
            position += 1
        } else if note[i:i+1] == "b" {
            position -= 1
        }
    }

    // deal with wrapping around in semitones
    if (noteIndex + up != enharmonicIndex) && (noteIndex + up > 0) {
        position -= 12
    } else if (noteIndex + up != enharmonicIndex) && (noteIndex + up < 0) {
        position += 12
    }

    otherNotePosition := semitones[otherNote]
    change := position - otherNotePosition

    // now add sharps and flats as need to otherNote
    if change > 0 {
        for i := 0; i < change; i++ {
            otherNote += "#"
        }
    } else {
        for i := 0; i < -change; i++ {
            otherNote += "b"
        }
    }

    return otherNote
}

// Finds the note above that is the given interval away
// @param note the name of a note and the number of its octave
// @param interval the name of an interval (ie. d7, m2, M3, P5, A4, etc.) up to 8ths
// @return the name of a note that is the specified interval away
func FindNoteFromInterval(note string, interval string) string {
    distance := semitoneDistanceFromInterval(interval)

    initialPosition := semitones[note[0:1]]

    // add sharps/flats
    for i := range note {
        if note[i:i+1] == "#" {
            initialPosition += 1
        } else if note[i:i+1] == "b" {
            initialPosition -= 1
        }
    }

    otherNotePosition := (((initialPosition + distance) % 12) + 12) % 12
    otherNote := semitoneReversed[otherNotePosition]

    if (initialPosition + distance) == otherNotePosition {
        otherNote += note[len(note)-1:len(note)]
    } else {
        oneHigher, _ := strconv.Atoi(note[len(note)-1:len(note)])
        otherNote += strconv.Itoa(oneHigher+1)
    }

    otherInterval := FindInterval(note, otherNote)

    // make sure that the note is the harmonic note that it is supposed to be
    intervalNum, _ := strconv.Atoi(interval[len(interval)-1:len(interval)])
    otherIntervalNum, _ := strconv.Atoi(otherInterval[len(otherInterval)-1:len(otherInterval)])
    enharmonicChange := intervalNum - otherIntervalNum

    enharmonicName := SwitchEnharmonic(otherNote[:len(otherNote)-1], enharmonicChange)
    pitchRange := otherNote[len(otherNote)-1:len(otherNote)]

    return enharmonicName + pitchRange
}
