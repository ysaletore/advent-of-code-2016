#!/usr/bin/env python

import sys;
import re;

def getDecompressedLen(string):
	length = 0;
	i = 0;
	while i < len(string):
		if string[i] == '(':
			paren = string.find(')', i);
			marker = map(int, string[i+1:paren].split('x'));
			repeat = string[paren+1:paren+1+marker[0]];

			sublength = 0;
			if re.search('(\d*x\d*)', repeat) != None:
				sublength = getDecompressedLen(repeat);
			else:
				sublength = len(repeat);

			length += sublength * marker[1];
			i = paren + 1 + marker[0];
		else:
			length += 1;
			i += 1;

	return length;

def day09(filename):
	with open(filename, 'r') as f:
		i = 0;
		paren = 0;

		decompressed = 0;
		for line in f:
			line = re.sub(r"[\s]", '', line.strip());
			decompressed += getDecompressedLen(line);
			
		print "Final decompressed length: " + str(decompressed);
def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day09(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
