import io
import unittest
from contextlib import redirect_stdout
from unittest import result

from main import hottest_days, print_hottest_days, printer, to_celsius


class ContainersTestCase(unittest.TestCase):
    def setUp(self):
        self.response = io.StringIO()

    def test_printer(self):
        with redirect_stdout(self.response):
            printer(["Hello"])
            result = self.response.getvalue().strip()
            self.assertEqual(result, "Hello")

    def test_to_celsius(self):
        result = to_celsius([212])[0]
        self.assertAlmostEqual(result, 100)

    def test_hottest_days(self):
        result = hottest_days([32, 20, 33, 14, 50], 30)
        expected = [32, 33, 50]
        self.assertEqual(result, expected)

    def test_print_hottest_day(self):
        with redirect_stdout(self.response):
            print_hottest_days([10, 32, 45, 212], 150)
            result = float(self.response.getvalue().strip())
            self.assertAlmostEqual(result, 100)



if __name__ == "__main__":
    unittest.main()
