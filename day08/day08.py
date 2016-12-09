#!/usr/bin/env python

import sys;

class Display(object):
	def __init__(self, i, j):
		self.x = i;
		self.y = j;
		self.display = list();

		for k in range(j):
			d2 = list();

			for l in range(i):
				d2.append(' ');
			self.display.append(d2);
	
	def rect(self, x, y):
		for i in range(x):
			for j in range(y):
				self.display[j][i] = '#';

	def rotateCol(self, index, amt):
		if index >= 0 and index < self.x and amt > 0:
			for i in range(amt):
				self._rotateCol(index);
		return;

		if index >= 0 and index < self.x and amt > 0:
			temp = list();

			for i in range(self.y):
				temp.append(self.display[(i-amt) % self.y][index]);

			for i in range(self.y):
				self.display[i][index] = temp[i];

	def _rotateCol(self, index):
		if index >= 0 and index < self.x:
			temp = self.display[self.y-1][index];

			for i in range(self.y - 1, 0, -1):
				self.display[i][index] = self.display[i-1][index];

			self.display[0][index] = temp;
		

	def rotateRow(self, index, amt):
		for i in range(amt):
			self._rotateRow(index);
		return;

		if index >= 0 and index < self.y and amt > 0:
			over = self.display[index][self.x-amt:self.x];
			left = self.display[index][0:self.x-amt];
			self.display[index] = over + left;

	def _rotateRow(self, index):
		if index >= 0 and index < self.y:
			temp = self.display[index][self.x - 1];
			for i in range(self.x - 1, 0, -1):
				self.display[index][i] = self.display[index][i-1];
			self.display[index][0] = temp;
		

	def __str__(self):
		return '\n'.join([''.join(row) for row in self.display]);

	def count(self):
		x = 0;
		for i in range(self.y):
			for j in range(self.x):
				if self.display[i][j] == '#':
					x += 1;

		return x;

def day08(filename):
	display = Display(50, 6);

	with open(filename, 'r') as f:
		for line in f:
			line = line.strip().split();

			if line[0] == 'rect':
				xy = line[1].split('x');
				display.rect(int(xy[0]), int(xy[1]));
			elif line[0] == 'rotate':
				amt = int(line[4]);
				if line[1] == 'row':
					row = int(line[2].split('y=')[1]);
					display.rotateRow(row,amt);
				elif line[1] == 'column':
					col = int(line[2].split('x=')[1]);
					display.rotateCol(col,amt);
				else:
					print "Usupported command: " + line;
			else:
				print "Usupported command: " + line;


	print display;
	print display.count();


def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day08(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
