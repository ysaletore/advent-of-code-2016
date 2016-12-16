#!/usr/bin/env python

import sys;

def dragon(string):
	rstring = string[::-1].replace('0', 'X').replace('1','0').replace('X','1');
	return string + '0' + rstring;

def checksum(string):
	chksm = '';

	for i in range(len(string) / 2):
		if string[2 * i] == string[2 * i+1]:
			chksm += '1';
		else:
			chksm += '0';

	if len(chksm) % 2 == 0:
		return checksum(chksm);
	else:
		return chksm;

def day16(string, length):	
	while len(string) < length:
		string = dragon(string);

	string = string[0:length];
	print checksum(string);


def main(argv):
	string = '';
	length = 0;

	if len(argv) != 2:
		string = '01000100010010111';
		length = 35651584;
	else:
		string = argv[0];
		length = int(argv[1]);

	day16(string, length);

if __name__ == "__main__":
	main(sys.argv[1:]);
