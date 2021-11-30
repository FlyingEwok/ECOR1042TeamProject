# Team T-55
# Nicholas Garth 101227727

from T55_P3_sorting import sort_books_title, sort_books_ascending_rate, sort_books_descending_rate, sort_books_publisher, sort_books_category, sort_books_pageCount
from T55_P1_load_data import load_dataset

def __invalidCommand() -> None:
    """Prints Invalid Command and passes (error handling)"""
    print("Invalid Command")
    pass

def sortBookCall(bookDict: dict) -> None:
    """Asks user what sorting command they want to run on their dictionary
    >>> sortBookCall(bookDict)
    T)itle   R)ate   P)ublisher  C)ategory   PA)ageCount    RE)turn
    Enter the upper-case letter to the left of the bracket of the option you want:
    """
    while True:
        print("\nT)itle   R)ate   P)ublisher  C)ategory   PA)ageCount    RE)turn")
        userInput = input("Enter the upper-case letter to the left of the bracket of the option you want: ")
        if userInput == 'T':
            sort_books_title(bookDict)
        elif userInput == 'R':
            while True: # Ask the user if they want ascending or descending order
                print("\nA)scending   D)escending    RE)turn")
                userInput = input("Enter the upper-case letter to the left of the bracket of the option you want: ")
                if userInput == 'A':
                    sort_books_ascending_rate(bookDict)
                elif userInput == 'D':
                    sort_books_descending_rate(bookDict)
                elif userInput == 'RE':
                    break
                else:
                    __invalidCommand()
        elif userInput == 'P':
            sort_books_publisher(bookDict)
        elif userInput == 'C':
            sort_books_category(bookDict)
        elif userInput == 'PA':
            sort_books_pageCount(bookDict)
        elif userInput == 'RE':
            break
        else:
            __invalidCommand()
        
book_dict = load_dataset('Google_Books_Dataset.csv')
sortBookCall(book_dict)