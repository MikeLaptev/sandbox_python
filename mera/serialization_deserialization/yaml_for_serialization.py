'''
Created on Aug, 12 2015

@author: mlaptev
'''

from base_serialization import Base_Serialization

import yaml
import os

class YAML_Serialization(Base_Serialization):
    '''
    This class will be used to demonstration of both serialization and de-serialization
    capabilities with using YAML
    '''

    def __init__(self):
        Base_Serialization.__init__(self)
        self.file_extension = "yaml"
        self.file_name_pattern = self.__class__.__name__ + "_" + self.file_name_pattern + self.file_extension
        

    #
    def serialize_object(self, object_to_serialize):
        object_file_name = self.file_name_pattern.replace(self.type_template, object_to_serialize.__class__.__name__)
        with open(object_file_name, 'w') as f:
            yaml.dump(object_to_serialize, f)

    #
    def deserialize_object(self, type_of_serialized_object):
        object_file_name = self.file_name_pattern.replace(self.type_template, type_of_serialized_object)
        with open(object_file_name, 'r') as f:
            data = yaml.load(f)
        return data
        
if __name__ == "__main__":
    yaml_serialization = YAML_Serialization()
    print "{0}Serialization... {0}".format(os.linesep)
    yaml_serialization.serialize_me()
    print "{0}Deserialization... {0}".format(os.linesep)
    yaml_serialization.deserialize_me()
    print "{0}Done... {0}".format(os.linesep)