from num2words import num2words
import re

cosmic_numbers = []

def next_number(x):
	written = re.sub(r'\W+', '', num2words(x).lower())
	if x == len(written):
		if not x in cosmic_numbers:
			cosmic_numbers.append(x)
	else:
		#print("%d is %d" % (x, len(written)))
		next_number(len(written))

for i in range(100000):
	#print("%d... " % i, end='')
	next_number(i)

print("Cosmic numbers: " + ", ".join([str(x) for x in cosmic_numbers]))