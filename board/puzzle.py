# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:45:34 2018

@author: afar
"""

import pandas as pd
from collections import namedtuple
import array
import csv
import os
import sys


class Puzzle():
          
    def __init__(self):
        self.puzzle = []
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
                
                     
    def listNeighbourhood(self, ID):
        """Looking neighbourhoods"""
        neighbourhood_list=[]
        for x, row in enumerate(self.puzzle):  
            for y, item in enumerate(row):
                if item.ID == ID:
                    if self.puzzle[x-1][y]:
                        neighbourhood_list.append(self.puzzle[x-1][y])
                    if self.puzzle[x+1][y]:
                        neighbourhood_list.append(self.puzzle[x+1][y])
                    if self.puzzle[x][y-1]:
                        neighbourhood_list.append(self.puzzle[x][y-1])
                    if self.puzzle[x][y+1]:
                        neighbourhood_list.append(self.puzzle[x][y-1])
        return neighbourhood_list
        
               
                     
                     
        

def main():
    print(Cell(0,0))
    print(Cell(1,3))
    print(Cell(1,0))
    print(Cell(0,'x'))
    print(Cell(1,'.'))
    print(Cell(0,None))
    
    
    path = "../maps/map1.csv"
    path2 = "../maps/map2.csv"
    
    p=Puzzle()
    
    p.load(path)
    print(str(p.puzzle))
    
    print("\n")
    
    
    p.load(path2)
    print(str(p.listNeighbourhood(3)))
    
    
   # p.listNeighboards(3)
if __name__ == "__main__":
    main()
   
    
    

    