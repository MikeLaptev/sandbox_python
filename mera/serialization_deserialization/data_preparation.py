"""
Created on Aug, 13 2015

@author: mlaptev
"""

import string
import random
import os


class CData_Preparation(object):
    """
    Instance of this class will be used as example for serialization/deserialization approach in Python
    """

    # simple variable
    # string
    string_variable = ""
    # number
    number_variable = 0
    # dictionary
    dict_variable = dict()
    # array
    array_variable = list()
    # set
    set_variable = set()
    # tuple
    tuple_variable = tuple()

    def __init__(self, length_of_word=10, deepness=3):
        # string
        self.string_variable = randomword(length_of_word)
        # number
        self.number_variable = random.randint(0, length_of_word)
        # dictionary
        self.dict_variable.update(generate_deep_dict(amount_of_levels=deepness))
        # array
        self.array_variable.extend(generate_simple_array())
        # set
        for element in generate_simple_array():
            self.set_variable.add(element)
        # tuple
        self.tuple_variable = tuple(generate_simple_array())

    def __str__(self):
        string_to_return = "String variable: {}{}".format(
            self.string_variable, os.linesep
        )
        string_to_return += "Number variable: {}{}".format(
            self.number_variable, os.linesep
        )
        string_to_return += "Dictionary: {}".format(os.linesep)
        for dict_key, dict_value in list(self.dict_variable.items()):
            string_to_return += "Key: {} => Value: {}{}".format(
                dict_key, dict_value, os.linesep
            )
        string_to_return += "Array: {}{}".format(self.array_variable, os.linesep)
        string_to_return += "Set: {}{}".format(self.set_variable, os.linesep)
        string_to_return += "Tuple: {}{}".format(self.tuple_variable, os.linesep)

        return string_to_return

    def __eq__(self, other):
        # check on None
        if not other:
            return False
        # check type of the object
        if type(other) is not CData_Preparation:
            return False

        # list of standard checks
        if self.string_variable != other.string_variable:
            print("Incorrect string!")
            return False
        if self.number_variable != other.number_variable:
            print("Incorrect number!")
            return False
        if self.dict_variable != other.dict_variable:
            print("Incorrect dictionary!")
            return False
        if self.array_variable != other.array_variable:
            print("Incorrect array!")
            return False
        if self.set_variable != other.set_variable:
            print("Incorrect set!")
            return False
        if self.tuple_variable != other.tuple_variable:
            print("Incorrect tuple!")
            return False

        return True

    def __ne__(self, other):
        return not (self == other)


# This function generates random word of required length. Word consists of letter (lower-case) and digits
def randomword(length):
    return "".join(
        random.choice(string.lowercase + string.digits) for dummy_i in range(length)
    )


# This function generates random dictionary with required nesting
def generate_deep_dict(
    amount_of_levels=1,
    min_amount_of_leaves=1,
    max_amount_of_leaves=5,
    min_len_of_obj_in_dict=2,
    max_len_of_obj_in_dict=5,
    min_len_of_key=1,
    max_len_of_key=10,
):
    result_dict = dict()

    if amount_of_levels == 1:
        for dummy_i in range(
            random.randrange(min_amount_of_leaves, max_amount_of_leaves)
        ):
            key_to_add = randomword(random.randrange(min_len_of_key, max_len_of_key))
            # randomly choose type of object that will be added into data object
            # TODO: change to enum for Python 3.x
            object_type = random.randint(1, 3)
            if object_type == 1:
                # it should be dict
                value_to_add = generate_simple_dict(
                    min_len_of_obj_in_dict,
                    max_len_of_obj_in_dict,
                    min_len_of_key,
                    max_len_of_key,
                )
            elif object_type == 2:
                # it should be array
                value_to_add = generate_simple_array(
                    min_len_of_obj_in_dict,
                    max_len_of_obj_in_dict,
                    min_len_of_key,
                    max_len_of_key,
                )
            elif object_type == 3:
                # it should be string
                value_to_add = randomword(
                    random.randrange(min_len_of_key, max_len_of_key)
                )
            # adding
            result_dict[key_to_add] = value_to_add
    else:
        for dummy_i in range(
            random.randrange(min_amount_of_leaves, max_amount_of_leaves)
        ):
            key_to_add = randomword(random.randrange(min_len_of_key, max_len_of_key))
            # randomly choose type of object that will be added into data object
            # TODO: change to enum for Python 3.x
            object_type = random.randint(0, 3)
            if object_type == 1:
                # it should be dict
                value_to_add = generate_simple_dict(
                    min_len_of_obj_in_dict,
                    max_len_of_obj_in_dict,
                    min_len_of_key,
                    max_len_of_key,
                )
            elif object_type == 2:
                # it should be array
                value_to_add = generate_simple_array(
                    min_len_of_obj_in_dict,
                    max_len_of_obj_in_dict,
                    min_len_of_key,
                    max_len_of_key,
                )
            elif object_type == 3:
                # it should be string
                value_to_add = randomword(
                    random.randrange(min_len_of_key, max_len_of_key)
                )
            elif object_type == 0:
                # another layer of nesting
                value_to_add = generate_deep_dict(
                    amount_of_levels - 1,
                    min_amount_of_leaves,
                    max_amount_of_leaves,
                    min_len_of_obj_in_dict,
                    max_len_of_obj_in_dict,
                    min_len_of_key,
                    max_len_of_key,
                )
            # adding
            result_dict[key_to_add] = value_to_add

    return result_dict


def generate_simple_dict(
    min_len_of_obj_in_dict=1,
    max_len_of_obj_in_dict=5,
    min_len_of_key=1,
    max_len_of_key=10,
):
    data = dict()
    # generating random key
    for dummy_i in range(
        random.randrange(min_len_of_obj_in_dict, max_len_of_obj_in_dict)
    ):
        new_key = randomword(random.randrange(min_len_of_key, max_len_of_key))
        new_value = randomword(random.randrange(min_len_of_key, max_len_of_key))
        if new_key not in data:
            data[new_key] = new_value

    return data


def generate_simple_array(
    min_len_of_obj_in_dict=1,
    max_len_of_obj_in_dict=5,
    min_len_of_key=1,
    max_len_of_key=10,
):
    data = list()
    # generating random key
    for dummy_i in range(
        random.randrange(min_len_of_obj_in_dict, max_len_of_obj_in_dict)
    ):
        new_value = randomword(random.randrange(min_len_of_key, max_len_of_key))
        data.append(new_value)

    return data


if __name__ == "__main__":
    obj = CData_Preparation()
    print(obj)
