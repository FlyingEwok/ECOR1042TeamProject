# Team T-55:
# Nicholas Garth 101227727
# Divya Dushyanthan 101221637
# Dylan Fortier 101221463
# Spencer Green 101196310

# Helper Functions
# Based off of ECOR1042 Lecture 8: Sorting Algorithms with Python (Slide 9), 
# which is based off GeeksforGeeks https://www.geeksforgeeks.org/bubble-sort/
def bubbleSort(arr: list, keyToSortBy: str = None) -> None:
    """Wrote by Nicholas Garth 101227727
    Performs a basic bubble sort on a dictionary or array; performs an in place sort on the list
    >>> arr = ['Banana', 'Carrot', 'Apple', 'Doughnut'] 
    >>> bubbleSort(arr)
    >>> print(arr)
    ['Apple', 'Banana', 'Carrot', 'Doughnut']
    >>> arr = [{'title': 'The Legend of Mr. Sourman II', 'author': 'Doughnut'}, {'title': 'Mr. Sourman is Dead here comes Donkey!', 'author': 'Doughnut'}]
    >>> bubbleSort(arr, 'title')
    >>> print(arr)
    [{'title': 'Mr. Sourman is Dead here comes Donkey!', 'author': 'Doughnut'}, {'title': 'The Legend of Mr. Sourman II', 'author': 'Doughnut'}]
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if (keyToSortBy and (arr[j][keyToSortBy] > arr[j+1][keyToSortBy])) or (not keyToSortBy and (arr[j] > arr[j+1])):
                arr[j], arr[j+1] = arr[j+1], arr[j]

def __sort_books_title(books: list) -> list:
    """Wrote by Nicholas Garth 101227727
    Returns book sorted by title; performs an in place sort on the list
    >>> arr = [{'title': 'The Legend of Mr. Sourman II', 'author': 'Doughnut'}, {'title': 'Mr. Sourman is Dead here comes Donkey!', 'author': 'Doughnut'}]
    >>> __sort_books_title(arr)
    >>> print(arr)
    [{'title': 'Mr. Sourman is Dead here comes Donkey!', 'author': 'Doughnut'}, {'title': 'The Legend of Mr. Sourman II', 'author': 'Doughnut'}]
    """
    bubbleSort(books, 'title')
    return books

def __printBooks(books: list, category: str = None):
    """Wrote by Nicholas Garth 101227727
    Print books out to shell
    >>> arr = [{'title': 'The Legend of Mr. Sourman II', 'author': 'Doughnut', 'rating': '4.5', 'publisher': 'Donkey Studios', 'pageCount': '669', 'language': 'English'}, {'title': 'Mr. Sourman is Dead here comes Donkey!', 'author': 'Doughnut', 'rating': '4.5', 'publisher': 'Donkey Studios', 'pageCount': '669', 'language': 'English'}]
    >>> __printBooks(arr)
    The Legend of Mr. Sourman II by Doughnut (pp. 669), published by Donkey Studios in English; rated: 4.5
    Watchmen (2019 Edition) by Doughnut (pp. 669), categorized under genre Superheroes, published by Donkey Studios in English; rated: 4.5
    """
    if category:
        print(f"\n=== {category} ===")
    for book in books:
        if 'generes' in book: # Check if genres is in the book dict
            print(f"{book['title']} by {book['author']} (pp. {book['pageCount']}), categorized under genre {book['generes']}, published by {book['publisher']} in {book['language']}; rated: {book['rating']}")
        else:
            print(f"{book['title']} by {book['author']} (pp. {book['pageCount']}), published by {book['publisher']} in {book['language']}; rated: {book['rating']}")

def getBookList(genres: list, dict: dict) -> list:
    """Returns a list of book dictionaries"""
    bookData = []
    # Get list of all books
    for genre in genres:
        for book in dict[genre]:
            book.update({'generes':genre}) #re inserts genre into dictionary
            bookData.append(book)
    return bookData

# Sorting Functions 
# Function 1
def sort_books_title(dict: dict) -> list:
    """Wrote by Nicholas Garth 101227727
    Returns dataset sorted by title
    >>> from T55_P1_load_data import load_dataset, readfile
    >>> sort_books_title(load_dataset(readfile('Google_Books_Dataset.csv')))
    "A Feast for Crows (A Song of Ice and Fire, Book 4)" by George R.R. Martin (pp. 864), categorized under genre Fiction, published by HarperCollins UK in English; rated: 4.5
    ...
    """
    print("\n_____\nBeginning Function 1:\n")
    genres = dict.keys()

    # Get list of all books
    bookData = getBookList(genres, dict)
    __sort_books_title(bookData)
    __printBooks(bookData)
    return bookData # Return the list

# Function 2
def sort_books_ascending_rate(dataset:dict)->list:
    """Wrote by Dylan Fortier 101221463 
    Returns a list with the book data stored as a dictionary where the books are sorted by the rate in ascending order.
    
    >>>sort_books_by_ascending_rate(load_dataset(readfile("Google_Books_Dataset.csv")))
    [{'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': '', 'publisher': 'Hachette UK', 'pageCount': '384', 'language': 'English', 'genere': 'Fiction'}, ..., {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': '5', 'publisher': 'HarperCollins UK', 'pageCount': '40', 'language': 'English', 'genere': 'Traditional'}]
    """
    genres = dataset.keys()
    #create list with book data
    book_list = getBookList(genres, dataset)
    #bubble sort
    number_of_books = len(book_list) # number of books in the list
    for book in range(number_of_books): # iterate over each book
        for book_index in range(0, number_of_books - book - 1): #
            if book_list[book_index].get('rating') > book_list[book_index + 1].get('rating'): # if the first books rating is greater than the second books rating
                book_list[book_index], book_list[book_index + 1] = book_list[book_index + 1], book_list[book_index] # swap the books indexes
            elif book_list[book_index].get('rating') == book_list[book_index + 1].get('rating'): # if the first books rating is greater than the second books rating
                if book_list[book_index].get('title') > book_list[book_index + 1].get('title'): # if the first books rating is greater than the second books rating
                    book_list[book_index], book_list[book_index + 1] = book_list[book_index + 1], book_list[book_index] # swap the books indexes
    print(book_list) # print the rate sorted list
    return book_list

# Function 3
def sort_books_descending_rate(dictionary) -> list :
    
    """Wrote by: Divya Dushyanthan 101221637
    Returns a list of books in descending rate
    >>>sort_books_descending_rate(dictionary)
    
    [{'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': '5', 'publisher': 'Penguin UK', 'pageCount': '400', 'language': 'English', 'genre': 'Fiction'}, {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'rating': '5', 'publisher': 'HarperCollins UK', 'pageCount': '40', 'language': 'English', 'genre': 'Fiction'}, {'title': 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'author': 'Michael Sincere', 'rating': '5', 'publisher': 'Simon and Schuster', 'pageCount': '224', 'language': 'English', 'genre': 'Economics'} ....]

    
    """
    genres = dictionary.keys()
    dictionary_lst = getBookList(genres, dictionary) #new dictionary list    
    
    dict_length = len(dictionary_lst) #length of dictionary list
    
    for i in range(dict_length - 1) : #checks to the last position of the dictionary list
        for j in range (dict_length - 1): 
            if len(dictionary_lst[j].get('rating')) == '' : #checks for books with no rating
                dictionary_lst[j]['rating'] = '0' #sets empty strings to 0
            if dictionary_lst[j]['rating'] < dictionary_lst[j +1]['rating']: #compares two books at a time to check which rating is greater
                dictionary_lst[j], dictionary_lst[j +1]= dictionary_lst[j+1], dictionary_lst[j] #swaps places if it is greater       
    print(dictionary_lst)
    return dictionary_lst

# Function 4
def sort_books_publisher(book_dict: dict) -> list:
    """
    Function Designed by Spencer Green
    Returns a list containing the dictionaries of book data sets in alphabetical order based on the publisher of the book, from a given dictionary containing the book data sets.
    >>>sort_books_publisher(load_dataset(readfile('Google_Books_Dataset.csv')))
    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': '', 'publisher': 'AMACOM', 'pageCount': '112', 'language': 'English'}, ... , {'title': '"The Lord of the Rings: The Fellowship of the Ring, The Two Towers, The Return of the King"', 'author': 'J. R. R. Tolkien', 'rating': '4.6', 'publisher': 'HarperCollins UK', 'pageCount': '1216', 'language': 'English'}, ... , {'title': 'Platform Revolution: How Networked Markets Are Transforming the Economy—and How to Make Them Work for You', 'author': 'Geoffrey G. Parker', 'rating': '4.5', 'publisher': 'W. W. Norton & Company', 'pageCount': '256', 'language': 'English'}]
    """
    genres = book_dict.keys()
    book_lst = getBookList(genres, book_dict)

    book_lst_len = len(book_lst)
    for i in range(book_lst_len):
        for j in range(book_lst_len-i-1):
            if book_lst[j].get('publisher') > book_lst[j+1].get('publisher'): 
                book_lst[j], book_lst[j+1] = book_lst[j+1], book_lst[j]
    for i in range(book_lst_len):
        for j in range(book_lst_len-i-1):                
            if book_lst[j].get('publisher') == book_lst[j+1].get('publisher'): 
                if book_lst[j].get('title') > book_lst[j+1].get('title'):
                    book_lst[j], book_lst[j+1] = book_lst[j+1], book_lst[j]            
    print(book_lst)  
    return book_lst 

# Function 5        
def sort_books_pageCount(book_dict: dict) -> list:
    """
    Function Designed by Spencer Green
    Returns a list containing the dictionaries of book data sets sorted by pageCount of the books in ascending order, with books of the same page count being sorted alphabetically by title, from a given dictionary containing the book data sets.
    >>>sort_books_pageCount(load_dataset(readfile('Google_Books_Dataset.csv')))
    [{'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': '', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'pageCount': '14', 'language': 'English'}, ... ,  {'title': '"The Girl in the Spider\'s Web: A Lisbeth Salander novel, continuing Stieg Larsson\'s Millennium Series"', 'author': 'David Lagercrantz', 'rating': '4.1', 'publisher': 'Vintage Crime/Black Lizard', 'pageCount': '416', 'language': 'English'}, ... , {'title': '"A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)"', 'author': 'George R.R. Martin', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'pageCount': '4544', 'language': 'English'}] 
    """
    genres = book_dict.keys()
    book_lst = getBookList(genres, book_dict)
    
    book_lst_len = len(book_lst)
    for i in range(book_lst_len):
        for j in range(book_lst_len-i-1):
            if int(book_lst[j].get('pageCount')) > int(book_lst[j+1].get('pageCount')): 
                book_lst[j], book_lst[j+1] = book_lst[j+1], book_lst[j]
    for i in range(book_lst_len):
        for j in range(book_lst_len-i-1):
            if int(book_lst[j].get('pageCount')) == int(book_lst[j+1].get('pageCount')): 
                if book_lst[j].get('title') > book_lst[j+1].get('title'): 
                    book_lst[j], book_lst[j+1] = book_lst[j+1], book_lst[j]            
    print(book_lst)  
    return book_lst 

# Function 6
def sort_books_category(dict: dict) -> list:
    """Wrote by Nicholas Garth 101227727
    Returns books sorted by category
    >>> from T55_P1_load_data import load_dataset, readfile
    >>> sort_books_category(load_dataset(readfile('Google_Books_Dataset.csv')))
    === Adventure ===
    "A Feast for Crows (A Song of Ice and Fire, Book 4)" by George R.R. Martin (pp. 864), published by HarperCollins UK in English; rated: 4.5
    "A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)" by George R.R. Martin (pp. 4544), published by HarperCollins UK in English; rated: 4.5
    After Anna by Alex Lake (pp. 416), published by HarperCollins UK in English; rated: 4.1
    Edgedancer: From the Stormlight Archive by Brandon Sanderson (pp. 226), published by Tor Books in English; rated: 4.8
    Sword of Destiny: Witcher 2: Tales of the Witcher by Andrzej Sapkowski (pp. 400), published by Hachette UK in English; rated: 4.8
    The Malady and Other Stories: An Andrzej Sapkowski Sampler by Andrzej Sapkowski (pp. 96), published by Hachette UK in English; rated: 4.8
    The Way Of Shadows: Book 1 of the Night Angel by Brent Weeks (pp. 688), published by Hachette UK in English; rated: 4.7
    ...
    """
    print("\n_____\nBeginning Function 6:")
    sortedDict = {}
    # Sort genres
    genres = list(dict.keys())
    bubbleSort(genres)
    # Sort books in each genre by title
    for genre in genres:
        sortedDict[genre] = __sort_books_title(list(dict[genre]))
        __printBooks(sortedDict[genre], genre) # Print the books in a fancy format
    sortedDictList = [sortedDict] # Put the dictionary into a list
    return sortedDictList # Return the list
    