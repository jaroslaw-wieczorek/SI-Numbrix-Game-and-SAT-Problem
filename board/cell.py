import sys
from os import path


class Cell():
    
    """
       ID is the value representing the cell
          
         |1||2||3|
         |4||5||6|
         |7||8||9|
    
    """

    def __init__(self, ID, value):
        if type(ID) != int:
            raise TypeError("TypeError: ID")
           
        elif ID < 0:
            raise ValueError("ValueError: ID")
        
        elif type(value) == int and value < 0:
             raise ValueError("ValueError: ID")

        else:
            self.ID = ID
            self.value = value
            
             
        
    def __str__(self):
        return "({:};{:})".format(self.ID , self.value)
           
        
    def __repr__(self):
        return "({:};{:})".format(self.ID , self.value)
