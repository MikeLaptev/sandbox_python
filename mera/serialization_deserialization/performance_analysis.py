'''
Created on Aug 21, 2015

@author: mlaptev
'''
from data_preparation import generate_deep_dict
from data_preparation import generate_simple_array

import json
import yaml
import pickle

import timeit
import tempfile

class Performance_Analysis(object):
    '''
    This class is used to analyze performance of serialization/deserialization approaches for JSON, YAML and Pickle 
    '''
    
    def __init__(self):
        print "Initialization started..."
        self.big_dict_with_single_deepness = generate_deep_dict(amount_of_levels=1, min_amount_of_leaves=1, max_amount_of_leaves=5, min_len_of_obj_in_dict=1, max_len_of_obj_in_dict=5, min_len_of_key=5, max_len_of_key=15)
        print "Big dictionary with single deepness has been generated..."
        print self.big_dict_with_single_deepness
        self.big_array = generate_simple_array(min_len_of_obj_in_dict=10, max_len_of_obj_in_dict=50, min_len_of_key=5, max_len_of_key=15)
        print "Big array has been generated..."
        print self.big_array
        self.big_dict_with_big_deepness = generate_deep_dict(amount_of_levels=5, min_amount_of_leaves=3, max_amount_of_leaves=5, min_len_of_obj_in_dict=3, max_len_of_obj_in_dict=5, min_len_of_key=5, max_len_of_key=15)
        print "Big dictionary with big deepness has been generated..."
        print self.big_dict_with_big_deepness
        print "Initialization completed..."

    # Serialization
    # JSON
    # Serialization into string
    def serialize_to_str_with_json(self, object_to_serialize):
        return json.dumps(object_to_serialize)
    # Serialization into temporary file that will be removed automatically after execution
    # Last parameter is True by default, since this function is needed only for performance measurements.
    def serialize_to_file_with_json(self, object_to_serialize, delete_tmp_file = True):
        with tempfile.NamedTemporaryFile(delete=delete_tmp_file) as f:
            json.dump(object_to_serialize, f, indent = 4)
            if not delete_tmp_file: return f.name

    # YAML
    # Serialization into string
    def serialize_to_str_with_yaml(self, object_to_serialize):
        return yaml.dump(object_to_serialize)
    # Serialization into temporary file that will be removed automatically after execution
    # Last parameter is True by default, since this function is needed only for performance measurements.
    def serialize_to_file_with_yaml(self, object_to_serialize, delete_tmp_file = True):
        with tempfile.NamedTemporaryFile(delete=delete_tmp_file) as f:
            yaml.dump(object_to_serialize, f)
            if not delete_tmp_file: return f.name

    # Pickle
    # Serialization into string
    def serialize_to_str_with_pickle(self, object_to_serialize):
        return pickle.dumps(object_to_serialize)
    # Serialization into temporary file that will be removed automatically after execution
    # Last parameter is True by default, since this function is needed only for performance measurements.
    def serialize_to_file_with_pickle(self, object_to_serialize, delete_tmp_file = True):
        with tempfile.NamedTemporaryFile(delete=delete_tmp_file) as f:
            pickle.dump(object_to_serialize, f)
            if not delete_tmp_file: return f.name

    # Deerialization
    # JSON
    # Deserialization from string
    def deserialize_str_with_json(self, serialized_string):
        return json.loads(serialized_string)
    # Deserialization from file. This function does not delete file after execution.
    def deserialize_file_with_json(self, file_name):
        with open(file_name, 'r') as f:
            data = json.load(f)
        return data
    
    # YAML
    # Deserialization from string
    def deserialize_str_with_yaml(self, serialized_string):
        return yaml.load(serialized_string)
    # Deserialization from file. This function does not delete file after execution.
    def deserialize_file_with_yaml(self, file_name):
        with open(file_name, 'r') as f:
            data = yaml.load(f)
        return data
    
    # Pickle
    # Deserialization from string
    def deserialize_str_with_pickle(self, serialized_string):
        return pickle.loads(serialized_string)
    # Deserialization from file. This function does not delete file after execution.
    def deserialize_file_with_pickle(self, file_name):
        with open(file_name, 'r') as f:
            data = pickle.load(f)
        return data
    
if __name__ == "__main__":
    amount_of_iterations_in_timeit = 1
    for iteration_number in range(1, 6):
        # Generate new random object on each iteration
        print "Iteration #{}".format(iteration_number)
        perf_object = Performance_Analysis()
        # Serialization
        print "Serialization (with Strings)"
        # JSON
        print "JSON:"
        print "Big dictionary: {}".format(timeit.timeit(stmt="perf_object.serialize_to_str_with_json(perf_object.big_dict_with_single_deepness)", setup="from __main__ import perf_object"), number=amount_of_iterations_in_timeit)
        print "Big array: {}".format(timeit.timeit(stmt="perf_object.serialize_to_str_with_json(perf_object.big_array)", setup="from __main__ import perf_object"), number=amount_of_iterations_in_timeit)
        print "Big dictionary with deepness: {}".format(timeit.timeit(stmt="perf_object.serialize_to_str_with_json(perf_object.big_dict_with_big_deepness)", setup="from __main__ import perf_object"), number=amount_of_iterations_in_timeit)
        # YAML
        print "YAML"
        print "Big dictionary: {}".format(timeit.timeit(stmt="perf_object.serialize_to_str_with_yaml(perf_object.big_dict_with_single_deepness)", setup="from __main__ import perf_object"), number=amount_of_iterations_in_timeit)
        print "Big array: {}".format(timeit.timeit(stmt="perf_object.serialize_to_str_with_yaml(perf_object.big_array)", setup="from __main__ import perf_object"), number=amount_of_iterations_in_timeit)
        print "Big dictionary with deepness: {}".format(timeit.timeit(stmt="perf_object.serialize_to_str_with_yaml(perf_object.big_dict_with_big_deepness)", setup="from __main__ import perf_object"), number=amount_of_iterations_in_timeit)
        # Pickle
        print "Pickle"
        print "Big dictionary: {}".format(timeit.timeit(stmt="perf_object.serialize_to_str_with_pickle(perf_object.big_dict_with_single_deepness)", setup="from __main__ import perf_object"), number=amount_of_iterations_in_timeit)
        print "Big array: {}".format(timeit.timeit(stmt="perf_object.serialize_to_str_with_pickle(perf_object.big_array)", setup="from __main__ import perf_object"), number=amount_of_iterations_in_timeit)
        print "Big dictionary with deepness: {}".format(timeit.timeit(stmt="perf_object.serialize_to_str_with_pickle(perf_object.big_dict_with_big_deepness)", setup="from __main__ import perf_object"), number=amount_of_iterations_in_timeit)
        
        # Deserialization
        print "Deserialization (with Strings)"
        # JSON
        print "JSON"
        json_big_dictionary = perf_object.serialize_to_str_with_json(perf_object.big_dict_with_single_deepness)
        json_big_array = perf_object.serialize_to_str_with_json(perf_object.big_array)
        json_big_dictionary_with_deepness = perf_object.serialize_to_str_with_json(perf_object.big_dict_with_big_deepness)
        print "Big dictionary: {}".format(timeit.timeit(stmt="perf_object.deserialize_str_with_json(json_big_dictionary)", setup="from __main__ import perf_object, json_big_dictionary"), number=amount_of_iterations_in_timeit)
        print "Big array: {}".format(timeit.timeit(stmt="perf_object.deserialize_str_with_json(json_big_array)", setup="from __main__ import perf_object, json_big_array"), number=amount_of_iterations_in_timeit)
        print "Big dictionary with deepness: {}".format(timeit.timeit(stmt="perf_object.deserialize_str_with_json(json_big_dictionary_with_deepness)", setup="from __main__ import perf_object, json_big_dictionary_with_deepness"), number=amount_of_iterations_in_timeit)
        # YAML
        print "YAML"
        yaml_big_dictionary = perf_object.serialize_to_str_with_yaml(perf_object.big_dict_with_single_deepness)
        yaml_big_array = perf_object.serialize_to_str_with_yaml(perf_object.big_array)
        yaml_big_dictionary_with_deepness = perf_object.serialize_to_str_with_yaml(perf_object.big_dict_with_big_deepness)
        print "Big dictionary: {}".format(timeit.timeit(stmt="perf_object.deserialize_str_with_yaml(yaml_big_dictionary)", setup="from __main__ import perf_object, yaml_big_dictionary"), number=amount_of_iterations_in_timeit)
        print "Big array: {}".format(timeit.timeit(stmt="perf_object.deserialize_str_with_yaml(yaml_big_array)", setup="from __main__ import perf_object, yaml_big_array"), number=amount_of_iterations_in_timeit)
        print "Big dictionary with deepness: {}".format(timeit.timeit(stmt="perf_object.deserialize_str_with_yaml(yaml_big_dictionary_with_deepness)", setup="from __main__ import perf_object, yaml_big_dictionary_with_deepness"), number=amount_of_iterations_in_timeit)
        # Pickle
        print "Pickle"
        pickle_big_dictionary = perf_object.serialize_to_str_with_pickle(perf_object.big_dict_with_single_deepness)
        pickle_big_array = perf_object.serialize_to_str_with_pickle(perf_object.big_array)
        pickle_big_dictionary_with_deepness = perf_object.serialize_to_str_with_pickle(perf_object.big_dict_with_big_deepness)
        print "Big dictionary: {}".format(timeit.timeit(stmt="perf_object.deserialize_str_with_pickle(pickle_big_dictionary)", setup="from __main__ import perf_object, pickle_big_dictionary"), number=amount_of_iterations_in_timeit)
        print "Big array: {}".format(timeit.timeit(stmt="perf_object.deserialize_str_with_pickle(pickle_big_array)", setup="from __main__ import perf_object, pickle_big_array"), number=amount_of_iterations_in_timeit)
        print "Big dictionary with deepness: {}".format(timeit.timeit(stmt="perf_object.deserialize_str_with_pickle(pickle_big_dictionary_with_deepness)", setup="from __main__ import perf_object, pickle_big_dictionary_with_deepness"), number=amount_of_iterations_in_timeit)