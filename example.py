#!/usr/bin/python3

"""
Examples of common Python syntax and techniques
"""



# IMPORTS

import sys
from pprint import pprint

# SMART IMPORTS

try:
	import json
except:
	import simplejson as json

# IMPORT FROM 'lib' DIRECTORY
libdir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'lib'
sys.path.insert(0, libdir)

import file_in_lib_directory



# SET CLI PARAMETERS

try:
	if sys.argv[1] == 'debug':
		debug = True
	else:
		debug = False
except:
	debug = False



# CLASSES

class Some_Class(object):
	"""
	Describe a generic Python class
	"""

	population = 0

	def __init__(self, name):
		# Instance methods must have 'self' as first argument
		self.name = name

		# Static properties are accessed by class name
		# No increment urinary operator in Python!
		Some_Class.population += 1

	def set_name(self, name):
		self.name = name
		return True

	def get_name(self):
		return self.name

	def get_population()
		# Static methods do not have 'self' as first argument
		return Some_Class.population

	def __del__(self):
		Some_Class.population -= 1



# METHODS

def print_name(name):
	"""
	Describe a generic Python method

	@type  name string
	@param name The name to print

	@rtype  bool
	@return Returns True on success, False on failure
	"""

	try:
		print(name)

	except TypeError as error:
		# Catch only the type of error expected, never the generic 'Exception'
		log(error)
		return False

	return True



# SETTING THE MAIN() METHOD

def main(args):
	"""
	Main body of application.

	@type  args list
	@param args List of strings presented as CLI arguments
	"""

	print_name(args[1])
	return True


if __name__ == '__main__':
	main(sys.argv)
