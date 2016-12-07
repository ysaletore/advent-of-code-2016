#!/usr/bin/env python

import sys;
import string;

LETTERS = list(string.ascii_lowercase);

def day04(filename):
	with open(filename, 'r') as f:
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

			name = line[0:line.rfind('-')].replace('-', ' ');
			real_name = '';
			if encoded.startswith(code):
				for i in range(len(name)):
					if name[i] == ' ':
						real_name = real_name + ' ';
					else:
						idx = LETTERS.index(name[i]);
						real_name = real_name + LETTERS[(idx + sector) % 26];

				print str(sector) + ":\t" + real_name;

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day04(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
