#!/usr/bin/env python

import sys;

def day04(filename):
	with open(filename, 'r') as f:
		total = 0;
		for line in f:
			line = line.strip();
			code = line[(line.find('[')+1):(line.find(']'))];
			sector = int(line[(line.rfind('-')+1):line.find('[')]);
			name = line[0:line.rfind('-')].replace('-', '');

			counts = {};
			for char in name:
				if char in counts:
					counts[char] = counts[char] + 1;
				else:
					counts[char] = 1;

			# make a reverse dict going from counts to chars
			rev_counts = {};
			for char,count in counts.iteritems():
				if count in rev_counts:
					rev_counts[count].append(char);
				else:
					rev_counts[count] = list(char);

			# reverse sort its keys
			rev_sorted_counts = sorted(rev_counts.keys(), reverse = True);
			encoded = '';
			for i in range(len(rev_sorted_counts)):
				encoded = encoded + ''.join(sorted(rev_counts[rev_sorted_counts[i]]));

			if encoded.startswith(code):
				total = total + sector;

		print total;

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day04(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
