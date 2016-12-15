#!/usr/bin/env python

import sys;
import re;

def day12(filename):
	registers = {'c': 1};
	instructions = list();
	with open(filename, 'r') as f:
		for line in f:
			instructions.append(line.strip());

	index = 0;
	length = len(instructions);

	while index < length:
		line = instructions[index];
		parts = line.split();

		if parts[0] == 'cpy':
			try:
				registers[parts[2]] = int(parts[1]);
			except ValueError:
				if parts[1] not in registers:
					registers[parts[1]] = 0;

				registers[parts[2]] = registers[parts[1]];
		elif parts[0] == 'inc':
			if parts[1] not in registers:
				registers[parts[1]] = 0;
			registers[parts[1]] += 1;
		elif parts[0] == 'dec':
			if parts[1] not in registers:
				registers[parts[1]] = 0;
			registers[parts[1]] -= 1;

		if parts[0] == 'jnz':
			try:
				if int(parts[1]) != 0:
					index += int(parts[2]);
			except ValueError:
				if parts[1] in registers and registers[parts[1]] != 0: 
					index += int(parts[2]);
				else:
					index += 1;
		else:
			index += 1;

	print registers;
			

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day12(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
