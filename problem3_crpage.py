# STAT/CS 287
# HW 01
#
# Name: Cecily Page
# Date: September 11 2018

import urllib.request
from os import path
from string import punctuation
import collections
import operator


def words_of_book():
    """Download `A tale of two cities` from Project Gutenberg. Return a list of
    words. Punctuation has been removed and upper-case letters have been
    replaced with lower-case.
    """
    
    # DOWNLOAD BOOK:
    url = "http://www.gutenberg.org/files/98/98.txt"
    req = urllib.request.urlopen(url)
    charset = req.headers.get_content_charset()
    raw = req.read().decode(charset)
    
    # PARSE BOOK
    raw = raw[750:] # The first 750 or so characters are not part of the book.
    
    # Loop over every character in the string, keep it only if it is NOT
    # punctuation:
    exclude = set(punctuation) # Keep a set of "bad" characters.
    list_letters_noPunct = [ char for char in raw if char not in exclude ]
    
    # Now we have a list of LETTERS, *join* them back together to get words:
    text_noPunct = "".join(list_letters_noPunct)
    # (http://docs.python.org/3/library/stdtypes.html#str.join)
    
    # Split this big string into a list of words:
    list_words = text_noPunct.strip().split()
    
    # Convert to lower-case letters:
    list_words = [ word.lower() for word in list_words ]
    
    return list_words


def read_file_by_word(file_path: str):

    with open(file_path, 'r') as file_name:
        list_words = file_name.read().split()

    return list_words


def use_cashed(file_path):

    if path.exists(file_path):
        list_words = read_file_by_word(file_path)
        return list_words
    else:
        with open(file_path, 'w') as file:
            for word in words_of_book():
                file.write(word + ' ')
        return words_of_book()


def count_most_common(word_list):
    all_words = {}
    for word in word_list:
        if word not in all_words:
            all_words[word] = 1
        elif word in all_words:
            all_words[word] += 1

    sorted_word_count = sorted(list(all_words.items()), key=lambda x: x[1], reverse=True)

    return sorted_word_count


word_list = use_cashed('tale_of_two_cities.txt')
word_count = count_most_common(word_list)
### 3.2
most_used_words = word_count[:100]
print(most_used_words)

### 3 bonus
print(collections.Counter(word_list))
