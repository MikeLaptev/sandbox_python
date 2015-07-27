'''
Created on Jul 27, 2015

@author: Mikhail
'''
import unittest
import test_base
import time

class test_2(test_base.BaseTest):
    '''
    This class is a wrapper for test class with id 2
    '''
    def test_2_execution(self):
        print self.getThreadInfo(), ">> Execution of", self.testName() , "has been started"
        time.sleep(2)
        print self.getThreadInfo(), ">> Execution of", self.testName() , "has been completed"

if __name__ == '__main__':
    unittest.main()