from interval import findInterval, semitoneDistanceFromInterval, enharmonicSwitch, findNoteFromInterval

print "Testing methods in interval..."
passed = True

# tests for findInterval (integration test)
tests = {('B', 'C'):'m2', ('D#', 'G'):'d4', ('C', 'B'):'M7', ('G#', 'A'):'m2', ('F#', 'C#'):'P5',
			('Eb', 'G'):'M3', ('F', 'Db'):'m6', ('Ab', 'Bb'):'M2', ('A', 'C'):'m3', ('C#', 'A'):'m6',
			('B', 'F#'):'P5', ('B', 'Gb'):'d6', ('C', 'C#'):'A8', ('E', 'Eb'):'d8', ('D#', "B"):'m6',
			('C', 'E'):'M3', ('D#', 'B'):'m6', ('Db', 'F'):'M3', ('Eb', 'Cb'):'m6', ('F#', 'G'):'m2',
			('C', 'F'):'P4', ('E', 'B'):'P5', ('Bb', 'A'):'M7', ('Gb', 'Ab'):'M2', ('D', 'Gb'):'d4',
			('G', 'Bb'):'m3', ('B', 'G'):'m6', ('Gb', 'Db'):'P5', ('Gb', 'D'):'A5', ('G', 'D#'):'A5',
			('C#', 'D'):'m2', ('C#', 'A'):'m6', ('Bb', 'D'):'M3', ('Fb', 'Cb'):'P5', ('B#', 'C#'):'m2',
			('C', 'B#'):'A7', ('C', 'F'):'P4', ('C', 'F#'):'A4', ('B', 'F'):'d5', ('F', 'Bb'):'M3', 
			('B', 'E'):'P4'}
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
tests = {('B', 1):'Cb', ("C#", 1): "Db", ("E", 1): "Fb", ("G", -1): "F##", ("A#", 1): "Bb", ("Bb", -1): "A#"}
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
tests = {('B', "m2"):'C', ("G#", "P5"): "D#", ("E", "m3"): "G", ("G", "m7"): "F", ("A#", "P4"): "D#", ("Bb", "M6"): "G"}
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