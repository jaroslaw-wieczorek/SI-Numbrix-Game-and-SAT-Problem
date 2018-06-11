import os
from board.puzzle import Puzzle
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
        p = Puzzle()
        p.load(path)
        return p

    def result_reduce_encoding(self, p: Puzzle):
        e = Reduced_Encoding(p)
        e.encode("scream")
        #os.system("cryptominisat5 --verb 0 scream > outscream")
        os.popen("cryptominisat5 --verb 0 scream > outscream").read()
        result = e.decode("outscream")
        return result

    def result_encoding(self, p: Puzzle):
        e = Unary_Encoding(p)
        e.encode("scream")
        #os.system("cryptominisat5 --verb 0 scream > outscream")
        os.popen("cryptominisat5 --verb 0 scream > outscream").read()
        result = e.decode("outscream")
        return result