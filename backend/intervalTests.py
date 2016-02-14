from interval import findInterval

# tests for findInterval
tests = {('B', 'C'):'m2', ('D#', 'G'):'d4', ('C', 'B'):'M7', ('G#', 'A'):'m2', ('F#', 'C#'):'P5',
			('Eb', 'G'):'M3', ('F', 'Db'):'m6', ('Ab', 'Bb'):'M2', ('A', 'C'):'m3', ('C#', 'A'):'m6',
			('B', 'F#'):'P5', ('B', 'Gb'):'d6', ('C', 'C#'):'A8', ('E', 'Eb'):'d8', ('D#', "B"):'m6',
			('C', 'E'):'M3', ('D#', 'B'):'P4', ('Db', 'F'):'M3', ('Fb', 'Cb'):'m6', ('F#', 'G'):'m2',
			('C', 'F'):'P4', ('E', 'B'):'P5', ('Bb', 'A'):'M7', ('Gb', 'Ab'):'M2', ('D', 'Gb'):'d5',
			('G', 'Bb'):'m3', ('B', 'G'):'m6', ('Gb', 'Db'):'P5', ('Gb', 'D'):'d5', ('G', 'D#'):'A5',
			('C#', 'D'):'m2', ('C#', 'A'):'m6', ('Bb', 'D'):'M3'}
failed = []

for test in tests.keys():
	testValue = findInterval(test[0], test[1])
	if testValue != tests[test]:
		failed.append("Failed " + str(test) + ". Expected: " + tests[test] + " but got " + testValue)

for fail in failed:
	print fail

if len(failed) == 0:
	print "Passed all tests for findInterval."
else:
	print "Failed a total of " + str(len(failed)) + " tests."