import os
from board.game_board import GameBoard
from board.cell import Cell
from unary import Unary_Encoding
from reduced_encoding import Reduced_Encoding
from tseitisin import Tseitin_Encoding
from os import path


class Numbrix():
    def __init__(self):
        pass

    # Load puzzle
    def load(self, path):
        g = GameBoard()
        g.load(path)
        return g

    def result_reduce_encoding(self, g: GameBoard):
        e = Reduced_Encoding(g)
        e.encode("scream")
        #os.system("cryptominisat5 --verb 0 scream > outscream")
        os.popen("cryptominisat5 --verb 0 scream > outscream").read()
        result = e.decode("outscream")
        return result

    def result_encoding(self, g: GameBoard):
        e = Unary_Encoding(g)
        e.encode("scream")
        #os.system("cryptominisat5 --verb 0 scream > outscream")
        os.popen("cryptominisat5 --verb 0 scream > outscream").read()
        result = e.decode("outscream")
        return result
