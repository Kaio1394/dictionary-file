from enum import Enum
from robot.api.deco import keyword
import os
from generate_lib import generate_email_random

class Type_variable(Enum):
        STR = "str("
        INT = "int("
        LINE_BREAK = "\n"
        
class Dictionary_file():
    def __init__(self):
        self.STR = Type_variable.STR.value
        self.INT = Type_variable.INT.value
        self.LINE_BREAK = Type_variable.LINE_BREAK.value  
        self.NOT_FOUND = "Not found" 
        self.OK = "OK"
   
    def create_dict_by_file_txt(self, name_file: str, full_path: str = None) -> dict:
        if full_path is None:
            arq =  open(os.path.dirname(__file__) + f"/{name_file}", 'r')
        elif full_path is not None and name_file == "":
            arq =  open(f"{full_path}", 'r')
        lines = arq.readlines()
        dict_ = dict()
        for line in lines:
            if line is not None and "=" in line:
                list_kys_values = ''.join(line.replace(' ', '')).split(',')
                for item in list_kys_values:
                    key = item.split('=')[0]
                    value = item.split('=')[1]  
                    if "@" in value:
                        value =  generate_email_random(1)
                    if self.LINE_BREAK in value: 
                        value = value.replace(self.LINE_BREAK, '')
                    if value.startswith(self.STR):
                        value = value.replace(self.STR, '').replace(')', '')
                    if value.startswith(self.INT):
                        value = int(value.replace(self.INT, '').replace(')', ''))                                                          
                    dict_.update({key: value})               
            else:
                break
        return dict_

    def upload_dicionary_class(self, dictionary: dict, **keys_values) -> str:
        for key, value in keys_values.items():
            if key in dictionary.keys():
                continue
            else:
                raise Exception(f'Dictionary not contains key: {key}')
        for key, value in keys_values.items():
            dictionary[key] = value 
        return self.OK

@keyword("CREATE DICT BY FILE TXT")
def create_dictionary(file_name: str, full_path: str = None) -> dict:
    dictionary = Dictionary_file()
    return dictionary.create_dict_by_file_txt(file_name, full_path)       

@keyword("UPDATE DICTIONARY")
def upload_dicionary(dictionary: dict, **keys_values) -> str:
    dictionary_class = Dictionary_file()
    return dictionary_class.upload_dicionary_class(dictionary, **keys_values)