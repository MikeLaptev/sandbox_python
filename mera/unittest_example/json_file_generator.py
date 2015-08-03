'''
Created on Jul 29, 2015

@author: Mikhail
'''
import json
import random
import string
import time
import os

__version__ = 2.0

class MyOwnJSONProcessing:
    
    # variables for amount of objects in dictionary (for json)
    min_len_of_json_dict = 1
    max_len_of_json_dict = 5
    # variables for max and min length of keys in dictionary (for json)
    min_len_of_key = 1
    max_len_of_key = 10
    # variable for max value in dictionary (for json)
    max_value = 100
    
    @classmethod
    def generate_set_of_files_with_json_obj(cls, amount_of_files, is_data_complicated = False):
        for dummy_i in xrange(amount_of_files):
            if not is_data_complicated:
                # we will generate simple data for json file
                cls.generate_json_file_with_data(data = cls.generate_data_for_json_obj())
            else:
                # lets try to generate more complicated data for json file
                cls.generate_json_file_with_data(data = cls.generate_complicated_data_for_json_obj())
    
    @classmethod
    def generate_data_for_json_obj(cls):
        json_data = {}
        # generating random key
        for dummy_i in range(random.randrange(cls.min_len_of_json_dict, cls.max_len_of_json_dict)):
            new_key = cls.randomword(random.randrange(cls.min_len_of_key, cls.max_len_of_key))
            new_value = random.randrange(cls.max_value)
            if not json_data.has_key(new_key):
                json_data[new_key] = new_value
                
        return json_data

    @classmethod
    def generate_complicated_data_for_json_obj(cls):
        raise NotImplementedError

    @staticmethod
    def generate_json_file_with_data(file_name_template = "data_<timestamp>.json", data = {}):
        """
        By default this function generates json file with name that contains time-stamp 
        when it has been generated
        """
        file_name_id = 0
        file_name = string.replace(file_name_template, '<timestamp>', str(time.time())) if (string.find(file_name_template, '<timestamp>') != -1) else file_name_template
        while os.path.exists(file_name):
            file_name_id += 1
            file_name = string.replace(file_name_template, '<timestamp>', str(time.time())) if (string.find(file_name_template, '<timestamp>') != -1) else string.replace(file_name_template, ".", str(file_name_id) + ".")
        # process the file
        with open(file_name, 'w') as f:
            json.dump(data, f, indent = 4) 
        print "File {} has been generated".format(file_name)
        return file_name

    @staticmethod
    def load_data_from_json_file(file_name):
        data = {}
        with open(file_name, 'r') as f:
            data = json.load(f)
        return data
    
    @staticmethod
    def randomword(length):
        return ''.join(random.choice(string.lowercase + string.digits) for dummy_i in range(length))

    @staticmethod
    def clean_up(dir_with_tests = ".", postfix = ".json"):
        """
        This function removes all files in folder from parameters (not from subfolders) with required postfix
        @param dir_with_tests: directory when selected files should be removed
        @param postfix: postfix for files that should be removed  
        """
        for name in os.listdir(dir_with_tests):
            if name.endswith(postfix): 
                file_or_dir_name = os.path.join(dir_with_tests, name)
                # we should process only files
                if os.path.isfile(file_or_dir_name):
                    os.remove(file_or_dir_name)
                    print "File {} has been removed...".format(file_or_dir_name)
