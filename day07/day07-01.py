#!/usr/bin/env python

import sys;

def getHypers(string):
	i = 0;
	nonhypers = list();
	while(string.find(']', i) >= i):
		nonhypers.append(string[string.find('[', i)+1:string.find(']', i)]);
		i = string.find(']', i) + 1;
		

	return nonhypers;


def getNonHypers(string):
	i = 0;
	nonhypers = list();
	while(string.find('[', i) >= i):
		nonhypers.append(string[i:string.find('[', i)]);
		i = string.find(']', i) + 1;
	
	nonhypers.append(string[i:len(string)]);

	return nonhypers;

def hasABBA(string):
	if len(string) >= 4:
		for i in range(len(string)-3):
			if string[i] == string[i+3] and \
				string[i+1] == string[i+2] and \
				string[i] != string[i+1]:
					return True;

	return False;

def day07(filename):
	counters = list();

	TLS_count = 0;
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip();
			if any(map(hasABBA, getNonHypers(line))) and not any(map(hasABBA, getHypers(line))):
				TLS_count = TLS_count + 1;

	print "TLS Count: " + str(TLS_count);

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day07(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
