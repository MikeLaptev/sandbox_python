'''
Created on Aug, 12 2015

@author: mlaptev
'''

from base_serialization import Base_Serialization
import os

class XML_Serialization(Base_Serialization):
    '''
    This class will be used to demonstration of both serialization and de-serialization
    capabilities with using XML
    '''

    def __init__(self):
        Base_Serialization.__init__(self)
        self.file_extension = "xml"
        self.file_name_pattern = self.__class__.__name__ + "_" + self.file_name_pattern + self.file_extension
        

    #
    def serialize_object(self, object_to_serialize):
        # TODO:
        print "Not implemented... and not supported at this time..."
        pass

    #
    def deserialize_object(self, type_of_serialized_object):
        # TODO:
        print "Not implemented... and not supported at this time..."
        pass
        
if __name__ == "__main__":
    xml_serialization = XML_Serialization()
    print "{0}Serialization... {0}".format(os.linesep)
    xml_serialization.serialize_me()
    print "{0}Deserialization... {0}".format(os.linesep)
    xml_serialization.deserialize_me()
    print "{0}Done... {0}".format(os.linesep)