# this generator should be used with a currently existing table or in this case a list of lists
# it can generate a custom layout of custom columns 
## it should be able to generate various codes as similar sets of numbers and letters
## for example a 4 digit number code for medical diagnoses: 0020, 0021, 3324
## or a 2 alphabetical org designation: HP, BP, TR
## or a 5 letter alphanumeric code: HP2029, DX2044, PL5620
import random

# designate the amount of numeric characters
# the amount of alphabetic characters
# and which of those comes first or if the order is random

def generateRandomNumber():
    return random.randint(0,9)

def generateRandomLetter():
   return random.choice("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split())

# print(generateRandomLetter(), generateRandomNumber())

class Column():
    name=''
    type='' # type of value: string, number, both
    def __init__(self, name, type) -> None:
        self.name = name
        self.type = type


class Row():
    row = {
        id: 0
    }
    def __init__(self, id, values) -> None:
        self.id = id
        self.values = values # what are values?


class Table():
    def __init__(self, rows) -> None:
        self.rows = rows
    
