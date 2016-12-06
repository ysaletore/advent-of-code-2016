#!/usr/bin/env python

import sys;

def day03(filename):
	with open(filename, 'r') as f:
		counter = 0;
		valid = 0;
		for line in f:
			sides = map(lambda X : int(X.lstrip().rstrip()), line.split());


			counter = counter + 1;
			if sides[0] + sides[1] > sides[2] and  \
				sides[1] + sides[2] > sides[0] and \
				sides[2] + sides[0] > sides[1]:
				valid = valid + 1;

		print "Counter: " + str(counter);
		print "Valid: " + str(valid);

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day03(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
