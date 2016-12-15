#!/usr/bin/env python

import sys;
from collections import deque;
from collections import defaultdict;

class Node(object):
	def __init__(self, fav, x, y, dist):
		self.x = x;
		self.y = y;
		self.dist = dist;
		self.open = getOpen(fav, x, y);

def binary(num):
	string = '';
	if num < 2:
		return str(num);
	else:
		return binary(num / 2) + str(num % 2);

	return string;

def getOpen(fav, x, y):
	if x < 0 or y < 0:
		return False;

	num = binary(x*x + 3*x + 2*x*y + y + y*y + fav);
	if sum([int(i) for i in num]) % 2 == 0:
		return True;
	else:
		return False;

def none():
	return None;

def day13(fav):
	num = 0;
	for t_x in range(52):
		for t_y in range(52):
			start = Node(fav, 1, 1, 0);

			queue = deque();
			queue.append(start);
			nodes = defaultdict(lambda : defaultdict(lambda : None))
			nodes[1][1] = start;
			dist = 0;

			while len(queue) > 0 and dist <= 50:
				node = queue.popleft();
				x = node.x;
				y = node.y;
				dist = node.dist;

				if x == t_x and y == t_y and dist <= 50:
					print "Finished in " + str(dist) + " steps to (" + str(t_x) + ", " + str(t_y) + ").";
					num += 1;
					break;

				if nodes[x-1][y] == None:
					nodes[x-1][y] = Node(fav, x-1,y, dist+1);
					if nodes[x-1][y].open:
						queue.append(nodes[x-1][y]);
				if nodes[x][y-1] == None:
					nodes[x][y-1] = Node(fav, x,y-1, dist+1);
					if nodes[x][y-1].open:
						queue.append(nodes[x][y-1]);
				if nodes[x+1][y] == None:
					nodes[x+1][y] = Node(fav, x+1,y, dist+1);
					if nodes[x+1][y].open:
						queue.append(nodes[x+1][y]);
				if nodes[x][y+1] == None:
					nodes[x][y+1] = Node(fav, x,y+1, dist+1);
					if nodes[x][y+1].open:
						queue.append(nodes[x][y+1]);

	print "Able to finish within 50 steps from " + str(num) + " locations.";

def main(argv):
	if len(argv) != 3:
		fav = 1364;
	else:
		fav = int(argv[0]);

	day13(fav);

if __name__ == "__main__":
	main(sys.argv[1:]);
