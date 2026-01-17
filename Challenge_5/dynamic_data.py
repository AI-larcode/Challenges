"""
Implement a proxy class that transforms a standard Python dictionary into a dynamic object, 
allowing attribute access via dot notation (e.g., data.key) instead of bracket notation (data['key']).
The wrapper must handle nested structures recursively, manage naming conflicts with Python keywords, 
and ensure the data remains read-only.
"""

from collections import abc
import keyword

class DynamicData:
    def __init__(self, mapping):
        self.__data = dict(mapping)
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return DynamicData.build(self.__data[name])
        
    def __dir__(self):
        return self.__data.keys()
    
    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

    
raw_data = {
    'name': 'Python Store',
    'class': 'Standard',
    'details': {'owner': 'Admin', 'established': 1991}
}

data = DynamicData(raw_data)
print(data)
print(data.name)           
print(data.class_)         
print(data.details.owner)  

# To improve this code we can use the __new__ function instead of the build one