# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:02:13 2018

@author: afar
"""
from board.puzzle import Puzzle
from board.cell import Cell
from unary import Encoding
from reduced_encoding import Reduced_Encoding
from tseitisin import Tseitin_Encoding

from os import path

def main():
    
    #print(Cell(0,0))
    #print(Cell(1,3))
    #print(Cell(1,0))
    #print(Cell(0,'x'))
    #print(Cell(1,'.'))
    #print(Cell(0,None))
    
    path0 = "maps/map0.csv"
    path = "maps/map1.csv"
    path2 = "maps/map2.csv"
    
    p=Puzzle()
    
    p.load(path0)
   
    print(p)
    print("\n")
    
    #print(str(p.listNeighbourhood(10)))
    
    e = Encoding(p)
    e.encode("scream")
    e.decode("outscream")
    pass


if __name__ == '__main__':
    
    main()