"""
Created on Aug 3, 2015

@author: Mikhail

@summary: Create several functions:
1. First function has two positional parameters and infinity numbers of positional parameters
2. Second function has a mandatory parameter with key and infinity number of parameters with keys
"""


def function_one(param_1, param_2, *list_of_params):
    print(("param_1 has value {}".format(param_1)))
    print(("param_2 has value {}".format(param_2)))
    if len(list_of_params) > 0:
        print("Additional arguments are:")
        for arg in list_of_params:
            print(("{}".format(arg)))
    else:
        print("No additional arguments")


def function_two(mandatory_param="Value!!!!!", **dictionary_of_params):
    print(("mandatory parameter is {}".format(mandatory_param)))
    if len(dictionary_of_params) > 0:
        print("Additional arguments are:")
        for key, value in list(dictionary_of_params.items()):
            print(("{} -> {}".format(key, value)))
    else:
        print("No additional arguments")


if __name__ == "__main__":
    print("Execution of first function")
    function_one(9, "Value!")
    function_one(9, "Value!", *[5, "Value!!", [6, "Value!!!"]])
    print("")
    print("Execution of second function")
    function_two(8, key1="Value!")
    function_two(9, key1="Value!", key2=[5, "Value!!", [6, "Value!!!"]])
    function_two(
        mandatory_param=10, key1="Value!", key2=[5, "Value!!", [6, "Value!!!"]]
    )
    function_two(key1="Value!", key2=[5, "Value!!", [6, "Value!!!"]])
