#!/usr/bin/env python

import sys;
import hashlib;

def day05(input_string):
	LIMIT = 8;
	password = '';
	i = 0;

	while len(password) < LIMIT:
		new_hex = hashlib.md5(input_string + str(i)).hexdigest()

		if new_hex.startswith('00000'):
			password = password + new_hex[5];
		i = i + 1;

	print password;

def main(argv):
	if len(argv) != 1:
		input_string = "abbhdwsy";
	else:
		input_string = argv[0];

	day05(input_string);

if __name__ == "__main__":
	main(sys.argv[1:]);
