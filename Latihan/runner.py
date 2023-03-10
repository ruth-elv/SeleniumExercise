import unittest
from unittest.suite import TestSuite
import aRegister, bLogin, cCheckout

if __name__ == '__main__':
    # create test suite from classes
    suite = TestSuite()
    # panggil test
    tests = unittest.TestLoader()
    # menambahkan test ke suite
    suite.addTests(tests.loadTestsFromModule(aRegister))
    suite.addTests(tests.loadTestsFromModule(bLogin))
    suite.addTests(tests.loadTestsFromModule(cCheckout))

    #run test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)
