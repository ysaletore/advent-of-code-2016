#!/usr/bin/env python

import sys;

def day01(filename):
	curr_loc = [0,0];
	curr_dir = 0;
	indexes = ['N', 'E', 'S', 'W'];

	travel = {
		'N': [0,1],		# N
		'E': [1,0],		# E
		'S': [0,-1],	# S
		'W': [-1,0]		# W
	};

	travelled = {
		'0,0': 1
	};

	with open(filename, 'r') as f:
		for line in f:
			line = line.rstrip();

			directions = line.split(',');
			directions = map(lambda X : X.lstrip().rstrip(), directions);

			for direction in directions:
				print "Current Location: " + str(curr_loc);
				print "Current Direction: " + str(indexes[curr_dir]);

				if direction[0] == "L": 			# turn left
					curr_dir = (curr_dir - 1) % 4;
				elif direction[0] == "R":			# turn right
					curr_dir = (curr_dir + 1) % 4;
				else:								# not right
					sys.exit("Something is wrong.");


				if travel[indexes[curr_dir]][0] != 0:
					for i in range(int(direction[1:])):
						print i;
						curr_loc[0] = curr_loc[0] + travel[indexes[curr_dir]][0];

						if str(curr_loc[0]) + ',' + str(curr_loc[1]) in travelled:
							print "Already visited here: " + str(curr_loc);
							print "Distance: " + str(abs(curr_loc[0]) + abs(curr_loc[1]));
							sys.exit();
						else:
							travelled[str(curr_loc[0]) + ',' + str(curr_loc[1])] = 1;
						
				elif travel[indexes[curr_dir]][1] != 0:
					for i in range(int(direction[1:])):
						curr_loc[1] = curr_loc[1] + travel[indexes[curr_dir]][1];

						if str(curr_loc[0]) + ',' + str(curr_loc[1]) in travelled:
							print "Already visited here: " + str(curr_loc);
							print "Distance: " + str(abs(curr_loc[0]) + abs(curr_loc[1]));
							sys.exit();
						else:
							travelled[str(curr_loc[0]) + ',' + str(curr_loc[1])] = 1;

				print "New instructions: " + str(direction);
				print "New heading: " + str(indexes[curr_dir]);
				print "New Location: " + str(curr_loc);
				print '\n';

		print "End: [" + str(curr_loc[0]) + ", " + str(curr_loc[1]) + "]";
		print "Distance: " + str(abs(curr_loc[0]) + abs(curr_loc[1]));

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day01(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
