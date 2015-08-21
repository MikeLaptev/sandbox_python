'''
Created on Aug 20, 2015

@author: mlaptev
'''

from data_preparation import CData_Preparation
from data_preparation import generate_simple_array
from data_preparation import generate_deep_dict
from data_preparation import randomword

import random
import os

class Base_Serialization(object):
    '''
    Base class for all classes that will be used for serialization/deserialization tutorial
    '''

    #
    def __init__(self):
        # object
        self.data_object = CData_Preparation()
        # array
        self.array_object = generate_simple_array()
        # dictionary
        self.dict_object = generate_deep_dict(amount_of_levels=3)
        # set
        self.set_object = set()
        for element in generate_simple_array():
            self.set_object.add(element)
        # tuple
        self.tuple_object = tuple(generate_simple_array())
        # string
        self.string_object = randomword(random.randint(10, 100))
        # int
        self.int_object = random.randint(10, 100)
        
        self.type_template = "%type%"
        self.file_extension = "txt"
        self.file_name_pattern = self.type_template + "."

    #
    def serialize_me(self):
        # Object
        self.serialize_object(self.data_object)

        # Array
        self.serialize_object(self.array_object)

        # Dictionary
        self.serialize_object(self.dict_object)

        # Set
        self.serialize_object(self.set_object)

        # Tuple
        self.serialize_object(self.tuple_object)

        # String
        self.serialize_object(self.string_object)

        # Integer
        self.serialize_object(self.int_object)
    
    """
    @attention: this function should be overriden in successor
    """
    def serialize_object(self, object_to_serialize):
        pass

    #
    def deserialize_me(self):
        # Object
        deserialized_object = self.deserialize_object(self.data_object.__class__.__name__)
        if self.data_object != deserialized_object:
            print "Incorrect serialization/deserialization of Data object. {0}Expected: {1}{0}Actual: {2}".format(os.linesep, self.data_object, deserialized_object)
        
        # Array
        deserialized_array = self.deserialize_object(self.array_object.__class__.__name__)
        if self.array_object != deserialized_array:
            print "Incorrect serialization/deserialization of Array object. {0}Expected: {1}{0}Actual: {2}".format(os.linesep, self.array_object, deserialized_array)
        
        # Dictionary
        deserialized_dictionary = self.deserialize_object(self.dict_object.__class__.__name__)
        if self.dict_object != deserialized_dictionary:
            print "Incorrect serialization/deserialization of Dict object. {0}Expected: {1}{0}Actual: {2}".format(os.linesep, self.dict_object, deserialized_dictionary)
        
        # Set
        deserialized_set = self.deserialize_object(self.set_object.__class__.__name__)
        if self.set_object != deserialized_set:
            print "Incorrect serialization/deserialization of Set object. {0}Expected: {1}{0}Actual: {2}".format(os.linesep, self.set_object, deserialized_set)
        
        # Tuple
        deserialized_tuple = self.deserialize_object(self.tuple_object.__class__.__name__)
        if self.tuple_object != deserialized_tuple:
            print "Incorrect serialization/deserialization of Tuple object. {0}Expected: {1}{0}Actual: {2}".format(os.linesep, self.tuple_object, deserialized_tuple)
        
        # String
        deserialized_string = self.deserialize_object(self.string_object.__class__.__name__)
        if self.string_object != deserialized_string:
            print "Incorrect serialization/deserialization of String object. {0}Expected: {1}{0}Actual: {2}".format(os.linesep, self.string_object, deserialized_string)
        
        # Integer
        deserialized_integer = self.deserialize_object(self.int_object.__class__.__name__)
        if self.int_object != deserialized_integer:
            print "Incorrect serialization/deserialization of Number object. {0}Expected: {1}{0}Actual: {2}".format(os.linesep, self.int_object, deserialized_integer)
        
    """
    @attention: this function should be overriden in successor
    """
    def deserialize_object(self, type_of_serialized_object):
        pass