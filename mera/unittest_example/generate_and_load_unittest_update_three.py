'''
Created on Jul 29, 2015

@author: Mikhail
'''
import unittest
from json_file_generator import MyOwnJSONProcessing as json_processing
from json_file_generator import __version__ as json_file_generator_version
import re
from unittest.case import skip, skipIf

class GenerateAndLoadJSONTestUpdateThree(unittest.TestCase):
    
    expected_data = {}

    @classmethod
    def setUpClass(cls):
        print "{} for {} has been called".format(cls.setUpClass.__name__, cls.__name__)
        cls.expected_data = json_processing.generate_data_for_json_obj()

    def setUp(self):
        print "{} for {} has been called".format(self.setUp.__name__, self._testMethodName)
        self.file_name = "generate_and_load_unittest.json"
        self.original_name = json_processing.generate_json_file_with_data(self.file_name, self.expected_data)

    def tearDown(self):
        print "{} for {} has been called".format(self.tearDown.__name__, self._testMethodName)

    @classmethod
    def tearDownClass(cls):
        print "{} for {} has been called".format(cls.tearDownClass.__name__, cls.__name__)
        json_processing.clean_up()

    def testGenerateAndLoadJSONValidKeys(self):
        print "Processing file {}".format(self.original_name)
        actual_data = json_processing.load_data_from_json_file(self.original_name)
        for exp_key in self.expected_data.keys():
            self.assertTrue(actual_data.has_key(exp_key), "Expected key '{}' has not been found in loaded json".format(exp_key))
    
    # general version of skip
    @skip("old functionality")
    def testGenerateAndLoadJSONValidKeysHasOnlyLetter1(self):
        print "Processing file {}".format(self.original_name)
        actual_data = json_processing.load_data_from_json_file(self.original_name)
        for act_key in actual_data.keys():
            self.assertTrue(re.match("[^a-zA-Z]", act_key) is None, "Key should contains only alpha symbols: {}".format(act_key))

    # version of skip that check version of our json_file_generator
    @skipIf(json_file_generator_version > 1, "This functionality is not supported in this version on the json file generator")
    def testGenerateAndLoadJSONValidKeysHasOnlyLetter2(self):
        print "Processing file {}".format(self.original_name)
        actual_data = json_processing.load_data_from_json_file(self.original_name)
        for act_key in actual_data.keys():
            self.assertIsNone(re.match("[^a-zA-Z]", act_key), "Key should contains only alpha symbols: {}".format(act_key))

    def testGenerateAndLoadJSONValidValues(self):
        print "Processing file {}".format(self.original_name)
        actual_data = json_processing.load_data_from_json_file(self.original_name)
        for exp_key, exp_value in self.expected_data.items():
            self.assertEquals(exp_value, actual_data.get(exp_key), "Dictionaries have different values '{}' for first and '{}' for second for the same key".format(exp_value, actual_data.get(exp_key)))

if __name__ == "__main__":
    unittest.main(verbosity=2)