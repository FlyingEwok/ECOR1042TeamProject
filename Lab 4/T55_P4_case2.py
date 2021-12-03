# Dylan Fortier 101221463

from T55_P3_sorting import sort_books_title, sort_books_ascending_rate, sort_books_descending_rate, sort_books_publisher, sort_books_category, sort_books_pageCount
from T55_P2_search_modify_dataset import print_dictionary_category, get_author_categories, all_categories_for_book_title
from T55_P1_load_data import load_dataset

category_list = ('\nCategories: \n1- Adventure \t2- Biography \n3- Business \t4- Classics \n5- Comics \t6- Crime \n7- Detective \t8- Economics \n9- Epic \t10- Fantasy \n11- Fiction \t12- Finance \n13- Horror  \t14- Humor \n15- Information Technology \t16- Investing \n17- Legal \t18- Management \n19- Money Managment \t20- Mystery \n21- Mythical Creatures \t22- Psychology \n23- Social Science \t24- Superheroes \n25- Thrillers \t26- Traditional')

def case2(bookdict:dict)->None:
    """
    """
    def checkcategoryexists(userinput:str)->bool:
        for category in bookdict:
            if userinput == category:
                return True

    def invalidcommand()->None:
        print('No such command')

    while True:
        print('\n\t5- Command Line NC) Number of books in a category \n\t6- Command Line CA) Categories for an author \n\t7- Command Line CB) Categories for a book title \n\t10- Command Line Q)uit')
        print()
        command = input('Enter the upper-case letter(s) to the left of the bracket in the above command list for the corresponding action: ')
        if command.upper() == 'NC':
                command = input('Enter the desired category: ')
                if checkcategoryexists(command):
                    print_dictionary_category(command, bookdict)
                else:
                    invalidcommand()

        elif command.upper() == 'CA':
            command = input('Enter the desired author: ')
            get_author_categories(command, bookdict)

        elif command.upper() == 'CB':
            title = input('Enter the desired book title: ')
            all_categories_for_book_title(command, bookdict)

        elif command.upper() == 'Q':
            print('Quitting...')
            return None

        else:
            invalidcommand()

book_dict = load_dataset('Google_Books_Dataset.csv')
case2(book_dict)
