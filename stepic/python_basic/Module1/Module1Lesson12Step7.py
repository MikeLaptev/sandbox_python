# coding=utf-8
__author__ = 'mlaptev'

if __name__ == "__main__":
    ticket_number = input()
    if int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2]) == \
       int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5]):
        print("Счастливый")
    else:
        print("Обычный")
