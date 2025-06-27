"""
Created on Jul 27, 2015

@author: Mikhail
"""

import unittest
import threading


class BaseTest(unittest.TestCase):

    def getThreadIdent(self):
        return threading.current_thread().ident

    def getThreadName(self):
        return threading.current_thread().getName()

    def getThreadInfo(self):
        return "[ " + str(self.getThreadIdent()) + " ] " + self.getThreadName()

    def setUp(self):
        threading.current_thread().setName(self.testName())
        print(
            (
                "\n",
                self.getThreadInfo(),
                ">> Pre-processing of test",
                self.testName(),
                "has been started",
            )
        )

    def tearDown(self):
        print(
            (
                self.getThreadInfo(),
                ">> Post-processing of test",
                self.testName(),
                "has been completed",
            )
        )

    def testName(self):
        return self.__class__.__name__
