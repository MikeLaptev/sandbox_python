'''
Created on Jul 30, 2015

@author: Mikhail
'''

def check_chess_fields(coord1, coord2):
    """
    Check that two chess fields has the same color
    >>> check_chess_fields(('A', 1), ('C', 3))
    True
    >>> check_chess_fields(('A', 1), ('D', 3))
    False
    >>> check_chess_fields(('A', 1), ('B', 4))
    True
    >>> check_chess_fields(('A', 1), ('E', 3))
    True
    >>> check_chess_fields(('G', 7), ('C', 3))
    True
    """
    start_char = ord('A') 
    start_number = 1
    first_coord_id = (ord(coord1[0]) - start_char) % 2 + (coord1[1] - start_number) % 2
    second_coord_id = (ord(coord2[0]) - start_char) % 2 + (coord2[1] - start_number) % 2
    
    return first_coord_id % 2 == second_coord_id % 2


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())