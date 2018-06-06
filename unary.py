import math

from bitstring import BitArray

from board.puzzle import Puzzle


class Encoding:

    def __init__(self, n):
        self.n = n
        self.gb = int(math.ceil(math.log2(self.n)))
        self.varnumber = self.gb * self.n

    def decode(self, puzzle, inputFile):
        for i in range(1, puzzle.n):
            ints = []
            # ints <- first x literals from inputFile
            # remove the first x literals from inputFile
            # add the output of iConvert(ints) to values
            values = []
            values.append(Encoding.iconvert(ints))
        # use Puzzle as a template to typeset values into output file--
        print(values)

    def convert(self, jd, x):
        x = x - 1
        ints = []
        xbit = BitArray(uint=x, length=self.gb)
        for i in range(0, self.gb):
            if xbit[-1]:
                ints.append(((jd - 1) * self.gb + 1))
            else:
                ints.append((-1)*((jd - 1) * self.gb + 1))
            del xbit[-1]
        return ints

    def iconvert(self, ints):###############3
        for i in ints:
            if i > 0:
                return (i - 1 % self.n) + 1

    def exists(self, id):###############3
        out = []
        for x in range(1, self.n):
            out.append(self.convert(id, x))
        return out

    def isunique(self, id):###############3
        CNF = []
        for x1 in range(1, self.n):
            for x2 in range(x1, self.n+1):
                #print(x1)
                #print(x2)
                #print("-----")
                CNF.append([[i * -1 for i in self.convert(id, x1)], [i * -1 for i in self.convert(id, x2)]])
        return CNF

    def arenotqual(self, id1, id2):###############3
        CNF = []
        for x1 in range(1, self.n):
            for x2 in range(x1, self.n+1):
                #print(x1)
                #print(x2)
                #print("-----")
                CNF.append([[i * -1 for i in self.convert(id1, x1)], [i * -1 for i in self.convert(id2, x2)]])
        return CNF

    def precedes(self, jd, ids): ###########
        CNF = []
        for x in range(1, self.n):
            clause = []
            clause.append([i * -1 for i in self.convert(jd, x)])
            for i in ids:
                clause.append(self.convert(i.ID, x + 1))
            CNF.append(clause)
        return CNF


    def isequal(self, ID, x): ##########
        return self.convert(ID, x)


    def encode(self, puzzle, outputfile):
        CNF = []
        for b in puzzle.puzzle:
            for c in b:
                CNF.append(self.exists(c.ID))
        for b in puzzle.puzzle:
            for c in b:
                CNF.append(self.isunique(c.ID))
        for b in puzzle.puzzle:
            it = iter(b)
            for c in it:
                CNF.append(self.arenotqual(c.ID, next(it).ID))
        for b in puzzle.puzzle:
            for c in b:
                ids = puzzle.listNeighbourhood(c.ID)
                CNF.append(self.precedes(c.ID, ids))
        for b in puzzle.puzzle:
            for c in b:
                if c.value != 0:
                    CNF.append(self.isequal(c.ID, c.value))

        print(CNF)
        # with open(outputfile, 'w') as file:
        #    file.write(CNF)