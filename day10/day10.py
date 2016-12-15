#!/usr/bin/env python

import sys;
import re;

class Output(object):
	def __init__(self, outputId):
		self.id = outputId;
		self.values = list();

	def rec(self, value):
		self.values.append(value);

	def __str__(self):
		return "Output " + self.id + ": " + str(self.values);

class Bot(Output):
	def __init__(self, botId):
		self.id = botId;
		self.values = list();

	def setLow(self, low):
		self.low = low;

	def setHigh(self, high):
		self.high = high;

	def len(self):
		return len(self.values);

	def rules(self):
		if len(self.values) >= 2:
			low_val = min(self.values);
			high_val = max(self.values);
			self.values.remove(low_val);
			self.values.remove(high_val);

			print "Bot " + self.id + " compared " + str(low_val) + " to " + str(high_val) + ".";

			self.low.rec(low_val);
			self.high.rec(high_val);

	def rec(self, value):
		self.values.append(value);
		if len(self.values) >= 2:
			self.rules();

	def __str__(self):
		return self.bodId + " " + str(self.values);

def day10(filename):
	with open(filename, 'r') as f:
		outputs = dict();
		bots = dict();
		values = list();
		for line in f:
			line = line.strip().split();

			if line[0] == 'bot':
				bot = line[1];

				if bot not in bots:
					bots[bot] = Bot(bot);

				bot = bots[bot];

				low = line[6];
				if line[5] == 'bot':
					if low not in bots:
						bots[low] = Bot(low);
					bot.setLow(bots[low]);

				elif line[5] == 'output':
					if low not in outputs:
						outputs[low] = Output(low);
					bot.setLow(outputs[low]);

				high = line[11];
				if line[10] == 'bot':
					if high not in bots:
						bots[high] = Bot(high);
					bot.setHigh(bots[high]);
				elif line[10] == 'output':
					if high not in outputs:
						outputs[high] = Output(high);
					bot.setHigh(outputs[high]);
				
			elif line[0] == 'value':
				value = int(line[1]);
				botId = line[5];
				values.append((botId, value));

		for value in values:
			print "Giving bot " + value[0] + " value " + str(value[1]);
			bots[value[0]].rec(value[1]);
			
		for idx,output in outputs.iteritems():
			print output;

def main(argv):
	if len(argv) != 1:
		filename = "input";
	else:
		filename = argv[0];

	day10(filename);

if __name__ == "__main__":
	main(sys.argv[1:]);
