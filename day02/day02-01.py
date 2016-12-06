#!/usr/bin/env python

import sys;

def day02(filename):
	keypad = [
		[7,8,9],
		[4,5,6],
		[1,2,3]
	]

	x = 1;
	y = 1;

	with open(filename, 'r') as f:
		for line in f:
			line = line.rstrip();
			for i in range(len(line)):
				direction = line[i];

				if direction == 'U':
					y = min(2, y + 1);
				elif direction == 'D':
					y = max(0, y - 1);
				elif direction == 'L':
					x = max(0, x - 1);
				elif direction == 'R':
					x = min(2, x + 1);
				else:
					sys.exit("Something went wrong");

			print keypad[y][x];

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day02(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
