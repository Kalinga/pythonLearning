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
        print reEmail("Hari's email id is harigovind@in.bosch.com")
        self.assertTrue(reEmail("Hari's email id is harigovind@in.bosch.com") ==
                                "harigovind@in.bosch.com")

    def test_Email2(self):
        self.assertFalse(reEmail("This is an invalid email id is -invalid.mail@address.co.in") ==
                                "-invalid.mail@address.co.in")
    def test_dummy(self):
        self.assertTrue(True)

if (__name__ == "__main__"):
    print "Unit test started: "
    unittest.main()