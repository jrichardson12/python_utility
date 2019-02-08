#!/opt/local/bin/python3
# authon: John Richardson
#   desc: Opens a file and can move that file into a list.

import sys


def openFile(fileName, readWrite):
	try:
		file = open(fileName, readWrite)
		return file
	except Exception:
		print('Unable to open file')
		print(sys.exc_info())
		sys.exit(0)


def fileToArray(file):
	temp = []
	for line in file:
		line = line.replace('\n', '')
		line = line.strip()
		temp.append(line)
	return temp
