#!/usr/bin/env python

import sys;
import hashlib;
import re;

def checkSoln(solutions, i):
	if solutions[i] != None:
		for letter in solutions[i]['t']:
			for j in xrange(i + 1, i + 1001):
				if solutions[j] != None:
					if letter in solutions[j]['q']:
						return letter;

	return None;
	

def day14(salt):
	solutions = list();
	keys = list();
	index = 0;

	while(len(keys) < 64):
		md5 = hashlib.md5(salt + str(index)).hexdigest();
		for i in xrange(2016):
			md5 = hashlib.md5(md5).hexdigest();
		triples = re.search(r'([a-z0-9])\1\1', md5);
		if triples:
			triples = triples.group(1);
		else:
			triples = None;

		solution = {
			't': triples,
			'q': re.findall(r'([a-z0-9])\1{4}', md5)
		};

		if solution['t'] or len(solution['q']) > 0:
			solutions.append(solution);
		else:
			solutions.append(None);

		if index >= 1005:
			letter = checkSoln(solutions, index - 1000);
			if letter != None:
				keys.append((index - 1000, md5));
		
		index += 1;

	print keys;

def main(argv):
	if len(argv) != 1:
		salt = "ahsbgdzn";
	else:
		salt = argv[0];

	day14(salt);

if __name__ == "__main__":
	main(sys.argv[1:]);
