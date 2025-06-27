"""
Created on Jul 29, 2015

@author: Mikhail
"""

import unittest
import os
from .json_file_generator import MyOwnJSONProcessing as json_processing


class GenerateAndLoadJSONTestUpdateOne(unittest.TestCase):

    def setUp(self):
        print(
            (
                "{} for {} has been called".format(
                    self.setUp.__name__, self._testMethodName
                )
            )
        )
        self.file_name = "generate_and_load_unittest.json"
        self.expected_data = json_processing.generate_data_for_json_obj()

    def tearDown(self):
        print(
            (
                "{} for {} has been called".format(
                    self.tearDown.__name__, self._testMethodName
                )
            )
        )
        # Second execution of the test can be failed because if we do not delete created file
        os.remove(self.file_name)

    def testGenerateAndLoadJSONValidKeys(self):
        original_name = json_processing.generate_json_file_with_data(
            self.file_name, self.expected_data
        )
        print(("Processing file {}".format(original_name)))
        actual_data = json_processing.load_data_from_json_file(original_name)
        for exp_key in list(self.expected_data.keys()):
            self.assertTrue(
                exp_key in actual_data,
                "Expected key '{}' has not been found in loaded json".format(exp_key),
            )
        for act_key in list(actual_data.keys()):
            self.assertTrue(
                act_key in self.expected_data,
                "Loaded key '{}' has not been found in dumped json".format(act_key),
            )

    def testGenerateAndLoadJSONValidValues(self):
        original_name = json_processing.generate_json_file_with_data(
            self.file_name, self.expected_data
        )
        print(("Processing file {}".format(original_name)))
        actual_data = json_processing.load_data_from_json_file(original_name)
        for exp_key, exp_value in list(self.expected_data.items()):
            self.assertEqual(
                exp_value,
                actual_data.get(exp_key),
                "Dictionaries have different values '{}' for first and '{}' for second for the same key".format(
                    exp_value, actual_data.get(exp_key)
                ),
            )
        for act_key, act_value in list(actual_data.items()):
            self.assertEqual(
                act_value,
                self.expected_data.get(act_key),
                "Dictionaries have different values '{}' for first and '{}' for second for the same key".format(
                    act_value, self.expected_data.get(act_key)
                ),
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
