#!/usr/bin/python3
import random
import threading
import time



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

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		pass



class Foo():
	population = 0
	def __init__(self, name):
		self.name = name
		self.killMe = False
		Foo.population += 1
		print("New Foo: "+name+" ("+str(Foo.population)+")")

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		pass

	def __del__(self):
		print (self.name + " terminated!")
		Foo.population -= 1


def NameCaller(o):
	while True:
		print(o.name)
		time.sleep(1)
		if o.killMe==True:
			return True

i = 0
while i<5:
	i += 1
	with Foo(str(i)) as f:
		print("Name: " + f.name)
		s = CallThreads(NameCaller, f)
		s.daemon = True
		s.start()
		time.sleep(3)
		f.killMe = True



"""
with Foo('dotan') as f:
	print("Name: " + f.name)
	spider = CallThreads(NameCaller, f)
	spider.daemon = True
	spider.start()
	time.sleep(10)
"""
