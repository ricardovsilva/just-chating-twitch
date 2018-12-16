import unittest

from assertpy import assert_that

from chronal_calibrator import ChronalCalibrator

class ChronalCalibratorTest(unittest.TestCase):

    def setUp(self):
        self.target = ChronalCalibrator()

    def test__calibrate__empty_string__throws_error(self):
        assert_that(self.target.calibrate).raises(Exception).when_called_with("")
        
    def test__calibrate__non_valid_number__throws_error(self):
        assert_that(self.target.calibrate).raises(Exception).when_called_with("foo")

    def test__calibrate__with_positive_numbers__should_sum_the_numbers(self):
        assert_that(self.target.calibrate("+5, +10")).is_equal_to(15)

    def test__calibrate__with_negative_numbers__should_sum_the_numbers(self):
        assert_that(self.target.calibrate("-5, -10")).is_equal_to(-15)

    def test__calibrate__with_mixed_numbers__should_sum_the_numbers(self):
        assert_that(self.target.calibrate("-5, +10, -7")).is_equal_to(-2)


if __name__ == '__main__':
    unittest.main()