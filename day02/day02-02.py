#!/usr/bin/env python

import sys;

def day02(filename):
	keypad = [
		[0,0,'D',0,0],
		[0,'A','B','C',0],
		[5,6,7,8,9],
		[0,2,3,4,0],
		[0,0,1,0,0]
	]

	x = 0;
	y = 2;

	with open(filename, 'r') as f:
		for line in f:
			line = line.rstrip();
			for i in range(len(line)):
				direction = line[i];

				if direction == 'U':
					y_ = min(4, y + 1);
					if keypad[y_][x] != 0:
						y = y_;
				elif direction == 'D':
					y_ = max(0, y - 1);
					if keypad[y_][x] != 0:
						y = y_;
				elif direction == 'L':
					x_ = max(0, x - 1);
					if keypad[y][x_] != 0:
						x = x_;
				elif direction == 'R':
					x_ = min(4, x + 1);
					if keypad[y][x_] != 0:
						x = x_;
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
