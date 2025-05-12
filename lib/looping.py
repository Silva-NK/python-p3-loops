#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
happy_new_year()

def square_integers(int_list):
    square_integers = list()
    for int in int_list:
        square_integer = int * int
        square_integers.append(square_integer)
    return square_integers
(print(square_integers(int_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])))

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()
