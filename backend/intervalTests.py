from interval import findInterval

# tests for findInterval
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

for fail in failed:
	print fail

if len(failed) == 0:
	print "Passed all " + str(len(tests.keys())) + " tests for findInterval."
else:
	print "Failed a total of " + str(len(failed)) + " tests."