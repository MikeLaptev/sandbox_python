'''
Created on Jul 30, 2015

@author: Mikhail
'''
import unittest

def loadTestSuitesWithAllTestByDiscover():
    # pattern should be like a bash shell pattern matching
    example_of_loader = unittest.TestLoader()
    list_of_modules = example_of_loader.discover(".", "generate_and_load_unittest_update_[a-z][a-z][a-z].py")
    # Each module has type unittest.TestSuite
    # Lets run all these modules one by one
    for module in list_of_modules:
        actual_result = unittest.TestResult()
        print "<<< Launching of {} test cases >>>".format(module.countTestCases())
        module.run(actual_result)
        print "Launch statistic"
        print "No errors occur " if len(actual_result.errors) == 0 else "{} error(s) occurs".format(len(actual_result.errors))
        print "No skipped tests " if len(actual_result.skipped) == 0 else "{} test(s) has been skipped".format(len(actual_result.skipped))
        print "Run was successful " if actual_result.wasSuccessful() else "Run contains test that did not complete successfully"

def loadTestSuitesWithSelectedTestsByDiscover():
        # pattern should be like a bash shell pattern matching
    example_of_loader = unittest.TestLoader()
    list_of_modules = example_of_loader.discover(".", "generate_and_load_unittest_update_[a-z][a-z][a-z][a-z].py")
    # Each module has type unittest.TestSuite
    # Lets run all these modules one by one
    for module in list_of_modules:
        actual_result = unittest.TestResult()
        print "<<< Launching of {} test cases >>>".format(module.countTestCases())
        module.run(actual_result)
        print "Launch statistic"
        print "No errors occur " if len(actual_result.errors) == 0 else "{} error(s) occurs".format(len(actual_result.errors))
        print "No skipped tests " if len(actual_result.skipped) == 0 else "{} test(s) has been skipped".format(len(actual_result.skipped))
        print "Run was successful " if actual_result.wasSuccessful() else "Run contains test that did not complete successfully"

if __name__ == "__main__":
    loadTestSuitesWithAllTestByDiscover()
    loadTestSuitesWithSelectedTestsByDiscover()