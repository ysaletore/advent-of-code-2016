#!/usr/bin/env python

import sys;
import re;

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
		min_count = 1000000;
		min_char = '';

		for char,count in counter.iteritems():
			if count < min_count:
				min_count = count;
				min_char = char;

		message = message + min_char;

	print message;

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day06(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
