from UnitTestUtils import UnitTestUtils
import unittest

class TestGradeCalculation(unittest.TestCase):

    def setUp(self):
        self.utils = UnitTestUtils(self, __file__, "../grade.py")

    def test_grades(self):

        subtests = [
            (['10','10'],   '10 out of 10 is 100.0% (A)',   'perfect score'),
            (['20','16'],   '16 out of 20 is 80.0% (B)',    'lower bound B'),
            (['12','9'],    '9 out of 12 is 75.0% (C)',     'middle C'),
            (['13','8'],    '8 out of 13 is 61.5% (D)',     'round to 1 decimal'),
            (['100','90'],  '90 out of 100 is 90.0% (A)',   'lower bound A'),
            (['100','89'],  '89 out of 100 is 89.0% (B)',   'upper-bound B'),
            (['100','79'],  '79 out of 100 is 79.0% (C)',   'upper-bound C'),
            (['100','70'],  '70 out of 100 is 70.0% (C)',   'lower-bound C'),
            (['100','69'],  '69 out of 100 is 69.0% (D)',   'upper-bound D'),
            (['100','60'],  '60 out of 100 is 60.0% (D)',   'lower-bound D'),
            (['100','59'],  '59 out of 100 is 59.0% (F)',   'upper-bound F'),
            (['5','0'],     '0 out of 5 is 0.0% (F)',       'lower-bound F'),
            (['101','0'],   'INVALID',                      'too many questions'),
            (['0','0'],     'INVALID',                      'too few questions'),
            (['5','6'],     'INVALID',                      'more correct than questions'),
            (['-1','6'],    'INVALID',                      'negative questions'),
            (['5','-1'],    'INVALID',                      'negative correct'),
            (['five','5'],  'INVALID',                      'questions not a number'),
            (['5','five'],  'INVALID',                      'correct not a number'),
        ]

        for test in subtests:
            inputs = test[0]
            expected = test[1]
            description = test[2]
            with self.subTest(description):
                self.utils.check_one_contains(inputs, expected)

if __name__ == '__main__':
    unittest.main()
