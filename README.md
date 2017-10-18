# Phased
Signal propagation from one point to another in a free-space environment.
* Doppler effect
* Time delay
* Phase shift
***
Call step to propagate the signal through a free space environment

```python
from phased import Phased
instance = Phased()
F = [1, 2, 3, 4, 5]
R = instance.step(F, [1000, 0, 0], [300, 200, 50])
```
***
test_python.py generate test_python.mat file\\
test_matlab.py compare test_python.mat and test_matlab.mat files
***
origin_pos, dest_pos, origin_vel, dest_vel:
__________________________________________
	List of 3 elements like [1, 2, 3]
	positions and velocities of radar and target

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
	Default: 8e3
Methods:
_______
	step:
	Propagate signal from one location to another
