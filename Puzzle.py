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
            raise TypeErrolooking_hashr("TypeError: ID")
           
        elif ID < 0:
            raise ValueError("ValueError: ID")
        
        elif type(value) == int and value < 0 : 
             raise ValueErrorlooking_hash("ValueError: ID")
             looking_hash
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



class Puzzle():
          
    def __init__(self):
        self.puzzle = []
        self.types=[0, 1]
        self.height=0
        self.width=0
 
    def load(self, filename, delim=';', nline='\n', qchar='"'):
        self.puzzle=[]
        if path.isfile(filename):
             with open(filename, newline=nline) as csvfile:
                 self.height = 0
                 self.width = 0
                 current_id = 1
                 spamreader = csv.reader(csvfile, delimiter=delim, quotechar=qchar)                 
                 for row in spamreader:
                     tmp=[]
                     self.height += 1
                     self.width = 0
                     for item in row:
                         if item == 'X' or item == 'x' :
                             tmp.append(Cell(0,0))
                         elif item == '' or item =='.' :
                             tmp.append(Cell(current_id, 0))
                             current_id+=1
                         else: 
                             tmp.append(Cell(current_id, item))
                             current_id+=1
                                                          
                     self.puzzle.append(tmp)
                 self.width = len(self.puzzle)
                
                     
    def listNeighboards(self, ID):
        pass#for(p = self.puzzle.first(); p != self.puzzle.end(); ++p):
           # pass

        
               
                     
                     
        

def main():
    print(Cell(0,0))
    print(Cell(1,3))
    print(Cell(1,0))
    print(Cell(0,'x'))
    print(Cell(1,'.'))
    print(Cell(0,None))
    
    
    path = "./map1.csv"
    path2 = "./map2.csv"
    
    p=Puzzle()
    
    
    p.load(path2)
    print(str(p.puzzle))
    
   # p.listNeighboards(3)
if __name__ == "__main__":
    main()
   
    
    

    