'''
Created on Jul 29, 2015

@author: Mikhail
'''
import unittest
import os
from json_file_generator import MyOwnJSONProcessing as json_processing

class GenerateAndLoadJSONTestInitial(unittest.TestCase):

    def testGenerateAndLoadJSON(self):
        """
        The main point for such scenario is:
        1. The JSON file preparation should not be a part of the test.
           Test should be simple as much as possible - no another logic inside
        """
        file_name = "generate_and_load_unittest.json"
        expected_data = json_processing.generate_data_for_json_obj()
        json_processing.generate_json_file_with_data(file_name, expected_data)
        actual_data = json_processing.load_data_from_json_file(file_name)
        for exp_key, exp_value in expected_data.items():
            self.assertTrue(actual_data.has_key(exp_key), "Expected key '{}' has not been found in loaded json".format(exp_key))
            self.assertEquals(exp_value, actual_data.get(exp_key), "Dictionaries have different values '{}' for first and '{}' for second for the same key".format(exp_value, actual_data.get(exp_key)))
        # Second execution of the test can be failed because if we do not delete created file
        os.remove(file_name)


if __name__ == "__main__":
    # We can try to use different values for verbosity: 0, 1, 2
    unittest.main(verbosity=2)