import math

import numpy
from bitstring import BitArray

from board.puzzle import Puzzle


class Encoding:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = puzzle.height
        self.n = puzzle.maxID()
        self.gb = int(math.ceil(math.log2(self.n)))

    def decode(self, inputFile):
        with open(inputFile, "r") as f:
            content = f.readlines()[1:]
            satout = []
            if len(content) == 0:
                print("NOT SATISFIED")
                return
            if len(content) > 1:
                for line in content:
                    line = line[2:]
                    line = line.split()
                    for x in line:
                        satout.append(int(x))
                del satout[-1]

            else:
                content = content[0]
                content = content[2:-2]
                # content = [x.strip() for x in content]
                content = content.split()
                satout = [int(x) for x in content]
            values = []
            for i in range(1, self.n + 1):
                ints = []
                ints = satout[0:self.n]
                satout = satout[self.n:]
                # ints <- first x literals from inputFile
                # remove the first x literals from inputFile
                # add the output of iConvert(ints) to values
                values.append(self.iconvert(ints))
            # use Puzzle as a template to typeset values into output file--
            it = iter(values)
            for b in self.puzzle.puzzle:
                for c in b:
                    if c.ID != 0:
                        c.value = next(it)
            return self.puzzle

    def convert(self, ajdi, x):
        return (ajdi - 1) * self.n + x

    def iconvert(self, ints):
        for i in ints:
            if i > 0:
                return ((i - 1) % self.n) + 1

    def exists(self, id):
        out = []
        for x in range(1, self.n + 1):
            out.append(self.convert(id, x))
        return out

    def isunique(self, id):
        CNF = []
        for x1 in range(1, self.n):
            for x2 in range(x1, self.n + 1):
                if x1 != x2:
                    CNF.append([-1 * self.convert(id, x1), -1 * self.convert(id, x2)])
        return CNF

    def arenotqual(self, id1, id2):
        CNF = []
        for x in range(1, self.n + 1):
            if id1 != id2:
                CNF.append([-1 * self.convert(id1, x), -1 * self.convert(id2, x)])
        return CNF

    def precedes(self, jd, ids):
        CNF = []
        for x in range(1, self.n):
            clause = []
            clause.append(-1 * self.convert(jd, x))
            for i in ids:
                clause.append(self.convert(i.ID, x + 1))
            CNF.append(clause)
        return CNF

    def isequal(self, ID, x):
        return self.convert(ID, x)


    def encode(self, outputfile):
        CNF = []
        #Every cell of the grid must be filled with a natural number ranging from 1 to n;
        for b in self.puzzle.puzzle:
            for c in b:
                if c.ID != 0:
                    CNF.append(self.exists(c.ID))
                    #for clau in self.exists(c.ID):
                    #    CNF.append(clau)
        #No cell has two numbers;
        for b in self.puzzle.puzzle:
            for c in b:
                if c.ID != 0:
                    for clau in self.isunique(c.ID):
                        CNF.append(clau)


        
        #No two cells have the same number;
        #for b in self.puzzle.puzzle:
            #it = iter(b)
            #for c in it:
            #   CNF.append(self.arenotqual(c.ID, next(it).ID))
            #for clau in self.arenotqual(c.ID, next(it).ID):
            #        CNF.append(clau)
            #if c.ID != 0:
                for x1 in range(1, self.n):
                    for x2 in range(x1, self.n + 1):
                        for clau in self.arenotqual(x1, x2):
                            CNF.append(clau)
            




        #Every cell except the one with number n does have a successor;
        for b in self.puzzle.puzzle:
            for c in b:
                if c.ID != 0:
                    ids = self.puzzle.listNeighbourhood(c.ID)
                    for clau in self.precedes(c.ID, ids):
                        CNF.append(clau)
        #Pre-filled numbers are unchanged.
        for b in self.puzzle.puzzle:
            for c in b:
                if c.value != 0:
                    CNF.append(self.isequal(c.ID, c.value))

        with open(outputfile, 'w') as file:
            file.write("p cnf ")
            file.write(str(self.n * self.n))
            file.write(" ")
            file.write(str(len(CNF)))
            file.write("\n")
            for clauso in CNF:
                clauso = str(clauso).replace("[", "")
                clauso = str(clauso).replace("]", "")
                clauso = str(clauso).replace(",",  "")
                file.write(clauso)
                file.write(" 0")
                file.write("\n")