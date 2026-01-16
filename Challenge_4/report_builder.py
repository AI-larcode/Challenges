"""
Refactor a data-processing class to support multiple export formats (JSON and Plain Text) 
without bloating the core logic. The goal is to leverage Multiple Inheritance and Mixin Classes to create 
a pluggable architecture where presentation logic is decoupled from data logic.
"""


import json

class JSONExportMixin:

    def to_json(self):
        return json.dumps(self.to_dict()) #To_dict() should be defined in another mixin

class PlainTextExportMixin:

    def to_plain_text(self) -> str:
        
        data = self.to_dict()
        lines = [f"{'WORD':<15} | {'FREQUENCY':>10}"]
        lines.append("-" * 28)
        
        for word, count in data.items():
            lines.append(f"{word:<15} | {count:>10}")
            
        return "\n".join(lines)
    
class LogStream(JSONExportMixin, PlainTextExportMixin):
    def __init__(self, file_name, alert_level):
        self.file_name = file_name
        self.alert_level = alert_level
    #...