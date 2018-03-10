from bitstring import BitArray, BitStream
import math


class Encoding:

    def __init__(self, n):
        self.n = n

    def convert(self, cellid, x):
        x -= 1
        b = math.log2(self.n)
        ints = []
        xbit = BitArray(uint=x, length=b)
        for i in range(1, b):
            if xbit[-1]:
                ints.append(((cellid-1)*b+1))
            else:
                ints.append(-((cellid - 1) * b + 1))
            del xbit[-1]
        return ints

    def iconverse(self, ints):
        result = 0
        power = 1
        for i in ints:
            if i > 0:
                result += power
            power *= 2
        return result + 1


    def hash(self, ints):
        return 1
        #Hash receives a clause and returns a unique DIMACS variable assigned to it in the hash table.

    def contains(self, ints):
        return 1
        #Method Contains, returning True or False, checks whether hash table contains an entry for the clause received as an argument.

    def tseitin(self, ints):
        CNF = []
        if Encoding.contains(ints):
            return CNF
        else:
            clause = []
            h=hash(ints)
            #add h to clause
            clause.append(h)
            for i in ints:
                #add -i to clause
                clause.append(-i)
            #add clause to CNF
            CNF.append(clause)
            for i in ints:
                #add {-h,i} to CNF
                CNF.append([-h,i])
            return CNF

    def precedes(self, cellid, ids):
        CNF = []
        for x in range(1,self.n):
            clause = []
            for i in Encoding.convert(cellid,x):
                #add -i to clause
                clause.append(-i)
            for i in ids:
                #add the output of Encoding.Hash(Encoding.convert(i,x + 1)) to clause
                clause.append(Encoding.Hash(Encoding.convert(i,x + 1)))
                #add the output of Tseitin(Convert(i,x + 1)) to CNF
                CNF.append(Encoding.tseitin(Encoding.convert(i,x + 1)))
            #add clause to CNF
            CNF.append(clause)
        return CNF

    def isequal(self, cellid, x):
        CNF = []
        for i in Encoding.convert(cellid,x):
            CNF.append(i)
        return CNF

    def encode(self, puzzle, outputfile):
        CNF = []
        for c in puzzle:
            ids = puzzle.listneighbours(c.cellid)
            CNF.append(Encoding.precedes(c.cellid, ids))
        for c in puzzle:
            if c.x != 0:
                CNF.append(Encoding.isequal(c.cellid,c.x))
        print(CNF)
