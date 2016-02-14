from interval import findInterval

# some tests
tests = {('B', 'C'): 'm2', ('D#', 'G'): 'd4', ('C', 'B'): 'M7'}
failed = []

for test in tests.keys():
	testValue = findInterval(test[0], test[1])
	if testValue != tests[test]:
		failed.append("Failed " + str(test) + ". Expected: " + tests[test] + " but got " + testValue)

for fail in failed:
	print fail

if len(failed) == 0:
	print "Passed all tests."