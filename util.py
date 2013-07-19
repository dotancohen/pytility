#!/usr/bin/python3
import signal
import sys
import threading
import unicodedata



class CallThreads(threading.Thread):
	"""
	Auxiliary class used to provide arguments to threads

	@version 2013-07-19
	"""

	def __init__(self, target, *args):
		"""
		@type  target string
		@param target The name of the function to run as a thread

		@type  *args any
		@param *args The arguments to send to the function
		"""
		self.target = target
		self.args = args
		threading.Thread.__init__(self)


	def run (self):
		self.target(*self.args)



def filterCharacters(s):
	"""
	Strip non printable characters
	http://stackoverflow.com/a/93557/343302

	@version 2013-07-19

	@type  s dict|list|tuple|bytes|string
	@param s Object to remove non-printable characters from

	@rtype  dict|list|tuple|bytes|string
	@return An object that corresponds with the original object, nonprintable characters removed.
	"""

	validCategories = (
		'Lu', 'Ll', 'Lt', 'LC', 'Lm', 'Lo', 'L', 'Mn', 'Mc', 'Me', 'M', 'Nd', 'Nl', 'No', 'N', 'Pc',
		'Pd', 'Ps', 'Pe', 'Pi', 'Pf', 'Po', 'P', 'Sm', 'Sc', 'Sk', 'So', 'S', 'Zs', 'Zl', 'Zp', 'Z'
	)
	convertToBytes = False

	if isinstance(s, dict):
		new = {}
		for k,v in s.items():
			new[k] = filterCharacters(v)
		return new

	if isinstance(s, list):
		new = []
		for item in s:
			new.append(filterCharacters(item))
		return new

	if isinstance(s, tuple):
		new = []
		for item in s:
			new.append(filterCharacters(item))
		return tuple(new)

	if isinstance(s, bytes):
		s = s.decode('utf-8')
		convertToBytes = True

	if isinstance(s, str):
		s = ''.join(c for c in s if unicodedata.category(c) in validCategories)
		if convertToBytes:
			s = s.encode('utf-8')
		return s

	else:
		return None



def signal_handler(signal, frame):
	"""
	Handle signal interrupts.

	@version 2013-07-19
	"""
	print ("Got signal: " + str(signal))
	sys.exit(0)

