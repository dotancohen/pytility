#!/usr/bin/python3

"""
Easily manipulate all tables of an SQL database

Curently only supports dropping tables
"""

import sys


def main():

	skip = ('rows in set', 'Tables_in_', '----',)

	print("Paste the output of 'show tables;' here then press Ctrl-D");
	data = sys.stdin.readlines()
	print("\n")

	for i in data:
		table = i[2:-2].strip()
		if table=='' or table.startswith(skip):
			continue
		print("drop table %s;" % table)

	print("\nshow tables;\n")



if __name__ == "__main__":

	main();
