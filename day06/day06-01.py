#!/usr/bin/env python

import sys;

def day06(filename):
	counters = list();

	with open(filename, 'r') as f:
		for line in f:
			line = line.strip();

			if len(counters) == 0:
				for i in range(len(line)):
					counters.append({});

			for i,char in enumerate(line):
				if char in counters[i]:
					counters[i][char] += 1;
				else:
					counters[i][char] = 1;

	message = '';
	for counter in counters:
		max_count = 0;
		max_char = '';

		for char,count in counter.iteritems():
			if count > max_count:
				max_count = count;
				max_char = char;

		message = message + max_char;

	print message;

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day06(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
