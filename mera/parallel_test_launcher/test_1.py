'''
Created on Jul 27, 2015

@author: Mikhail
'''
import unittest
import test_base
import time

class test_1(test_base.BaseTest):
    '''
    This class is a wrapper for test class with id 1
    '''
    def test_1_execution(self):
        print self.getThreadInfo(), ">> Execution of", self.testName() , "has been started"
        time.sleep(1)
        print self.getThreadInfo(), ">> Execution of", self.testName() , "has been completed"

if __name__ == '__main__':
    unittest.main()