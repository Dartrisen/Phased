import unittest
from scipy import io
from phased import Phased

class TestPython(unittest.TestCase):

    def __init__(self):

        self.path = 'test_cases/'
        self.name = 'python'

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

        super().__init__()

    def test(self):

        phased = Phased(**{item: self.mdict[item] for item in self.args1})
        result = phased.step(**{item: self.mdict[item] for item in self.args2})

        io.savemat('{}{}_test'.format(self.path, self.name), {self.name: result})

if __name__ == '__main__':

    test = TestPython()
    test.test()