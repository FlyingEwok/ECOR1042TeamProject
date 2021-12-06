# Team T-55:
# Nicholas Garth 101227727
# Divya Dushyanthan 101221637
# Dylan Fortier 101221463
# Spencer Green 101196310

# Function 1
def print_dictionary_category(category: str, dict: dict) -> int:
    """Wrote by: Nicholas Garth 101227727
    Returns the number of books in a given category of a given book dictionary. As well prints the list of books in the category
    >>> print_dictionary_category("Superheroes", load_dataset(readfile('Google_Books_Dataset.csv')))
    The category Superheroes has 5 books. This is the list of books in the category Superheroes:

    {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'rating': '4.4', 'publisher': 'Marvel Entertainment', 'pageCount': '128', 'language': 'English'}
    {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': '4.1', 'publisher': 'DC', 'pageCount': '164', 'language': 'English'}
    {'title': 'Spider-Verse: Volume 1', 'author': 'Dan Slott', 'rating': '4.4', 'publisher': 'Marvel Entertainment', 'pageCount': '624', 'language': 'English'}
    {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'rating': '4.2', 'publisher': 'DC Comics', 'pageCount': '448', 'language': 'English'}
    {'title': 'Spider-Man: Anti-Venom', 'author': 'Dan Slott', 'rating': '4', 'publisher': 'Marvel Entertainment', 'pageCount': '96', 'language': 'English'}
    """
    # Count the number of books in the category
    count = 0
    numBooks = 0 # A variable the soul purpose of is to return the number of books
    for book in dict[category]:
        count += 1
    # Print the following
    print(f"The category {category} has {count} books. This is the list of books in the category {category}:\n")
    # Use counter to list and print each book in category
    for book in dict[category]:
        print(dict[category][count-1]) # Subtract 1 from count due to dictionaries counting starting at zero instead of one
        if count >=0:
            numBooks += 1 # As count value drops increase the numBooks value so the number of books isn't lost
            count -= 1
    return numBooks

# Function 2
def add_book(book_dict: dict, new_book_data: tuple) -> dict:
    """
    Function designed by Spencer Green.
    Returns a dictionary containing original sets of book data, with the addition of a new book's data set when given the book dictionary that the new book should be added to, and all seven data requirements of the new book(required data includes: "title", "author", rating, "publisher", "category", "page_count", and "language").
    >>>add_book(load_dataset(readfile("Google_Books_Dataset.csv")), ('Old Yeller', 'Fred Gipson', '4.3', 'HarperCollins', 'Fiction', '144', 'English'))
    {...
    'Fiction': [...{'title': 'Old Yeller', 'author': 'Fred Gipson', 'rating', '4.3', 'publisher': 'HarperCollins', 'pageCount': '288', 'language': 'English'}...], 
    ...}
    """
    (title, author, rating, publisher, category, pageCount, language) = new_book_data #unpacks the book data given as the parameter for easy access to each value.
    
    new_book_dict = {'title': title, 'author': author, 'rating': rating, 'publisher': publisher, 'pageCount': pageCount, 'language': language} #Creates a new dictionary based on the new book data passed through the function
    book_dict[category] += [new_book_dict] #Adds the dictionary containing the new book's data set to book_dict. The placement of the new dictionary will be determined by the category of the book(as the key of the individual dictionaries are categories/genres).
    if new_book_dict in book_dict[category]:
        print("The Book Has Been Added Correctly") #Prints a statement saying the book has been added correctly.
    else:
        print("There Was an Error Adding the Book")
    return book_dict 

# Function 3
def remove_book(title : str , category : str, dictionary : dict ) -> dict :
    """Wrote by: Divya Dushyanthan 101221637
    Returns the dictionary with indicated book removed aswell as if the fuction had sucessfully
    removed the book or not.
    >>>remove_book ("Antiques Roadkill: A Trash 'n' Treasures Mystery","Fiction", load_dataset(readfile('Google_Books_Dataset.csv')))
    The book has been removed correctly
    >>>remove_book ("Harry Potter", "Fantasy", load_dataset(readfile('Google_Books_Dataset.csv')))
    There was an error removing the book. Book not found.'    
    """
   
    books = dictionary[category]
    
    for values in books :
        find_book = values.get("title")
        if title == find_book :
            dictionary[category].remove(values)
            print(" The book has been removed correctly")
            return dictionary
            
    else:
        print("There was an error removing the book. Book not found")
        return dictionary 

# Function 4
def get_books_by_rate(rating: int, dataset:dict)->dict:
    """Wrote by: Dylan Fortier 101221463
    Returns a dictionary with all the books for the given rating. It will also
    print the information of all the books for the given rate.
    
    >>> get_books_by_rate(5, load_dataset(readfile('Google_Books_Dataset.csv')))
    Title: Final Option: 'The best one yet'
    Author: Clive Cussler
    Rating: 5
    Publisher: Penguin UK
    Pagecount: 400
    Language: English
    Genre: Fiction
    ...
    {'Books with a rating of: 5': [{'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'rating': '5', 'publisher': 'Penguin UK', 'pageCount': '400', 'language': 'English', 'genre': 'Fiction'},...]}
    """
    new_list = [] # new list for putting the rearranged book dictionaries into it
    rate_sort = [] # sorted list by rate of book dictionaries
    # rearrange the order of the dictionary(so genere is in the individual book dictionaries
    for genere in dataset: # access key by genere
        for dictionary in dataset[genere]: # access book dictionaries
            dictionary.update({'genre':genere}) # add genere key into the dictionary
            new_list.append(dictionary) # add the new dictionary into the new list
    # organizing by book rating
    for dictionary in new_list: # access the new dictionaries
        if len(dictionary.get('rating')) > 0: # if the rating isnt empty
            if rating <= float(dictionary.get('rating')) < rating + 1: # if the rating is between the lower and upper rating limit
                rate_sort.append(dictionary) # add the dictionary to the rate sorted list
                for item in dictionary: # access objects in book dictionaries that are in the rating inputted
                    print(item.capitalize() + ':', dictionary[item]) # print the info of each book for the given rate
        else: # if the string is empty
            None # skip the book
    final_dictionary = {} # empty dictionary for new sorted by rate dictionaries
    final_dictionary['Books with a rating of: '+ str(rating)] = rate_sort # add the rate sorted books
    return final_dictionary # return dictionary of rate sorted books

# Function 5
def find_books_by_title(title: str, dict: dict) -> bool:
    """Wrote by: Nicholas Garth 101227727
    Returns a boolean on if a book exsits or not, also prints to the console if it exsits or not
    >>> find_books_by_title("Antiques Roadkill: A Trash 'n' Treasures Mystery", load_dataset(readfile('Google_Books_Dataset.csv')))
    The Book has been found!
    True
    >>> find_books_by_title("The Legend Of Mr. Sourman", load_dataset(readfile('Google_Books_Dataset.csv')))
    The Book has NOT been found!
    False
    """
    # Grab genre keys and cycle through every index seraching for the book
    genres = dict.keys()
    for i in genres:
        for book in dict[i]:
            found = book["title"] == title
            if found:
                print("The Book has been found!")
                return True
    print("The Book has NOT been found!")
    return False

# Function 6
def get_books_by_author(book_dict: dict, author_name: str) -> list:
    """
    Function Designed by Spencer Green
    Returns a list of book titles written by a given author, from a given dictionary containing the datasets of different books where said author and corresponding book titles are stored. 
    >>>get_books_by_author(load_dataset(readfile('Google_Books_Dataset.csv')), "Agatha Christie")
    The author Agatha Christie has published the following books: 
    1-The Red Signal: An Agatha Christie Short Story 
    2-The Mysterious Affair at Styles 
    3-And Then There Were None 
    ['The Red Signal: An Agatha Christie Short Story', 'And Then There Were None', 'The Mysterious Affair at Styles'] #What to test for 
    """
    author_title_lst = []
    
    for key in book_dict: #Accesses each key, which are categories.
        for value in book_dict[key]: #for each key, the values are accessed to iterate through each book data set stored as a dictionary.
            if value['author'] == author_name: #Continues if the value stored under a books' 'title' key matches the given author_name. 
                if value['title'] not in author_title_lst: #Adds the title of the book written by the given author to author_title_list, if the book title isn't already in the list.
                    author_title_lst.append(value['title'])
  
    print("The author " + author_name + " has published the following books:")
    for i in range(len(author_title_lst)): #This loop prints out the numbered sequence of book titles written by the given author.
            print(str(i + 1) +  "-" + author_title_lst[i])
    return author_title_lst

# Function 7
def get_books_by_publisher(publisher: str , dictionary : dict) -> list:
    """Wrote by: Divya Dushyanthan 101221637
    Returns a list with the book titles found in the dictionary that match the publisher passed
    >>>get_books_by_publisher("Hachette UK", load_dataset(readfile('Google_Books_Dataset.csv')))
    The publisher Hachette UK has published the following books:
    1 - Sword of Destiny: Witcher 2: Tales of the Witcher
    2 - The Guardians: The explosive new thriller from international bestseller John Grisham
    3 - "The Name of the Wind: The Kingkiller Chronicle:, Book 1"
    4 - 'Salem's Lot
    ...
    """
   
    publisher_lst = []
    titles_publisher_lst = []
    
    for key in dictionary: #Loops through keys in dictionary
        for book in dictionary[key] : #checks for the book info 
            if book['publisher'] == publisher: #checks to see if the publisher it is at matches the publisher passed
                book.get("publisher")# gets all the info from the book found by publisher
                if book not in publisher_lst: #checks to see if book has been added yet or not
                    publisher_lst.append(book) # adds the book info into a list
                    
                    
   
    for item in publisher_lst: #looks for book in list
        title = item.get("title")# gets titles of books
        titles_publisher_lst.append(title) #adds titles to a new list
                   
           
    display = ('The publisher {0} has published the following books:'.format(publisher))
    print(display)
    
    i = 1 #start of list
    for titles in titles_publisher_lst:
        print(i, "-", titles) # prints out numbered list of books
        i+=1
                              

       
    return titles_publisher_lst

# Function 8
def check_category_and_title(category:str, title:str, dataset:dict)->bool:
    """Wrote by: Dylan Fortier 101221463
    Returns a boolean which is True if the books title exists in the dictionary
    for the given category, and otherwise returns False.
    
    >>> check_category_and_title('Humor', 'Tall Tales and Wee Stories: The Best of Billy Connolly', get_books_by_rate(5, load_dataset(readfile('Google_Books_Dataset.csv'))))
    The category Humor has the book title Tall Tales and Wee Stories: The Best of Billy Connolly.
    True
    """
    for genere in dataset: # access genere keys
        if genere == category: # if the genere is the category we are looking for
            for dictionary in dataset[genere]: # access teh dictionaries for the genere/category
                for header in dictionary: # access the headers in the dictionary
                    if header == 'title': # if the header is title
                        if dictionary.get(header) == title: # if the value of the header is the title we are looking for
                            print('The category', category, 'has the book title', title + '.') # print if the book is found in the category
                            return True # returns True that the book is in the genere
                        else: # if the title is not in the dictionary
                            print('The category', category, 'does not have the book title', title + '.') # print that there is no book in that genere
                            return False # returns False that the book is not in the genere
    print('The category', category, 'does not exist.') # prints that the genere does not exist
    return False # returns false that the genere does not exist

# Function 9
def all_categories_for_book_title(title: str, dict: dict) -> list:
    """Wrote by: Nicholas Garth 101227727
    Returns a list with all genres a book is classified as, as well print the genres
    >>> all_categories_for_book_title("Antiques Chop", load_dataset(readfile('Google_Books_Dataset.csv')))
    The book title "Antiques Chop" has the following categories:

    1- Fiction
    2- Detective
    3- Mystery
    """
    print(f'The book title "{title}" has the following categories:\n')
    numBooks = 0
    bookGenres = []
    # Grab genre keys and cycle through every index seraching for the book
    genres = dict.keys()
    for i in genres:
        for book in dict[i]:
            found = book["title"] == title
            if found:
                numBooks += 1 # Keep track of the book amount to label each genre in print
                print(f"{numBooks}- {i}")
                bookGenres.append(i)
    return bookGenres

# Function 10
def get_books_by_category(book_dict: dict, category_name: str) -> list:
    """
    Function Designed by Spencer Green
    Returns a list of book title names which fall under a given book category from a dictionary containing the individual data sets of each book. 
    >>>get_books_by_category(load_dataset(readfile("Google_Books_Dataset.csv")), "Adventure")
    The category Adventure has the following books: 
    1-Sword of Destiny: Witcher 2: Tales of the Witcher 
    2-A Feast for Crows (A Song of Ice and Fire, Book 4) 
    3-After Anna 
    4-The Way Of Shadows: Book 1 of the Night Angel 
    5-A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, 
    A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance 
    with Dragons (A Song of Ice and Fire) 
    6-Edgedancer: From the Stormlight Archive 
    7-The Malady and Other Stories: An Andrzej Sapkowski Sampler
    ['Sword of Destiny: Witcher 2: Tales of the Witcher', '"A Feast for Crows (A Song of Ice and Fire, Book 4)"', 'After Anna', 'The Way Of Shadows: Book 1 of the Night Angel', '"A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)"', 'Edgedancer: From the Stormlight Archive', 'The Malady and Other Stories: An Andrzej Sapkowski Sampler'] #What to test
    """
    book_title_lst = []

    for key in book_dict: #Accesses the each category(each key)
        if key == category_name: #Continues if the category matches the category given
            for value in book_dict[key]: #This loop accesses the dictionaries under the given category and adds each book title to the book_title_lst.
                if value['title'] not in book_title_lst:
                    book_title_lst.append(value['title'])
                    
    print("The category " + category_name + " has the following books:")
    for i in range(len(book_title_lst)): #This loop prints out the numbered sequence of book titles under the given category.
            print(str(i + 1) +  "-" + book_title_lst[i])    
    return book_title_lst

# Function 11
def get_book_by_category_and_rate(category : str , rate : int , dictionary : dict) -> list:
    """Wrote by: Divya Dushyanthan 101221637
    Returns a list of books that are within the range of the rating passed and in the category passed.
    >>>get_book_by_category_and_rate("Fiction", 4 , load_dataset(readfile('Google_Books_Dataset.csv')))
    The category Fiction and the rate 4 has the following books:
    1 - "The Painted Man (The Demon Cycle, Book 1)"
    2 - Edgedancer: From the Stormlight Archive
    3 - Sword of Destiny: Witcher 2: Tales of the Witcher
    4 - After Anna
    ....
    """
    
    category_lst = [] 
    rate_lst = []
    title_lst = []
    
       
    for key in dictionary : #looks through keys of dictionary
        if key == category : #Checks if key and category are equivalent
            for value in dictionary[key]: #Looks for the values in the category
                category_lst.append(value) #adds all the books info  in the category into a list            
                
    for book in category_lst: #checks for book info inside of the list
        if len(book.get('rating')) > 0 : #gets ratings in the category and checks for exsisting ratings since some books have no ratings
            if rate <= float(book.get('rating')) < (rate + 1) : #compares the ratings found to see if they are within the range of the rating +1 passed in the function  
                rate_lst.append(book) #adds all the books that fall into the rating into a list
    
    for item in rate_lst: #looks for books in rate list
        title = item.get("title") #gets the title from book
        title_lst.append(title) #adds it to a new list
        
                
    display = ('The category {0} and the rate {1} has the following books:'.format(category,rate))
    print(display)
    
    i = 1 # start number for list
    for book_title in title_lst: 
        print(i, "-", book_title) #Prints out a numbered list of books
        i+=1
                   
    
    return title_lst

# Function 12
def get_author_categories(authors_name:str, dataset:dict)->list:
    """Wrote by: Dylan Fortier 101221463
    Returns a list of catergories for the given author, and prints what categories
    the author has published books under as a numbered list.
    
    >>>get_author_categories('Barbara Allan', get_books_by_rate(5, load_dataset(readfile('Google_Books_Dataset.csv'))))
    The author Barbara Allan has published books under the following categories
    1 - Fiction
    2 - Detective
    3 - Mystery
    ['Fiction', 'Detective', 'Mystery']
    """
    authors_categories = [] # empty list for authors published books in categories
    for genere in dataset: # access generes of the dataset
        for dictionary in dataset[genere]: # access the dictionaries of the generes
            if dictionary['author'] == authors_name: # if the dictionary has the authors name in it
                if genere not in authors_categories: # if the genere is not in the list
                    authors_categories.append(genere) # add the genere to the list
                else: # if the genere ahs already been added
                    None # do nothing
    print('The author ' + authors_name + ' has published books under the following categories') # print that the author has published in the categories that are in the authors_categories list
    for length in range(len(authors_categories)): # iterate through the authors_categories list
        print(length + 1, '-', authors_categories[length]) # print each category that the author has published in(+1 is to start at number 1 in the printed list)
    return authors_categories # return the authors_categories list


