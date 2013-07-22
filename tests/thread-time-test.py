#!/usr/bin/python3
import sys
import threading
import time


class CallThreads(threading.Thread):

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
		method_name = 'run'
		self.target(*self.args)


def assigner():
	count = 0
	while True:
		print("while")
		count += 1
		w = CallThreads(worker, count)
		w.daemon = True
		w.start()
		time.sleep(3)


def worker(count):
	times = 0
	while True:
		times += 1
		print(str(count)+": "+str(times))
		time.sleep(1)


def main(args):
	assigner()


if __name__ == '__main__':
	main(sys.argv)
