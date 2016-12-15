#!/usr/bin/env python

import sys;

def day15(filename):
	discs = list();
	with open(filename, 'r') as f:
		i = 1;
		for line in f:
			line = line.strip().replace('.', '').split();
			disc = {
				'i': i,
				'n': int(line[3]),
				'x': int(line[11])
			}
			discs.append(disc);
			i += 1;

		# hack for part 2
		discs.append({'i': 7, 'n': 11, 'x': 0})

		t = 0;
		keepGoing = True;
		while keepGoing:
			keepGoing = False;
			for disc in discs:
				if ((disc['x'] + t + disc['i']) % disc['n']) != 0:
					keepGoing = True;
					break;

			if keepGoing:
				t += 1;

		print t;

		for disc in discs:
			a = (disc['x'] + t) % disc['n'];

def main(argv):
	if len(argv) != 1:
		filename = 'input';
	else:
		filename = argv[0];

	day15(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
