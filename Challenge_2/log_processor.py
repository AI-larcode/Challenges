"""
Challenge Description
Develop a memory-efficient tool capable of processing massive log files (e.g., multi-gigabyte server logs)
without exhausting the system's RAM. The objective is to extract specific information based on alert levels
and perform a word frequency analysis on the filtered messages.
"""

from collections import Counter

PUNCTUATION_TABLE = str.maketrans('', '', ".,¿?¡!:;'")

def log_processor(file_name:str , alert_level:str) -> list[tuple[str, int]]:
    """
    Process logs lazily to count word frequency in messages 
    of a specific alert level.
    """
    words_count = Counter()

    with open(file_name, 'r', encoding='utf-8') as f:

        log_parts = (line.split('|') for line in f if '|' in line)

        cleaned_messages = (
            parts[2].lower().translate(PUNCTUATION_TABLE)
            for parts in log_parts 
            if parts[1].strip() == alert_level
        )
    
        for message in cleaned_messages:
            words_count.update(message.split())

    return words_count.most_common(5)
    
print(log_processor('test.txt', 'ERROR'))