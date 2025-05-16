from UnitTestUtils import UnitTestUtils
import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.utils = UnitTestUtils(self, __file__, "../calculator.py")

    def test_calculations(self):

        subtests = [
            ( ['5','6','+'],            '5.0 + 6.0 = 11.0', '' ),
            ( ['10','2','/'],           '10.0 / 2.0 = 5.0', '' ),
            ( ['5','6','x'],            '5.0 x 6.0 = 30.0', '' ),
            ( ['1.1','.2','-'],         '1.1 - 0.2 = 0.9', '' ),
            ( ['3.0','2.0','+'],        '3.0 + 2.0 = 5.0', '' ),
            ( ['-4','3','x'],           '-4.0 x 3.0 = -12.0', '' ),
            ( ['8','-10','+'],          '8.0 + -10.0 = -2.0', '' ),
            ( ['-6.6','-3','/'],        '-6.6 / -3.0 = 2.2', '' ),
            ( ['4','3','/'],            '4.0 / 3.0 = 1.3333', '' ),
            ( ['4','0','x'],            '4.0 x 0.0 = 0.0', '' ),
            ( ['4','0','/'],            '4.0 / 0.0 = ERROR', '' ),
            ( ['2.02468','2.00000','/'],'2.0247 / 2.0 = 1.0124', '' ),
            ( ['two','',''],            'INVALID NUMBER', '' ),
            ( ['10','two',''],          'INVALID NUMBER', '' ),
            ( ['3.5','2.0','*'],        'INVALID OPERATOR', '' ),
            ( ['175','232','times'],    'INVALID OPERATOR', '' ),
        ]

        for test in subtests:
            inputs = test[0]
            expected = test[1]
            description = test[2]
            with self.subTest(description):
                self.utils.check_one_equals(inputs, expected)

if __name__ == '__main__':
    unittest.main()
