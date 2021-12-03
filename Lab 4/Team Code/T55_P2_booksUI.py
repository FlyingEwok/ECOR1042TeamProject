# Team T-55:
# Nicholas Garth 101227727
# Divya Dushyanthan 101221637
# Dylan Fortier 101221463
# Spencer Green 101196310

# PLEASE UPDATE YOUR PYTHON VERSION TO 3.10 IF YOU HAVEN'T ALREADY!!!!! PYTHON VERSION 3.10 IS CRUCIAL FOR THE CODE TO RUN!!!

# Imports
from T55_P1_load_data import load_dataset
from T55_P3_sorting import sort_books_title, sort_books_ascending_rate, sort_books_descending_rate, sort_books_publisher, sort_books_category, sort_books_pageCount
from T55_P2_search_modify_dataset import get_books_by_rate, get_books_by_author, get_books_by_publisher,  get_books_by_category,all_categories_for_book_title, get_book_by_category_and_rate, print_dictionary_category, get_author_categories, all_categories_for_book_title, add_book , remove_book , find_books_by_title
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

def __checkcategoryexists(userinput:str)->bool:
    """Wrote by: Dylan Fortier 101221463
    Checks if a category exists in a dictionary"""
    for category in bookDict:
        if userinput == category:
            return True

def __book_info() -> tuple:
        """Written by: Divya Dushyanthan 101221637
        Returns a tuple for the info inputted, used in add book function command
        
        >>> book_info()
        (Old Yeller, Fred Gipson, 4.7, HarperCollins, Fiction, 144, Language)
        """
        title = input("Enter the title of the book you would like to add: ")
        author = input("Enter the author of the book you would like to add: ")
        rating = float(input("Enter the rating of the book you would like to add: "))
        publisher = input("Enter the publisher of the book you would like to add: ")
        genre = input("Enter the genre of the book you would like to add: ")
        pageCount = int(input("Enter the page count of the book you would like to add: "))
        language = input("Enter the language of the book you would like to add: ")
        info = (title, author, rating, publisher, genre, pageCount, language)

        return info

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
    # Keep running the program until user quits
    while True:
        print("\n1- Command Line L)oad file\n2- Command Line A)dd book\n3- Command Line R)emove book\n4- Command Line F)ind book by title\n5- Command Line NC) Number of books in a category\n6- Command Line CA) Categories for an author\n7- Command Line CB) Categories for a book title\n8- Command Line G)et book\n9- Command Line S)ort book\n10-Command line Q)uit")
        userInput = input("\nEnter the upper-case letter to the left of the bracket of the option you want: ")
        match userInput.upper():
            case 'L':
                bookDict = load_dict()
            case 'A':
                __bookLoadCheck(command_add)
            case 'R':
                __bookLoadCheck(command_remove)
            case 'F':
                __bookLoadCheck(command_find)
            case 'NC':
                __bookLoadCheck(call_print_dictionary_category)
            case 'CA':
                __bookLoadCheck(call_get_author_categories)
            case 'CB':
                __bookLoadCheck(call_all_categories_for_book_title)
            case 'G':
                __bookLoadCheck(get_book_call)
            case 'S':
                __bookLoadCheck(sortBookCall)
            case 'Q':
                # Wrote by: Dylan Fortier 101221463
                print('Quitting...')
                break # quits the program
            case _:
                __invalidCommand()

# Function 1
def load_dict() -> None:
    """Written by: Divya Dushyanthan 101221637
    Loads the dataset and puts it into the dictionary"""
    load_command = input("Enter the load data set you wish to enter: ")
    global bookDict # make bookDict global so it can be used in any function
    bookDict = load_dataset(load_command)
    print("Dataset loaded")
    time.sleep(1)

# Function 2
def command_add(book_dict : dict) -> None:
    """Written by: Divya Dushyanthan 101221637
    Executes add_book"""
    add_book(book_dict, __book_info())

# Function 3
def command_remove(book_dict : dict) -> None:
    """Written by: Divya Dushyanthan 101221637
    Removes a entry from dictionary given the users request"""
    title = input("Enter the title of the book you would like to remove: ")
    category = input("Enter the category of the book you would like to remove: ")
    r_command = remove_book(title,category, book_dict)

# Function 4
def command_find(book_dict : dict)-> None:
    """Written by: Divya Dushyanthan 101221637
    Finds a book based on title given users request"""
    title = input("Enter the title of the book you would like to find: ")
    f_command = find_books_by_title(title, book_dict) 

# Function 5
def call_print_dictionary_category(bookDict: dict) -> None:
    """Wrote by: Dylan Fortier 101221463/Converted to Function by: Nicholas Garth 101227727
    Runs a user interactive print_dictionary_categroy"""
    command = input('Enter the desired category: ') # prompts the user for the desired author
    if __checkcategoryexists(command): # if the category exists aka is True
        print_dictionary_category(command, bookDict)
    else:
        __invalidCommand() # entered an invalid command

# Function 6
def call_get_author_categories(bookDict: dict) -> None:
    """Wrote by: Dylan Fortier 101221463/Converted to Function by: Nicholas Garth 101227727
    Runs a user interactive get_author_categories"""
    command = input('Enter the desired author: ') # prompts the user for the desired author
    get_author_categories(command, bookDict)

# Function 7
def call_all_categories_for_book_title(bookDict: dict) -> None:
    """Wrote by: Dylan Fortier 101221463/Converted to Function by: Nicholas Garth 101227727
    Runs a user interactive all_categories_for_book_title"""
    command = input('Enter the desired book title: ') # prompts the user for the desired title
    all_categories_for_book_title(command, bookDict)

# Function 8
def get_book_call(book_dict: dict) -> None:
    """
    Function designed by Spencer Green
    Determines the way in which books of a data set will be retrieved when given a command including( R)ate, A)uthor, P)ublisher, C)ategory, CT)Category and Title, and CR)Category and Rate.
    >>>get_book_call(book_dict ).
    R)ate A)uthor P)ublisher C)ategory CT)Category and Title CR)Category and Rate.
    Enter an upper-case letter seen above to determine the way books are to be retrieved: 
    """
    while True:
        print("\nR)ate\tA)uthor\tP)ublisher\tC)ategory\tCT)Category and Title\tCR)Category and Rate\tRE)turn.")
        user_input = input("Enter an upper-case letter seen above to determine the way books are to be retrieved: " )
        match user_input.upper():
            case 'R':
                rate_input = input("Enter the desired book rating: ")
                get_books_by_rate(float(rate_input), book_dict)
            case 'A':
                author_input = input("Enter the desired book author: ")
                get_books_by_author(book_dict, author_input)
            case 'P':
                publisher_input = input("Enter the desired book publisher: ")
                get_books_by_publisher(publisher_input, book_dict)
            case 'C':
                category_input = input("Enter the desired book category: ")
                get_books_by_category(book_dict, category_input)
            case 'CT':
                title_input = input("Enter the desired book title: ")
                all_categories_for_book_title(title_input, book_dict)
            case 'CR':
                category_input = input("Enter the desired book category: ")
                rate_input = input("Enter the desired book rating: ")
                get_book_by_category_and_rate(category_input, rate_input, book_dict)
            case 'RE':
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
        print("\nT)itle\tR)ate\tP)ublisher\tC)ategory\tPA)ageCount\tRE)turn")
        userInput = input("Enter the upper-case letter to the left of the bracket of the option you want: ")
        match userInput.upper():
            case 'T':
                sort_books_title(bookDict)
            case 'R':
                while True: # Ask the user if they want ascending or descending order
                    print("\nA)scending\tD)escending\tRE)turn")
                    userInput = input("Enter the upper-case letter to the left of the bracket of the option you want: ")
                    match userInput.upper():
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

# Run the program
runProgram()