#!/usr/bin/env python

import sys;
import re;

def day09(filename):
	with open(filename, 'r') as f:
		i = 0;
		paren = 0;

		decompressed = '';
		for line in f:
			line = re.sub(r"[\s]", '', line.strip());

			while i < len(line):
				if line[i] == '(':
					paren = line.find(')', i);
					marker = map(int, line[i+1:paren].split('x'));
					repeat = line[paren+1:paren+1+marker[0]];
	
					if len(repeat) >= marker[0]:
						for j in range(marker[1]):
							decompressed += repeat;
							print len(decompressed);
					
					i = paren + 1 + marker[0];
				else:
					decompressed += line[i];
					i += 1;

		print "Final decompressed length: " + str(len(decompressed));
def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day09(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
