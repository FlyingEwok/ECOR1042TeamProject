# Team T-55:
# Wrote by:
# Nicholas Garth 101227727
# Reviewed by:
# Divya Dushyanthan 101221637
# Dylan Fortier 101221463
# Spencer Green 101196310

from typing import List
import re

# Based off Lecture 3(1): Iterative Development and Text Processing, slide 10
def readfile(filename: str) -> List[str]:
    """Wrote by: Nicholas Garth 101227727
    Reads file from filename and returns a list of every line of the file
    >>> readfile(hi.txt)
    ['Hi']
    """
    infile = open(filename, "r",encoding="UTF-8")
    records = []
    for line in infile:
        records.append(line.strip())
    infile.close()
    return records

# Comma splitting regex based off of following article
# https://newbedev.com/splitting-on-comma-outside-quotes
def load_dataset(dataset: str) -> dict:
    """Wrote by: Nicholas Garth 101227727
    Returns sorted dict by genere category from a list of records with comma seperated values
    >>> load_dataset(readfile('Google_Books_Dataset.csv'))["Superheroes"]
    [{'title': 'Spider-Man: Anti-Venom', 'author': 'Dan Slott', 'rating': '4', 'publisher': 'Marvel Entertainment', 'pageCount': '96', 'language': 'English'}, {'title': 'Watchmen (2019 Edition)', 'author': 'Alan Moore', 'rating': '4.2', 'publisher': 'DC Comics', 'pageCount': '448', 'language': 'English'}, {'title': 'Spider-Verse: Volume 1', 'author': 'Dan Slott', 'rating': '4.4', 'publisher': 'Marvel Entertainment', 'pageCount': '624', 'language': 'English'}, {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'rating': '4.1', 'publisher': 'DC', 'pageCount': '164', 'language': 'English'}, {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'rating': '4.4', 'publisher': 'Marvel Entertainment', 'pageCount': '128', 'language': 'English'}]
    """
    records = readfile(dataset)
    headings = records[0].split(",") # Row zero is the header row in csv
    categoryIndex = headings.index('generes')
    bookDictionary = {}
    for i in range(1, len(records)): # Start at 1 to skip headers
        recordFields = re.split(r",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", records[i]) # Comma Splitting Regex
        book = {}
        for j in range(1, len(recordFields)): # Start at 1 to skip record id
            if not j == categoryIndex:
                book[generateKey(headings[j])] = recordFields[j] 
        # Sort books into bins based on categories
        if bookDictionary.get(recordFields[categoryIndex]) == None:
            bookDictionary[recordFields[categoryIndex]] = []
        if book not in bookDictionary[recordFields[categoryIndex]]: # Check for duplicate books
            bookDictionary[recordFields[categoryIndex]].append(book)
    return bookDictionary  

# Based off of the following stackoverflow post, made by user jbaiter
# https://stackoverflow.com/questions/19053707/converting-snake-case-to-lower-camel-case-lowercamelcase
def to_camel_case(snake_str: str) -> str:
    """Wrote by stackoverflow user jbaiter
    Converts string with snake case into string with camel case
    >>> to_camel_case("to_camel_case")
    toCamelCase
    """
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])

def generateKey(string: str) -> str:
    """Wrote by: Nicholas Garth 101227727
    A convienient method of generating dict keys
    >>> generateKey("page_count")
    pageCount
    """
    return to_camel_case(string)

