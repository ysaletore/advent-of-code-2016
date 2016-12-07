#!/usr/bin/env python

import sys;

def getABAs(string):
	ABAs = list();
	if len(string) >= 3:
		for i in range(len(string)-2):
			if string[i] == string[i+2] and \
				string[i] != string[i+1]:
					ABAs.append(string[i:i+3]);

	return ABAs;

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

def flatten(l):
	return [item for sublist in l for item in sublist]

def day07(filename):
	counters = list();

	SSL_count = 0;
	with open(filename, 'r') as f:
		for line in f:
			line = line.strip();
			for aba in flatten(map(getABAs, getNonHypers(line))):
				bab = aba[1] + aba[0] + aba[1];
				if any(map(lambda X : bab in X, getHypers(line))):
					SSL_count = SSL_count + 1;
					break;

	print "SSL Count: " + str(SSL_count);

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day07(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
