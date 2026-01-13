import itertools
from typing import Union

class LogStream:
    def __init__(self, file_name, alert_level):
        self.file_name = file_name
        self.alert_level = alert_level

    def __iter__(self):
        PUNCTUATION_TABLE = str.maketrans('', '', ".,¿?¡!:;'")
        with open(self.file_name, 'r') as f:
            log_parts = (line.split('|') for line in f)

            clean_messages = (part[2].lower().translate(PUNCTUATION_TABLE)
                            for part in log_parts
                            if part[1].strip() == self.alert_level)
            for message in clean_messages:
                yield message

    def __repr__(self):
        return f'LogStream({self.file_name!r}, {self.alert_level!r})'
    
    def __getitem__(self, index: Union[int, slice]): # Union means that the value can be both types
        if isinstance(index, int):
            return next(itertools.islice(self.__iter__(), index, index + 1))
        elif isinstance(index, slice):
            return list(itertools.islice(self.__iter__(), index.start, index.stop, index.step))
        else:
            raise TypeError("Index must be int or slice")
        
L = LogStream('Challenge_3/test.txt', 'ERROR')
for i in L:
    print(i)
