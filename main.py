# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:02:13 2018

@author: afar
"""
import os
from board.game_board import GameBoard
from board.cell import Cell
from unary import Unary_Encoding
from reduced_encoding import Reduced_Encoding
from tseitisin import Tseitin_Encoding
from numbrix import Numbrix
from os import path


def main():
    path0 = "maps/map0.csv"
    path1 = "maps/map1.csv"
    path2 = "maps/map2.csv"
    path3 = "maps/map3.csv"
    path4 = "maps/map4.csv"
    n = Numbrix()
    p = n.load(path4)
    print(p)
    n.result_reduce_encoding(p).printMatrix()
    print("")
    p = n.load(path4)
    n.result_encoding(p).printMatrix()

if __name__ == '__main__':
    
    main()