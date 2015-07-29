'''
Created on Jul 29, 2015

@author: Mikhail
'''
import json
import random
import string
import time
import os
import threading

class MyOwnJSONProcessing:
    
    # variables for amount of objects in dictionary (for json)
    min_len_of_json_dict = 1
    max_len_of_json_dict = 5
    # variables for max and min length of keys in dictionary (for json)
    min_len_of_key = 1
    max_len_of_key = 10
    # variable for max value in dictionary (for json)
    max_value = 100
    
    def generate_set_of_files_with_json_obj(self, amount_of_files):
        for dummy_i in xrange(amount_of_files):
            #print "Generating of file #{}".format(dummy_i)
            self.generate_json_file_with_data(data = self.generate_data_for_json_obj())
    
    def generate_data_for_json_obj(self):
        json_data = {}
        # generating random key
        for dummy_i in range(random.randrange(self.min_len_of_json_dict, self.max_len_of_json_dict)):
            new_key = self.randomword(random.randrange(self.min_len_of_key, self.max_len_of_key))
            new_value = random.randrange(self.max_value)
            if not json_data.has_key(new_key):
                json_data[new_key] = new_value
                
        
        return json_data
    
    def generate_json_file_with_data(self, file_name_template = "data_<timestamp>.json", data = {}):
        """
        By default this function generates json file with name that contains time-stamp 
        when it has been generated
        """
        file_name_id = 0
        file_name = string.replace(file_name_template, '<timestamp>', str(time.time())) if (string.find(file_name_template, '<timestamp>') != -1) else file_name_template
        while os.path.exists(file_name):
            file_name_id += 1
            file_name = string.replace(file_name_template, '<timestamp>', str(time.time())) if (string.find(file_name_template, '<timestamp>') != -1) else string.replace(file_name_template, ".", str(file_name_id) + "")
        # process the file
        with open(file_name, 'w') as f:
            json.dump(data, f, indent = 4) 
            
    def load_data_from_json_file(self, file_name):
        data = {}
        lock = threading.Lock()
        with lock:
            with open(file_name, 'r') as f:
                data = json.load(f)
            
        return data
    
    def randomword(self, length):
        return ''.join(random.choice(string.lowercase) for dummy_i in range(length))

if __name__ == '__main__':
    json_generator = MyOwnJSONProcessing()
    json_generator.generate_set_of_files_with_json_obj(5)