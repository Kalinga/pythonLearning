import unittest
from assignments.assignment4 import reEmail

class RETest(unittest.TestCase):
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "RETest:setUp_:begin"
        ## do something...
        print "RETest:setUp_:end"

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "RETest:tearDown_:begin"
        ## do something...
        print "RETest:tearDown_:end"

    def test_Email1(self):
        print reEmail("Hari's email id is harigovind@in.google.com")
        self.assertTrue(reEmail("Hari's email id is harigovind@in.google.com") ==
                                "harigovind@in.goolge.com")

    def test_Email2(self):
        self.assertFalse(reEmail("This is an invalid email id is -invalid.mail@address.co.in") ==
                                "-invalid.mail@address.co.in")
    def test_dummy(self):
        self.assertTrue(True)

# For invocation from terminal
# python -m unittest reTest.RETest.test_Email1
if (__name__ == "__main__"):
    print "Unit test started: "
    unittest.main()