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
        
        elif type(value) == int and value < 0 : 
             raise ValueError("ValueError: ID")
        elif ID == 0 or value == 0:
            self.ID = 0
            self.value = 0
            
        elif ID>0 and value == 0:
            self.ID = ID
            self.value = 0
              
        else:
            self.ID = ID
            self.value = value
            
             
        
    def __str__(self):
        return "({:};{:})".format(self.ID , self.value)
           
        
    def __repr__(self):
        return "({:};{:})".format(self.ID , self.value)



