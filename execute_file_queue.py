import queue
import threading


class ExecuteFileQueue(object):
	def __init__(self, file_name):
		self._file = file_name
		self.line_queue = queue.Queue()
		self.read_file()

	def read_file(self):
		file = open(self._file, encoding='utf-8')
		for line in file.readlines():
			self.line_queue.put(line.replace("\r", "").replace("\n", ""))

	def file_queue(self):
		return self.line_queue
