# Team T-55:
# Nicholas Garth 101227727
# Divya Dushyanthan 101221637
# Dylan Fortier 101221463
# Spencer Green 101196310

# PLEASE UPDATE YOUR PYTHON VERSION TO 3.10 IF YOU HAVEN'T ALREADY!!!!! PYTHON VERSION 3.10 IS CRUCIAL FOR THE CODE TO RUN!!!

# Imports
from T55_P1_load_data import load_dataset
from T55_P2_search_modify_dataset import print_dictionary_category
from T55_P3_sorting import sort_books_title, sort_books_ascending_rate, sort_books_descending_rate, sort_books_publisher, sort_books_category, sort_books_pageCount
from typing import Callable
import time
import sys

# Helper Functions
def __invalidCommand() -> None:
    """Written by Nicholas Garth 101227727
    Prints Invalid Command and passes (error handling)"""
    print("Invalid Command")
    time.sleep(1) # Make it sleep so user can read it before it gets pushed up
    pass

def __bookLoadCheck(command: Callable) -> None:
    """Written by Nicholas Garth 101227727
    Performs a check to see if bookDict is loaded, if it is then execute the function
    >>> __bookLoadCheck(sortBookCall)
    Please load the file first
    """
    if 'bookDict' in globals():
        command(bookDict)
    else:
        print("Please load the file first!")
        time.sleep(1) # Make it sleep so user can read it before it gets pushed up

def __checkPythonVersion() -> None:
    """Written by Nicholas Garth 101227727
    Check the version of Python the user is running and terminate if they aren't"""
    if sys.version_info < (3, 10):
        print('Please upgrade your Python version to 3.10.0 or higher')
        sys.exit()

def __checkCategoryExists(userInput: str) -> bool:
    for i in bookDict:
        if userInput == i:
            return True

# User Input Functions
def runProgram() -> None:
    """Written by Nicholas Garth 101227727
    Runs the interaction hub of the program -- (NEEDS PYTHON 3.10)
    >>> runProgram()

    1- Command Line L)oad file
    2- Command Line A)dd book
    3- Command Line R)emove book
    4- Command Line F)ind book by title
    5- Command Line NC) Number of books in a category
    6- Command Line CA) Categories for an author
    7- Command Line CB) Categories for a book title
    8- Command Line G)et book
    9- Command Line S)ort book
    10- Command line Q)uit

    Enter the upper-case letter to the left of the bracket of the option you want:
    """
    # Check what Python version the user is running and if running an old version terminate and tell them to upgrade
    __checkPythonVersion() 

    # Keep running the program until user quits
    while True:
        print("\n1- Command Line L)oad file\n2- Command Line A)dd book\n3- Command Line R)emove book\n4- Command Line F)ind book by title\n5- Command Line NC) Number of books in a category\n6- Command Line CA) Categories for an author\n7- Command Line CB) Categories for a book title\n8- Command Line G)et book\n9- Command Line S)ort book\n10-Command line Q)uit")
        userInput = input("\nEnter the upper-case letter to the left of the bracket of the option you want: ")
        match userInput:
            case 'L':
                global bookDict # make bookDict global so it can be used in any function
                bookDict = load_dataset('Google_Books_Dataset.csv') # REPLACE WHAT THIS VAR = WITH THE LOADFILE FUNCTION!!!!!
            case 'A':
                pass # Replace pass with function associated
            case 'R':
                pass # Replace pass with function associated
            case 'F':
                pass # Replace pass with function associated
            case 'NC':
                __bookLoadCheck(call_print_dictionary_category)
            case 'CA':
                pass # Replace pass with function associated
            case 'CB':
                pass # Replace pass with function associated
            case 'G':
                pass # Replace pass with function associated
            case 'S':
                __bookLoadCheck(sortBookCall)
            case 'Q':
                print("Thank You for using our program\nBye Bye!")
                break
            case _:
                __invalidCommand()

# Function 9
def sortBookCall(bookDict: dict) -> None:
    """Written by Nicholas Garth 101227727
    Asks user what sorting command they want to run on their dictionary  -- (NEEDS PYTHON 3.10)
    >>> sortBookCall(bookDict)
    T)itle   R)ate   P)ublisher  C)ategory   PA)ageCount    RE)turn
    Enter the upper-case letter to the left of the bracket of the option you want:
    """
    # Keep running the program until user returns to previous menu
    while True:
        print("\nT)itle   R)ate   P)ublisher  C)ategory   PA)ageCount    RE)turn")
        userInput = input("Enter the upper-case letter to the left of the bracket of the option you want: ")
        match userInput:
            case 'T':
                sort_books_title(bookDict)
            case 'R':
                while True: # Ask the user if they want ascending or descending order
                    print("\nA)scending   D)escending    RE)turn")
                    userInput = input("Enter the upper-case letter to the left of the bracket of the option you want: ")
                    match userInput:
                        case 'A':
                            sort_books_ascending_rate(bookDict)
                        case 'D':
                            sort_books_descending_rate(bookDict)
                        case 'RE':
                            break
                        case _:
                            __invalidCommand()
            case 'P':
                sort_books_publisher(bookDict)
            case 'C':
                sort_books_category(bookDict)
            case 'PA':
                sort_books_pageCount(bookDict)
            case 'RE':
                break
            case _:
                __invalidCommand()

def call_print_dictionary_category(bookDict: dict):
    while True:
        categoryToSearch = input("Enter a category: ")
        if __checkCategoryExists(categoryToSearch):
            print_dictionary_category(categoryToSearch, bookDict)
            time.sleep(3)
            break
        else:
            print("\nCategory not in this dictionary\nPlease Try Again.")

# Run the program
runProgram()