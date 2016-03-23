from interval import findInterval, semitoneDistanceFromInterval, enharmonicSwitch, findNoteFromInterval

print "Testing methods in interval..."
passed = True

# tests for findInterval (integration test)
tests = {('B2', 'C3'):'m2', ('D#3', 'G3'):'d4', ('C4', 'B4'):'M7', ('G#3', 'A3'):'m2', ('F#3', 'C#4'):'P5',
			('Eb3', 'G3'):'M3', ('F1', 'Db1'):'M3', ('Ab3', 'Bb3'):'M2', ('A2', 'C3'):'m3', ('C#4', 'A4'):'m6',
			('B5', 'F#5'):'P4', ('B5', 'Gb6'):'d6', ('C2', 'C#3'):'A8', ('E6', 'Eb7'):'d8', ('D#3', "B3"):'m6',
			('C4', 'E4'):'M3', ('D#5', 'B6'):'m6', ('Db2', 'F3'):'M3', ('Eb4', 'Cb4'):'m6', ('F#5', 'G5'):'m2',
			('C6', 'F6'):'P4', ('E2', 'B3'):'P5', ('Bb5', 'A6'):'M7', ('Gb4', 'Ab4'):'M2', ('D3', 'Gb3'):'d4',
			('G5', 'Bb5'):'m3', ('B3', 'G4'):'m6', ('Gb5', 'Db5'):'P4', ('Gb1', 'D1'):'d4', ('G3', 'D#4'):'A5',
			('C#5', 'D5'):'m2', ('C#6', 'A5'):'M3', ('Bb3', 'D2'):'m6', ('Fb5', 'Cb5'):'P5', ('B#3', 'C#4'):'m2',
			('C3', 'B#3'):'A7', ('C4', 'F4'):'P4', ('C5', 'F#5'):'A4', ('B2', 'F2'):'A4', ('F1', 'Bb1'):'P4', 
			('B5', 'E5'):'P5', ("B4", "B5"): "P8", ("A3", "A3"): "P1"}
failed = []

for test in tests.keys():
	testValue = findInterval(test[0], test[1])
	if testValue != tests[test]:
		failed.append("Failed " + str(test) + ". Expected: " + tests[test] + " but got " + testValue)

if len(failed) == 0:
	print "Passed all " + str(len(tests.keys())) + " tests for findInterval."
else:
	passed = False
	print "Failed a total of " + str(len(failed)) + " tests for findInterval."

for fail in failed:
	print fail

# tests for semitoneDistanceFromInterval
tests = {"P1": 0, "dd2": -1, "d2": 0, "m2": 1, "M2": 2, "A2": 3, "AA2": 4, "dd3": 1, "d3": 2, "m3": 3, 
			"M3": 4, "A3": 5, "AA3": 6, "dd4": 3, "d4": 4, "P4": 5, "A4": 6, "d5": 6, "P5": 7, "A5": 8,
			"AA5": 9, "m6": 8, "M6": 9, "m7": 10, "M7": 11, "A7": 12, "P8": 12}
failed = []

for test in tests.keys():
	testValue = semitoneDistanceFromInterval(test)
	if testValue != tests[test]:
		failed.append("Failed " + str(test) + ". Expected: " + str(tests[test]) + " but got " + str(testValue))

if len(failed) == 0:
	print "Passed all " + str(len(tests.keys())) + " tests for semitoneDistanceFromInterval."
else:
	passed = False
	print "Failed a total of " + str(len(failed)) + " tests for semitoneDistanceFromInterval."

for fail in failed:
	print fail

# tests for enharmonicSwitch
tests = {('B', 1):'Cb', ("C#", 1): "Db", ("E", 1): "Fb", ("G", -1): "F##", ("A#", 1): "Bb", ("Bb", -1): "A#", 
		("F", -1): "E#", ("C", -1): "B#"}
failed = []

for test in tests.keys():
	testValue = enharmonicSwitch(test[0], test[1])
	if testValue != tests[test]:
		failed.append("Failed " + str(test) + ". Expected: " + tests[test] + " but got " + testValue)

if len(failed) == 0:
	print "Passed all " + str(len(tests.keys())) + " tests for enharmonicSwitch."
else:
	passed = False
	print "Failed a total of " + str(len(failed)) + " tests for enharmonicSwitch."

for fail in failed:
	print fail

# tests for findNoteFromInterval
tests = {('B1', "m2"):'C2', ("G#3", "P5"): "D#4", ("E3", "m3"): "G3", ("G4", "m7"): "F5", 
		("A#2", "P4"): "D#3", ("Bb3", "M6"): "G4", ("A3", "m2"): "Bb3"}
failed = []

for test in tests.keys():
	testValue = findNoteFromInterval(test[0], test[1])
	if testValue != tests[test]:
		failed.append("Failed " + str(test) + ". Expected: " + tests[test] + " but got " + testValue)

if len(failed) == 0:
	print "Passed all " + str(len(tests.keys())) + " tests for findNoteFromInterval."
else:
	passed = False
	print "Failed a total of " + str(len(failed)) + " tests for findNoteFromInterval."

for fail in failed:
	print fail

if passed:
	print "Passed all tests for interval!"