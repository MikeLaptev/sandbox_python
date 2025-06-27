"""
Created on Jul 27, 2015

@author: Mikhail
"""

import unittest
from . import test_base
import time


class test_4(test_base.BaseTest):
    """
    This class is a wrapper for test class with id 4
    """

    def test_4_execution(self):
        print(
            (
                self.getThreadInfo(),
                ">> Execution of",
                self.testName(),
                "has been started",
            )
        )
        time.sleep(4)
        print(
            (
                self.getThreadInfo(),
                ">> Execution of",
                self.testName(),
                "has been completed",
            )
        )


if __name__ == "__main__":
    unittest.main()
