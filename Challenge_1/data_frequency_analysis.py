"""
Challenge Description
Design a robust and efficient function to process large strings of text (such as IoT event logs or voice-to-text transcripts) 
to determine word frequency. The goal is to identify the top N most frequent words while ensuring the code remains readable,
maintainable, and highly performant by leveraging Python's internal optimization mechanisms.
"""

import string

def frequency_analysis(text: str, top_n: int):
    
    text_lowercase = text.lower()
    text_without_punctuation = ''.join(char for char in text_lowercase if char not in string.punctuation)
    text_list = text_without_punctuation.split()
    word_frecuency = {}
    for word in text_list:
        word_frecuency[word] = word_frecuency.get(word, 0) + 1 

    '''
    Using a dict comprehension with text_list.count(word) is inefficient because count() performs 
    a full linear scan of the list for every single word, resulting in O(n²) complexity.
    
    word_frecuency = {word: text_list.count(word) for word in set(text_list)}
    '''
    sorted_word_tuples = sorted(word_frecuency.items(), key=lambda item: item[1], reverse=True)
    top_n_words = sorted_word_tuples[:top_n]
    return top_n_words

print(frequency_analysis('Hola. HOLA, Que tal? que dices no es posible que eso sea cierto. NO', 4))

from collections import Counter

CHARS_TO_DELETE = ".,¿?¡!:;'"
PUNCTUATION_TABLE = str.maketrans('', '', CHARS_TO_DELETE)

def opt_frequency_analysis(text: str, top_n: int) -> list[tuple[str, int]]:
    """
    Find the most repeated words in a text after cleaning punctuation.

    Args:
        text: A plain text string.
        top_n: The number of top frequent words to return.

    Returns:
        A list of tuples, each containing a word and its frequency
    """

    
    clean_text = (text.lower().translate(PUNCTUATION_TABLE))
    return Counter(clean_text.split()).most_common(top_n)

print(opt_frequency_analysis('Hola. HOLA, Que tal? que dices no es posible que eso sea cierto. NO', 4))
