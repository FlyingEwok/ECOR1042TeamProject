# Milestone 3 Lab 1
# Divya Dushyanthan

import T55_P1_load_data
from T55_P1_load_data import readfile, load_dataset, to_camel_case, generateKey
import T55_P2_search_modify_dataset  
from T55_P2_search_modify_dataset import add_book , remove_book , find_books_by_title
from typing import Callable
import time

menu = ("\n1-Command Line L)oad file \n2-Command Line A)dd book \n3-Command Line R)emove book \n4-Command Line F)ind book by title \n5-Command Line NC) Number of books in a category \n6-Command Line CA) Categories for an author \n7-Command Line CB) Categories for a book title \n8-Command Line G)et book      \nR)ate   A)uthor   P)ublisher   C)ategory   CT) Category and Title    CR) Category and Rate \n9-Command Line \nS)ort book T)itle R)ate    P)ublisher  C)ategory  PA)ageCount\n10-Command line Q)uit")

def __bookLoadCheck(command: Callable) -> None:
        """
        Returns none. Checks if load has been entered before executing any other functions and reminds user to input it if not loaded.

        """
        if 'book_dict' in globals():
                command(book_dict)
        else:
                print("Please load the file first!")
                time.sleep(1) # Make it sleep so user can read it before it gets pushed up

def load_dict() -> None:
        """
        Written by Divya Dushyanthan 101221637
        Returns none. The function asks for which dataset the user would like to use and passes it into the load_dataset.
        """
        load_command = input("Enter the load data set you wish to enter: ")  
        global book_dict
        book_dict = load_dataset(load_command)    
               
def book_info() -> tuple:
        """
        Written by Divya Dushyanthan 101221637
        Returns a tuple for the info inputted, used in add book function command
        >>>> book_info()
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

def command_add(book_dict : dict) -> None:
        """
        Written by Divya Dushyanthan 101221637
        Returns none. The function takes in book_dict and passes it and the tuple from book_info into the add book function.
        """
        add_book(book_dict, book_info())
        
        
def command_remove(book_dict : dict) -> None:
        """
        Written by Divya Dushyanthan 101221637
        Returns none. The function takes in book_dict, passes it aswell as collects the title and category into the remove book function.
        """
        title = input("Enter the title of the book you would like to remove: ")
        category = input("Enter the category of the book you would like to remove: ")
        r_command = remove_book(title,category, book_dict)
        
def command_find(book_dict : dict)-> None:
        """
        Written by Divya Dushyanthan 101221637
        Returns none. The function takes in book_dict, passes it aswell as collects the title puts into the find book function.
        """
        title = input("Enter the title of the book you would like to find: ")
        f_command = find_books_by_title(title, book_dict)  
        

def case_one() -> None :

        """
        Written by Divya Dushyanthan 101221637
        Returns none. The function goes through all the commands of case one and calls the appropriate function and inputs.
        """
        start = True
        while start :
                print(menu)
                command = input("Enter the letter coresponding to the action you would like to do: ")
                if command.upper() == 'L':                       
                        load_dict()    
                elif command.upper() == 'A': 
                        __bookLoadCheck(command_add)
                elif command.upper() == 'R':
                        __bookLoadCheck(command_remove)
                elif command.upper() == 'F':
                        __bookLoadCheck(command_find)   
                        
                elif command.upper() == "Q":
                        start = False                  
                else :
                        print('No such command')
                   
                       
                 
                
        print("Done")        
      

case_one()

