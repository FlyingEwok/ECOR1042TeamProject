# Team T-55
# Nicholas Garth 101227727

from T55_P3_sorting import sort_books_title, sort_books_ascending_rate, sort_books_descending_rate, sort_books_publisher, sort_books_category, sort_books_pageCount
from T55_P1_load_data import load_dataset
import time
import sys

# Helper Functions
def __invalidCommand() -> None:
    """Written by Nicholas Garth 101227727
    Prints Invalid Command and passes (error handling)"""
    print("Invalid Command")
    time.sleep(1) # Make it sleep so user can read it before it gets pushed up
    pass

def __checkPythonVersion() -> None:
    """Written by Nicholas Garth 101227727
    Check the version of Python the user is running and terminate if they aren't"""
    if sys.version_info < (3, 10):
        print('Please upgrade your Python version to 3.10.0 or higher')
        sys.exit()

# Sort Book Call Function
def sortBookCall(bookDict: dict) -> None:
    """Written by Nicholas Garth 101227727
    Asks user what sorting command they want to run on their dictionary
    >>> sortBookCall(bookDict)
    T)itle   R)ate   P)ublisher  C)ategory   PA)ageCount    RE)turn
    Enter the upper-case letter to the left of the bracket of the option you want:
    """
    # Check Python Version
    __checkPythonVersion()

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
        
book_dict = load_dataset('Google_Books_Dataset.csv')
sortBookCall(book_dict)