#Spencer Green 101196310

# PLEASE UPDATE YOUR PYTHON VERSION TO 3.10 IF YOU HAVEN'T ALREADY!!!!! PYTHON VERSION 3.10 IS CRUCIAL FOR THE CODE TO RUN!!!

from T55_P1_load_data import load_dataset
from T55_P2_search_modify_dataset import get_books_by_rate, get_books_by_author, get_books_by_publisher,  get_books_by_category,all_categories_for_book_title, get_book_by_category_and_rate
import time
from typing import Callable
def __invalidCommand() -> None:
    """Written by Nicholas Garth 101227727
    Prints Invalid Command and passes (error handling)"""
    print("Invalid Command")
    time.sleep(1) # Make it sleep so user can read it before it gets pushed up
    pass

def get_book_call(book_dict: dict) -> None:
    """
    Function designed by Spencer Green
    Determines the way in which books of a data set will be retrieved when given a command including( R)ate, A)uthor, P)ublisher, C)ategory, CT)Category and Title, and CR)Category and Rate.
    >>>get_book_call(book_dict ).
    R)ate A)uthor P)ublisher C)ategory CT)Category and Title CR)Category and Rate.
    Enter an upper-case letter seen above to determine the way books are to be retrieved: 
    """
    while True:
        print("\nR)ate A)uthor P)ublisher C)ategory CT)Category and Title CR)Category and Rate RE)turn.")
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
            

y = get_book_call(load_dataset('Google_Books_Dataset.csv'))