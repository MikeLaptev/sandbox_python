'''
Created on Aug, 5 2015.

@author: mlaptev
'''
import string

def local_function_example(list_of_initials):
    """
    >>> local_function_example(["B, B", "K, P", "A, C", "C, A", "L, O"])
    <<< By Second name >>>
    A, C
    B, B
    C, A
    K, P
    L, O
    <<< By First name >>>
    C, A
    B, B
    A, C
    L, O
    K, P
    """
    
    def sort_by_second_name(list_of_initials_to_sort):
        return sorted(list_of_initials_to_sort)
    
    def sort_by_first_name(list_of_initials_to_sort):
        list_of_second_and_first_names = []
        # change the order
        for initials in list_of_initials_to_sort:
            list_of_second_and_first_names.append(", ".join(string.split(initials, ", ")[::-1]))
        # sorting
        list_of_second_and_first_names.sort()    
        # change the order back
        sorted_list = []
        for initials in list_of_second_and_first_names:
            sorted_list.append(", ".join(string.split(initials, ", ")[::-1]))
        
        return sorted_list
    
    print "<<< By Second name >>>"
    sorted_list_of_initials_by_second_name = sort_by_second_name(list_of_initials)
    for initials in sorted_list_of_initials_by_second_name:
        print initials
        
    print "<<< By First name >>>"
    sorted_list_of_initials_by_first_name = sort_by_first_name(list_of_initials)
    for initials in sorted_list_of_initials_by_first_name:
        print initials

if __name__ == '__main__':
    import doctest
    print doctest.testmod()