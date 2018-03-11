#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:45:34 2018

@author: afar
"""

import pandas as pd
from collections import namedtuple
import array
import csv
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
            
        elif type(value) != int:
            self.ID = ID
            self.value = '.'
              
        else:
            self.ID = ID
            self.value = value
            
                      
    def __str__(self):
        return "[*] cell id={:} value={:}".format(self.ID , self.value)
           
        
    def __repr__(self):
        return "[*] cell id={:} value={:}".format(self.ID , self.value)



class Puzzle():
      
    
    def __init__(self):
        self.puzzle = []
        self.types=[0, 1]
        
    def load(self, filename, delim=';', nline='\n', qchar='"'):
        if path.isfile(filename):
             with open(filename, newline=nline) as csvfile:
                 y=0
                 x=0
                 spamreader = csv.reader(csvfile, delimiter=delim, quotechar=qchar)                 
                 for row in spamreader:
                     tmp=list()
                     for item in row:
                         tmp.append(item)
                                  
                     
                     self.puzzle.append(tmp)
                     tmp=[]
        
               
                     
                     
        

def main():
    print(Cell(0,0))
    print(Cell(1,3))
    print(Cell(1,0))
    print(Cell(0,'x'))
    print(Cell(1,'.'))
    print(Cell(0,None))
    
    
    path = "/home/afar/SI-Numbrix-Game-and-SAT-Problem/map1.csv"

    p=Puzzle()
    
    
    p.load(path)
    print(p.puzzle)

if __name__ == "__main__":
    main()
   
    
    

    