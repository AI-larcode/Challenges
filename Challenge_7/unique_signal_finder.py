"""
In data stream processing, it's common to look for the first occurrence of a unique element. 
Given a long string (representing a signal or a stream of characters), write a function that 
finds the index of the first character that does not repeat anywhere else in the string. 
If every character repeats, return -1.
"""
from collections import Counter

def first_unique_char(char_list: list[str]):
    char_dict = Counter(char_list)

    char_index_dict = {}
    for index in range(len(char_list)):
        char_index_dict[char_list[index]] = (char_dict[char_list[index]], index)

    count_index_list = char_index_dict.values()
    for count_index in count_index_list:
        if count_index[0] == 1:
            return count_index[1]
    return -1

print(first_unique_char(list("entrevista")))

def opt_first_unique_char(char_list: str):
    char_dict = Counter(char_list)

    for index, char in enumerate(char_list):
        if char_dict[char] == 1:
            return index
    return -1

print(opt_first_unique_char("entrevista"))
