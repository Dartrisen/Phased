# Phased
Signal propagation from one point to another in a free-space environment.

PropagationSpeed:
________________
	Signal propagation speed.
  	Specify signal wave propagation speed in free space as a real positive scalar. Units are meters per second.
  	Default: Speed of light

OperatingFrequency:
__________________
	Signal carrier frequency
  	A scalar containing the carrier frequency of the narrowband signal. Units are hertz.
  	Default: 3e8
SampleRate:
__________
	Sample rate
	A scalar containing the sample rate. Units of sample rate are hertz.
	The algorithm uses this value to determine the propagation delay in number of samples.
	Default: 1e6
Methods:
_______
	step:
	Propagate signal from one location to another
