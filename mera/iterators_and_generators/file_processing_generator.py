'''
Created on Aug, 11 2015

@author: mlaptev
'''

def file_processing(file_name = "TCP_IP.txt", word_to_search="TCP"):
    string_number = 0
    with open(file_name, 'r') as f:
        for line_in_file in f:
            string_number += 1
            if word_to_search in line_in_file:
                yield "{}: {}{}".format(string_number, line_in_file[:68], "...") 

if __name__ == '__main__':
    for line_info in file_processing():
        print line_info