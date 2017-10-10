__author__ = "UID_0"

import numpy as np
from scipy import constants
import itertools as it

class Phased(object):
	"""
	The phased modul narrowband signal propagation from one point to another in a free-space
	environment. The object applies range-dependent time delay, gain and phase shift to the
	input signal.
	"""
	def __init__(self, operating_frequency = 3e8, sample_rate = 8e3):

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
				self.fs = 8e3
		except (TypeError, ValueError) as e:
			print(e)

		self.c = 3e8
		
		super().__init__()

	def check(self, vec):

		if (vec == None):
			vec = [0, 0, 0]
		elif (len(vec) == 3 and isinstance(vec, list)):
			try:
				for item in vec:
					if (isinstance(item, float) or isinstance(item, int)):
						return vec
					else:
						vec = [0, 0, 0]
			except (TypeError, ValueError) as e:
				print(e)
		else:
			vec = [0, 0, 0]
		return vec

	def phase(self, t):

		phase = np.exp(-1j*2*constants.pi*self.fop*t)
		return phase

	def invLoss(self, t):

		invloss = np.power(4*constants.pi*self.fop*t, -2)
		return invloss

	def motion(self, origin_pos, dest_pos, origin_vel, dest_vel, t_max):

		def module(vec):

			return np.sqrt(sum([item**2 for item in vec]))

		distance = np.array([item1 - item2 for item1, item2 in zip(dest_pos, origin_pos)])
		velocity = np.array([item1 - item2 for item1, item2 in zip(dest_vel, origin_vel)])
		dt = 1/self.fs
		counter = it.count()
		next_counter = next(counter)

		while (next_counter < t_max):
			t = next_counter*dt
			r = distance + velocity*t
			yield next_counter, t, module(r)
			next_counter = next(counter)

	def step(self, F, origin_pos = None, dest_pos = None, origin_vel = None, dest_vel = None):
		'''
		T(t) = t(t)*exp(iw_0t) - the transmitted signal
		R(r) = r(r)*exp(iw_0t) - the received signal
		R(r) = s(t - R/c)*exp[i(w_0 + w_d)*(t - R/c)] where w_d is the dopler frequency
		w_d = w_0*(1 - v'/c cos(theta))
		cos(theta) - it is the angle between v' and R
		R - it is the distance between transmitter and receiver
		s(t - R/c) approx s(t) - s'(t)*R/c?
		'''
		origin_pos = self.check(origin_pos)
		dest_pos = self.check(dest_pos)
		origin_vel = self.check(origin_vel)
		dest_vel = self.check(dest_vel)

		transmitted = np.array(F, copy = False)
		received = np.empty_like(transmitted, dtype = np.complex)

		t_max = len(F)
		motion = self.motion(origin_pos, dest_pos, origin_vel, dest_vel, t_max)
		for counter, t, r in motion:
			tau = r/self.c
			if (tau > t):
				received[counter] = 0
			else:
				received[counter] = transmitted[counter]*self.phase(tau)*self.invLoss(tau)
		return received

def main():
	phased = Phased()
	R = phased.step([1, 1, 1, 1, 1], [1000, 0, 0], [300, 200, 50])
	print(R)

if __name__ == '__main__':
	main()
