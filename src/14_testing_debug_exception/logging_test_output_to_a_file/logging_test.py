import unittest

# A simple function to illustrate
def parse_int(s):
    return int(s)

class TestConversion(unittest.TestCase):
    # Testing that an exception gets raised
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, "N/A")

    # Testing an exception plus regex on exception message
    def test_bad_int_msg(self):
        self.assertRaisesRegex(ValueError, 'invalid literal .*', parse_int, 'N/A') 

# Example of testing an exception along with inspection of exception instance
import errno

class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('/file/not/found')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail("IOError not raised") 

import sys
def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)

if __name__ == '__main__':
    with open('testing.out', 'w') as f:
        main(f)
