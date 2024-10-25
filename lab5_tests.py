import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.

    # Part 3
    def test_time_add_1(self):
        a = data.Time(4,40,45)
        b = data.Time(1,30,45)
        actual = lab5.time_add(a,b)
        expected = data.Time(6,11,30)
        self.assertEqual(actual,expected)

    def test_time_add_2(self):
        a = data.Time(20,30,4)
        b = data.Time(1,29, 56)
        actual = lab5.time_add(a,b)
        expected = data.Time(22,0,0)
        self.assertEqual(actual,expected)

    # Part 4
    def test_is_descending_1(self):
        nums = [39.4, 29.1, 24.3, -4, -40]
        actual = lab5.is_descending(nums)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_descending_2(self):
        nums = []
        actual = lab5.is_descending(nums)
        expected = None
        self.assertEqual(actual, expected)

    def test_is_descending_3(self):
        nums = [300,200,201,200,30,20,10,0]
        actual = lab5.is_descending(nums)
        expected = False
        self.assertEqual(actual, expected)

    # Part 5
    def test_largest_between_1(self):
        nums = [2,30,2,3,5,7,2,3,1]
        actual = lab5.largest_between(nums, 3,7)
        expected = 5
        self.assertEqual(actual, expected)

    def test_largest_between_2(self):
        nums = [2,30,2,3,5,7,2,3,1]
        actual = lab5.largest_between(nums, 7,3)
        expected = 5
        self.assertEqual(actual, expected)

    # Part 6
    def test_furthest_from_origin_1(self):
        points = [data.Point(2,1), data.Point(-30, -2),data.Point(20,0),
                  data.Point(3,1)]
        actual = lab5.furthest_from_origin(points)
        expected = 1
        self.assertEqual(actual, expected)

    def test_furthest_from_origin_2(self):
        points = [data.Point(2, 1), data.Point(30, 2), data.Point(20, 0),
                  data.Point(3, 1)]
        actual = lab5.furthest_from_origin(points)
        expected = 1
        self.assertEqual(actual, expected)

    def test_furthest_from_origin_3(self):
        points = []
        actual = lab5.furthest_from_origin(points)
        expected = None
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
