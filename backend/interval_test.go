package main

import (
	"testing"
)

type intervaltest struct {
	notes []string
	interval string
}

var intervalTests = []intervaltest {
	{[]string {"Eb3", "G3"}, "M3"},
	{[]string {"C#4", "A4"}, "m6"},
	{[]string {"D#3", "B3"}, "m6"},
	{[]string {"E2", "B3"}, "P5"},
	{[]string {"C#5", "D5"}, "m2"},
	{[]string {"B5", "E5"}, "P5"},
	{[]string {"F#3", "C#4"}, "P5"},
	{[]string {"A3", "A3"}, "P1"},
	{[]string {"F#5", "G5"}, "m2"},
	{[]string {"C6", "F6"}, "P4"},
	{[]string {"F1", "Db1"}, "M3"},
	{[]string {"Ab3", "Bb3"}, "M2"},
	{[]string {"Bb3", "D2"}, "m6"},
	{[]string {"A2", "C3"}, "m3"},
	{[]string {"B3", "G4"}, "m6"},
	{[]string {"G#3", "A3"}, "m2"},
	{[]string {"B4", "B5"}, "P8"},
	{[]string {"Gb1", "D1"}, "d4"},
	{[]string {"D#5", "B6"}, "m6"},
	{[]string {"C4", "B4"}, "M7"},
	{[]string {"C5", "F#5"}, "A4"},
	{[]string {"C3", "B#3"}, "A7"},
	{[]string {"B2", "C3"}, "m2"},
	{[]string {"B#3", "C#4"}, "m2"},
	{[]string {"E6", "Eb7"}, "d8"},
	{[]string {"Fb5", "Cb5"}, "P5"},
	{[]string {"F1", "Bb1"}, "P4"},
	{[]string {"B2", "F2"}, "A4"},
	{[]string {"Bb5", "A6"}, "M7"},
	{[]string {"D3", "Gb3"}, "d4"},
	{[]string {"G3", "D#4"}, "A5"},
	{[]string {"C2", "C#3"}, "A8"},
	{[]string {"B5", "F#5"}, "P4"},
	{[]string {"C4", "F4"}, "P4"},
	{[]string {"C#6", "A5"}, "M3"},
	{[]string {"D#3", "G3"}, "d4"},
	{[]string {"Gb5", "Db5"}, "P4"},
	{[]string {"Db2", "F3"}, "M3"},
	{[]string {"Eb4", "Cb4"}, "m6"},
	{[]string {"C4", "E4"}, "M3"},
	{[]string {"B5", "Gb6"}, "d6"},
	{[]string {"Gb4", "Ab4"}, "M2"},
	{[]string {"G5", "Bb5"}, "m3"},
}

func TestFindInterval(t *testing.T) {
	for i, test := range intervalTests {
		notes := test.notes
		interval := test.interval
		answer := findInterval(notes[0], notes[1])
		if interval != answer {
			t.Error("findInterval Test", i, "For", notes, "expected", interval, "got", answer)
		}
	}
}

type semitonetest struct {
	interval string
	semitone int
}

var semitoneTests = []semitonetest {
	{"M7", 11},
	{"M6", 9},
	{"M3", 4},
	{"M2", 2},
	{"d4", 4},
	{"d5", 6},
	{"d2", 0},
	{"d3", 2},
	{"m7", 10},
	{"A3", 5},
	{"m6", 8},
	{"A5", 8},
	{"A4", 6},
	{"m3", 3},
	{"m2", 1},
	{"A2", 3},
	{"P1", 0},
	{"A7", 12},
	{"P4", 5},
	{"P5", 7},
	{"P8", 12},
	{"dd3", 1},
	{"dd2", -1},
	{"dd4", 3},
	{"AA5", 9},
	{"AA3", 6},
	{"AA2", 4},
}

func TestSemitoneDistanceFromInterval(t *testing.T) {
	for i, test := range semitoneTests {
		interval := test.interval
		semitone := test.semitone
		answer := semitoneDistanceFromInterval(interval)
		if semitone != answer {
			t.Error("semitoneDistanceFromInterval Test", i, "For", interval, "expected", semitone, "got", answer)
		}
	}
}