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
from os import path
import sys

from .cell import Cell

class GameBoard():
          
    def __init__(self):
        self.table = []
        self.height=0
        self.width=0
 
    def __repr__(self):
        return ''.join(map(str,self.table))
        
    def printMatrix(self):
        for b in self.table:
            for c in b:
                print(c.value, end=' ')
            print("\n", end='')


    """
        Fucntion takes csv and load it to self.table variable
        
    
    """

    def load(self, filename, delim=';', nline='\n', qchar='"'):
        self.table=[]
        if path.isfile(filename):
             with open(filename, newline=nline) as csvfile:
                 self.height = 0
                 self.width = 0
                 current_id = 1
                 spamreader = csv.reader(csvfile, delimiter=delim, quotechar=qchar)                 
                 for row in spamreader:
                     tmp=[]
                     self.height += 1
                     for cell_value in row:
                         if cell_value == 'X' or cell_value == 'x' :
                             tmp.append(Cell(0,0))
                         elif cell_value == '' or cell_value =='.' :
                             tmp.append(Cell(current_id, 0))
                             current_id+=1
                         else: 
                             tmp.append(Cell(current_id, int(cell_value)))
                             current_id+=1
                                                          
                     self.table.append(tmp)
                 self.width = len(self.table[0])
        return True
    
    def maxID(self):
        max = 0
        for row in self.table:
            for cell in row:
                if(cell.ID > max):
                    max=cell.ID
                    #print(max)
        return max

    
                     
    def listNeighbourhood(self, ID):
        """Looking neighbourhoods"""
        neighbourhood_list=[]
        for row, rows in enumerate(self.table):  
            for col, cell in enumerate(rows):
                if cell.ID == ID:
                    if row + 1 <=self.height-1 and self.table[row +1][col].ID != 0:
                        cell = self.table[row +1][col]
                        #print("x+1:",row," y:",col," cell:", cell)
                        neighbourhood_list.append(cell)
                        
                    if row - 1 >= 0 and self.table[row - 1][col].ID != 0:
                        cell = self.table[row - 1][col]
                        #print("x-1:",row," y:",col," cell:", cell)
                        neighbourhood_list.append(cell)
                
                    if col + 1 <= self.width-1 and self.table[row][col+1].ID != 0:
                        cell = self.table[row][col + 1]
                        #print("x:",row," y+1:",col," cell:", cell)
                        neighbourhood_list.append(cell)
                        
                    if col - 1 >= 0 and self.table[row][col-1].ID != 0:
                        cell = self.table[row][col - 1]
                        #print("x:",row," y-1:",col," cell:", cell)
                        neighbourhood_list.append(cell)                    
                    break
                
        return neighbourhood_list
        
               


    