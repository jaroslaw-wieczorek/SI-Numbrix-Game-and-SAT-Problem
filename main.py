# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:02:13 2018

@author: afar
"""
import os
from board.puzzle import Puzzle
from board.cell import Cell
from unary import Encoding
from reduced_encoding import Reduced_Encoding
from tseitisin import Tseitin_Encoding
from numbrix import Numbrix
from os import path


def main():
    
    #print(Cell(0,0))
    #print(Cell(1,3))
    #print(Cell(1,0))
    #print(Cell(0,'x'))
    #print(Cell(1,'.'))
    #print(Cell(0,None))
    
    path0 = "maps/map0.csv"
    path1 = "maps/map1.csv"
    path2 = "maps/map2.csv"
    path3 = "maps/map3.csv"
    n = Numbrix()
    p = n.load(path0)
    print(n.result_reduce_encoding(p))
    print(n.result_encoding(p))

if __name__ == '__main__':
    
    main()