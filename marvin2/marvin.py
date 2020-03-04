#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import random
marvin_image = r"""
       o                 o
                  o
         o   ______      o
           _/  (   \_
 _       _/  (       \_  O
| \_   _/  (   (    0  \
|== \_/  (   (          |
|=== _ (   (   (        |
|==_/ \_ (   (          |
|_/     \_ (   (    \__/
          \_ (      _/
            |  |___/
           /__/
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""

def menu():
    """
    Prints menu
    """
    print("1) Present yourself to Marvin.")
    print("2) Celcius to Fahrenheit:")
    print("3) Multiplying words.")
    print("4) Total and average.")
    print("5) Comparing values:")
    print("6) String and added characters:")
    print("7) Isogram?")
    print("8) Shuffle word:")
    print("9) Anagram.")
    print("10) Acronym.")
    print("11) Mask a string:")
    print("q) Quit.")

def greeter():
    """
    Prints greeting
    """
    name = input("What is your name? ")
    print("\nMarvin says:\n")
    print("Hello %s - your awesomeness!" % name)
    print("What can I do you for?!")

def converting_degrees():
    """
    Prints Celcius to Fahrenheit
    """
    print("Convert Celcius-degrees til Fahrenheit:")
    user_input = input()
    print((int(user_input) * 9) / 5 + 32)

def multiplying_word():
    """
    Prints word multiple times
    """
    print("Tell me a word to multiply!")
    word = input()
    print("How many times?")
    times = input()
    for _ in range(int(times)):
        print(word)

def average_and_total():
    """
    Prints average and total
    """
    print("Write numbers and finish with 'done':")
    my_list = []
    while True:
        print("Number:")
        number = input()
        if number == "done":
            break
        list.append(int(number))
    print("The total is: " + str(sum(my_list)))
    mean = sum(my_list) / len(my_list)

    print("The average is: " + str(mean))

def compare_value():
    """
    Prints compared values
    """
    print("Comparing values, write 'done' when finished:")
    while True:
        print("You number")
        previous = input()
        if previous == "done":
            break
        else:
            print("Next")
            current = int(input())
            previous = int(previous)
            if current > previous:
                print("Bigger than")
            elif current < previous:
                print("Smaller than")
            else:
                print("Equal")

def add_charachters():
    """
    Prints added charachters to String
    """
    word_in = input("Write a word:")
    word_out = ""
    i = 0
    for letter in word_in:
        word_out = word_out + letter * (i + 1) + '-'
        i += 1
    print(word_out[:-1])

def test_isogram():
    """
    Prints if word is Isogram
    """
    word_in = input("Write a word: ")
    isogram = True
    for letter in word_in:
        total = 0
        for l in word_in:
            if letter == l:
                total += 1
            if total > 1:
                isogram = False
    print("Isogram: " + str(isogram))

def random_word():
    """
    Shuffles word
    """
    while True:
        word = input("Write a word: ")
        word_out = ""
        try:
            int(word)
            print("Error: has to be a word!")
            continue
        except ValueError:
            while word:
                #slumpa siffra inom längden av ordet
                index = random.randint(0, len(word) -1)
                #ta ut slumpade bokstav till nya ordet
                word_out += word[index]
                #kolonet betyder allting över och under beroende på position
                word = word[:index] + word[index + 1:]
        print(word_out)
        break

def anagram():
    """
    Check if Anagram
    """
    word_in1 = input("Write a word: ").lower()
    word_in2 = input("Write next word: ").lower()
    if sorted(word_in1) == sorted(word_in2):
        print("This is an Anagram")
    else:
        print("This is not an Anagram")

def create_acronym():
    """
    Create an Acronym
    """
    string = input("Enter a phrase starting with capital letters: ")
    string_split = string.split()
    acronym = ""
    for i in string_split:
        acronym = acronym + i[0].upper()

    print(acronym)

def mask_string():
    """
    Mask a string
    """
    string_in = input("Print a string of atleast 5 characters : ")
    index = 0
    new_string = ""
    for c in string_in:
        if index < len(string_in) - 4:
            new_string += "#"
        else:
            new_string += c
        index += 1

    print(new_string)


while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("Hi, I'm Marvin. I know it all. What can I do you for?")

    menu()

    choice = input("--> ")

    if choice == "q":
        print("Bye, bye - and welcome back anytime!")
        break

    elif choice == "1":
        greeter()
    elif choice == "2":
        converting_degrees()
    elif choice == "3":
        multiplying_word()
    elif choice == "4":
        average_and_total()
    elif choice == "5":
        compare_value()
    elif choice == "6":
        add_charachters()
    elif choice == "7":
        test_isogram()
    elif choice == "8":
        random_word()
    elif choice == "9":
        anagram()
    elif choice == "10":
        create_acronym()
    elif choice == "11":
        mask_string()


    else:
        print("That is not a valid choice. You can only choose from the menu.")

    input("\nPress enter to continue...")
