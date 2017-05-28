#!/usr/bin/python3

"""
Easily manipulate all tables of an SQL database
"""

import sys


def main(action):

	actions = ['drop', 'truncate']

	if action == None:
		action = actions[0]

	if action not in actions:
		print("Not a legal action: " + action)
		print("Legal actions:")
		print(actions)
		return False

	skip = ('rows in set', 'Tables_in_', '----',)

	print("Paste the output of 'show tables;' here then press Ctrl-D");
	data = sys.stdin.readlines()
	print("\n")

	for i in data:
		table = i[2:-2].strip()
		if table=='' or table.startswith(skip):
			continue
		print("%s table %s;" % (action, table, ))

	print("\nshow tables;\n")



if __name__ == "__main__":

	action = None

	if len(sys.argv)>1:
		action = sys.argv[1]

	main(action);
