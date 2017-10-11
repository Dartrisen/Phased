import unittest
from scipy import io
from phased import Phased

class PhasedTest(unittest.TestCase):

    def __init__(self):

        self.path = 'test_cases/'
        self.tests = [1, 2]
        self.name = 'received'

        self.args1 = [
                    'operating_frequency',
                    'sample_rate',
        ]
        self.args2 = [
                    'F',
                    'origin_pos',
                    'dest_pos',
                    'origin_vel',
                    'dest_vel',
        ]
        self.mdict = {
                    'operating_frequency':  3e8,
                    'sample_rate':          8e3,
                    'F':                    [1, 1, 1, 1, 1],
                    'origin_pos':           [1000, 0, 0],
                    'dest_pos':             [300, 200, 50],
                    'origin_vel':           [0, 0, 0],
                    'dest_vel':             [0, 0, 0],
        }
        phased = Phased()
        #io.savemat('{}input'.format(self.path), self.mdict)

    def test(self):

        #inputs = io.loadmat('{}{}'.format(self.path, 'input'))
        phased = Phased(**{item: self.mdict[item] for item in self.args1})
        received = phased.step(**{item: self.mdict[item] for item in self.args2})

        io.savemat('{}test'.format(self.path), {self.name: received})

if __name__ == '__main__':
    test = PhasedTest()
    test.test()
