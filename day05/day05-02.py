#!/usr/bin/env python

import sys;
import hashlib;

def day05(input_string):
	LIMIT = 8;
	password = list();
	counter = 0;
	i = 0;

	for i in range(LIMIT):
		password.append('_');

	while counter < LIMIT:
		new_hex = hashlib.md5(input_string + str(i)).hexdigest()

		if new_hex.startswith('00000'):
			try:
				index = int(new_hex[5]);
				if index < LIMIT and password[index] == '_':
					counter = counter + 1;
					password[index] = new_hex[6];
			except ValueError:
				pass;
			
			sys.stdout.write('\r' + ''.join(password));
			sys.stdout.flush();

		i = i + 1;

	print '';
	print ''.join(password);

def main(argv):
	if len(argv) != 1:
		input_string = "abbhdwsy";
	else:
		input_string = argv[0];

	day05(input_string);

if __name__ == "__main__":
	main(sys.argv[1:]);
