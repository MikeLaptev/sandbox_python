'''
Created on Jul 27, 2015

@author: Mikhail
'''
import unittest
import test_base

class test_0(test_base.BaseTest):
    '''
    This class is a wrapper for test class with id 0
    '''
    def test_0_execution(self):
        print self.getThreadInfo(), ">> ", self.testName() , "has been executed"

if __name__ == '__main__':
    unittest.main()