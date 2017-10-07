__author__ = "UID_0"

class Phased(object):
	"""
	The phased modul narrowband signal propagation from one point to another in a free-space
	environment. The object applies range-dependent time delay, gain and phase shift to the
	input signal.
	"""
	def __init__(self, operating_frequency = 3e8, sample_rate = 1e6):

		cond1 = isinstance(operating_frequency, float)
		cond2 = isinstance(operating_frequency, int)
		try:
			if cond1 or cond2 :
				self.fop = float(operating_frequency)
			else:
				self.fop = 3e8
		except (TypeError, ValueError) as e:
			print(e)

		cond1 = isinstance(sample_rate, float)
		cond2 = isinstance(sample_rate, int)
		try:
			if cond1 or cond2:
				self.fs = float(sample_rate)
			else:
				self.fs = 1e6
		except (TypeError, ValueError) as e:
			print(e)
		
		super().__init__()

		self.origin_pos = []
		self.dest_pos = []

		self.origin_vel = []
		self.dest_vel = []

	def clear(self):

		self.origin_pos.clear()
		self.dest_pos.clear()

		self.origin_vel.clear()
		self.dest_vel.clear()

	def step(self, F, origin_pos = None, dest_pos = None, origin_vel = None, dest_vel = None):

		if (origin_pos == None):
			self.origin_pos = [0, 0, 0]
		elif (len(origin_pos) == 3 and isinstance(origin_pos, list)):
			try:
				for item in origin_pos:
					if (isinstance(item, float) or isinstance(item, int)):
						self.origin_pos = origin_pos
					else:
						self.origin_pos = [0, 0, 0]
			except (TypeError, ValueError) as e:
				print(e)
		else:
			self.origin_pos = [0, 0, 0]

		if (dest_pos == None):
			self.dest_pos = [0, 0, 0]
		elif (len(dest_pos) == 3 and isinstance(dest_pos, list)):
			try:
				for item in dest_pos:
					if (isinstance(item, float) or isinstance(item, int)):
						self.dest_pos = dest_pos
					else:
						self.dest_pos = [0, 0, 0]
			except (TypeError, ValueError) as e:
				print(e)
		else:
			self.dest_pos = [0, 0, 0]

		if (origin_vel == None):
			self.origin_vel = [0, 0, 0]
		elif (len(origin_vel) == 3 and isinstance(origin_vel, list)):
			try:
				for item in origin_vel:
					if (isinstance(item, float) or isinstance(item, int)):
						self.origin_vel = origin_vel
					else:
						self.origin_vel = [0, 0, 0]
			except (TypeError, ValueError) as e:
				print(e)
		else:
			self.origin_vel = [0, 0, 0]

		if (dest_vel == None):
			self.dest_vel = [0, 0, 0]
		elif (len(dest_vel) == 3 and isinstance(dest_vel, list)):
			try:
				for item in dest_vel:
					if (isinstance(item, float) or isinstance(item, int)):
						self.dest_vel = dest_vel
					else:
						self.dest_vel = [0, 0, 0]
			except (TypeError, ValueError) as e:
				print(e)
		else:
			self.dest_vel = [0, 0, 0]

def main():
	phased = Phased()

if __name__ == '__main__':
	main()
