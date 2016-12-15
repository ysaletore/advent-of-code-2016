#!/usr/bin/env python

import sys;
import re;

translator = {
	'first': 0,
	'second': 1,
	'third': 2,
	'fourth': 3
};

def day11(filename):
	with open(filename, 'r') as f:
		floors = {};
		for line in f:
			words = line.strip().split();
			if words[4] == 'nothing':
				continue;

			parts = line.strip().split(',');
			index = words[1];
			components = list();

			for part in parts:
				words = part.replace('.', '').split();
				print ' '.join(words[len(words)-2:]);
			
			

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day11(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
