#!/usr/bin/env python

import sys;
from collections import defaultdict;
from collections import deque;
import itertools;

# data['cog'], data['pog'], data['prg'], data['rug'], data['thg']
# data['com'], data['pom'], data['prm'], data['rum'], data['thm']

class Node(object):
	def __init__(self, e, data, moves):
		self.e = e;
		self.data = dict(data);
		self.moves = moves;

		self.valid = True;

		if e < 0 or e > 3:
			self.valid = False;

		if data['com'] != data['cog'] and (data['com'] == data['pog'] or data['com'] == data['prg'] or data['com'] == data['rug'] or data['com'] == data['thg']):
			self.valid = False;	

		if self.valid and data['pom'] != data['pog'] and (data['pom'] == data['cog'] or data['pom'] == data['prg'] or data['pom'] == data['rug'] or data['pom'] == data['thg']):
			self.valid = False;	

		if self.valid and data['prm'] != data['prg'] and (data['prm'] == data['pog'] or data['prm'] == data['cog'] or data['prm'] == data['rug'] or data['prm'] == data['thg']):
			self.valid = False;	

		if self.valid and data['rum'] != data['rug'] and (data['rum'] == data['pog'] or data['rum'] == data['prg'] or data['rum'] == data['cog'] or data['rum'] == data['thg']):
			self.valid = False;	

		if self.valid and data['thm'] != data['thg'] and (data['thm'] == data['pog'] or data['thm'] == data['prg'] or data['thm'] == data['rug'] or data['thm'] == data['cog']):
			self.valid = False;	

		self.success = False;
		if all([data[i] == 3 for i in data]):
			self.success = True;

	def __str__(self):
		return "Valid: " + str(self.valid) + ", E: " + str(self.e) + " " + str(self.data) + " in " + str(self.moves) + " moves.";

def day11():
	tree = lambda: defaultdict(tree);
	data = {
		'pog': 0,
		'thg': 0,
		'thm': 0,
		'prg': 0,
		'rug': 0,
		'rum': 0,
		'cog': 0,
		'com': 0,
		'pom': 1,
		'prm': 1
	}

	start = Node(0, data, 0);
	states = tree();
	states[0][data['pog']][data['thg']][data['thm']][data['prg']][data['rug']][data['rum']][data['cog']][data['com']][data['pom']][data['prm']] = start;
	queue = deque();
	queue.append(start);
	
	while len(queue) > 0:
		node = queue.popleft();
		print node;

		# check if this is the final state:
		if node.success:
			print "SUCCESS: " + str(node);
			break;

		# get items we can currently take
		items = list();
		for key,val in node.data.iteritems():
			if val == node.e:
				items.append(key);

		# check both directions
		for e2 in range(node.e - 1, node.e + 2, 2):
			# ensure in valid direction
			if e2 >= 0 or e2 < 4:
				# test with moving 1 or 2 items
				for j in range(2):
					# iterate over all combinations
					for item in itertools.combinations(items, j+1):
						# make copy of data dict
						data = dict(node.data);

						for it in item:
							data[it] = e2;

						if type(states[e2][data['pog']][data['thg']][data['thm']][data['prg']][data['rug']][data['rum']][data['cog']][data['com']][data['pom']][data['prm']]) != Node:
							n2 = Node(e2, data, node.moves + 1);
							states[e2][data['pog']][data['thg']][data['thm']][data['prg']][data['rug']][data['rum']][data['cog']][data['com']][data['pom']][data['prm']] = n2;
		
							if n2.valid:
								queue.append(n2);

def main(argv):
	day11();

if __name__ == "__main__":
	main(sys.argv[1:]);
