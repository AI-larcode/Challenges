"""
Implement an algorithm to group a list of strings into sub-lists where each sub-list contains 
words that are anagrams of each other. Anagrams are words that contain the same characters with 
the same frequency but in a different order.
"""

def anagram_joiner(word_list: list[str]) -> list[list[str]]:
    word_dict = {}
    for word in word_list:
        if not tuple(sorted(word)) in word_dict:
            word_dict[tuple(sorted(word))] = [word]
        else: 
            word_dict[tuple(sorted(word))].append(word)

    anagram_list = list(word_dict.values())
    return(anagram_list)

print(anagram_joiner(["comer", "romer", "mecer", "creme", "perro", "remer", "merco"]))
