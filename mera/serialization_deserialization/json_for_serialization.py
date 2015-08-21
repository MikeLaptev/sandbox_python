'''
Created on Aug, 12 2015

@author: mlaptev
'''

from base_serialization import Base_Serialization

import json
import os

class JSON_Serialization(Base_Serialization):
    '''
    This class will be used to demonstration of both serialization and de-serialization
    capabilities with using JSON
    '''

    def __init__(self):
        Base_Serialization.__init__(self)
        self.file_extension = "json"
        self.file_name_pattern = self.__class__.__name__ + "_" + self.file_name_pattern + self.file_extension
        

    def serialize_object(self, object_to_serialize):
        try:
            object_file_name = self.file_name_pattern.replace(self.type_template, object_to_serialize.__class__.__name__)
            with open(object_file_name, 'w') as f:
                json.dump(object_to_serialize, f, indent = 4)
        except TypeError, te:
            print "Object '{}' is not JSON serializable: {}{}".format(object_to_serialize.__class__.__name__, os.linesep, te)

    def deserialize_object(self, type_of_serialized_object):
        try:
            object_file_name = self.file_name_pattern.replace(self.type_template, type_of_serialized_object)
            with open(object_file_name, 'r') as f:
                data = json.load(f)
            return data
        except ValueError, ve:
            print "Object '{}' could not be decoded after serialization: {}{}".format(type_of_serialized_object, os.linesep, ve)
        
if __name__ == "__main__":
    json_serialization = JSON_Serialization()
    print "{0}Serialization... {0}".format(os.linesep)
    json_serialization.serialize_me()
    print "{0}Deserialization... {0}".format(os.linesep)
    json_serialization.deserialize_me()
    print "{0}Done... {0}".format(os.linesep)