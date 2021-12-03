# Dylan Fortier 101221463 T55

# Imports
from T55_P3_sorting import sort_books_title, sort_books_ascending_rate    , sort_books_descending_rate, sort_books_publisher, sort_books_category, sort_books_pageCount
from T55_P2_search_modify_dataset import print_dictionary_category, get_author_categories, all_categories_for_book_title
from T55_P1_load_data import load_dataset

# Function for case 2
def case2(bookdict:dict)->None:
    """
    Returns a interactive UI which has 4 commands that the user can interact with and inputs a dictionary.
    >>>case2(load_dataset('Google_Books_Dataset.csv'))

	5- Command Line NC) Number of books in a category
	6- Command Line CA) Categories for an author
	7- Command Line CB) Categories for a book title
	10- Command Line Q)uit

    Enter the upper-case letter(s) to the left of the bracket in the above command list for the corresponding action:
    """
    # checks if the category exists, used for command NC
    def checkcategoryexists(userinput:str)->bool:
        for category in bookdict:
            if userinput == category:
                return True

    # simply prints no such command when an improper input is detected
    def invalidcommand()->None:
        print('No such command')

    while True:
        # Prints the UI with all the commands
        print('\n\t5- Command Line NC) Number of books in a category \n\t6- Command Line CA) Categories for an author \n\t7- Command Line CB) Categories for a book title \n\t10- Command Line Q)uit')
        print()
        # prompts the user for a command to execute
        command = input('Enter the upper-case letter(s) to the left of the bracket in the above command list for the corresponding action: ')
        # if the command is NC
        if command.upper() == 'NC': # checks the input and converts it to uppercase if entered as lowercase
                command = input('Enter the desired category: ') # prompts the user for the desired author
                if checkcategoryexists(command): # if the category exists aka is True
                    print_dictionary_category(command, bookdict)
                else:
                    invalidcommand() # entered an invalid command
        # if the command is CA
        elif command.upper() == 'CA':# checks the input and converts it to uppercase if entered as lowercase
            command = input('Enter the desired author: ') # prompts the user for the desired author
            get_author_categories(command, bookdict)
        # if the command is CB
        elif command.upper() == 'CB':# checks the input and converts it to uppercase if entered as lowercase
            command = input('Enter the desired book title: ') # prompts the user for the desired title
            all_categories_for_book_title(command, bookdict)
        # if the command is Q
        elif command.upper() == 'Q':# checks the input and converts it to uppercase if entered as lowercase
            print('Quitting...') # notifies the user
            return None # quits the program

        else:
            invalidcommand() # entered an invalid command

case2(load_dataset('Google_Books_Dataset.csv'))
