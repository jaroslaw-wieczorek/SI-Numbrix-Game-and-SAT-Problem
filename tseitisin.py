import numpy
from bitstring import BitArray, BitStream
import math
import hashlib

class Encoding:

    def __init__(self, size):
        self.size = size
        self.n = size * size
        self.hash_table = {} #this is dictionary to hash function
        self.gb = int(math.ceil(math.log2(self.n))) +1
        self.varnumber = self.gb * self.n

    def decode(self, puzzle, inputFile):
        with open(inputFile, "r") as f:
            content = f.readlines()[1:]
            satout = []
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
                #content = [x.strip() for x in content]
                content = content.split()
                satout =[int(x) for x in content]
            values = []
            for i in range(1, self.gb+1):
                ints = []
                ints = satout[0:self.n]
                satout = satout[self.n:]
                # ints <- first x literals from inputFile
                # remove the first x literals from inputFile
                # add the output of iConvert(ints) to values
                values.append(self.iconverse(ints))
            # use Puzzle as a template to typeset values into output file--
            answer = numpy.empty((self.size, 0)).tolist()
            count = 0
            it = iter(values)
            for row in answer:
                for x in range(0, self.size):
                    row.append(next(it))
                print(*row, sep=' ')
                #print("\n")

    def convert(self, iD, x):
        x = x - 1
        ints = []
        xbit = BitArray(uint=x, length=self.gb)
        for i in range(1, self.gb+1):
            if xbit[-1]:
                ints.append(((iD - 1) * self.gb + 1))
            else:
                ints.append(-1*((iD - 1) * self.gb + 1))
            del xbit[-1]
        return ints
    

    def iconverse(self, ints):
        result = 0
        power = 1
        for i in ints:
            if i > 0:
                result = result + power
            power = power * 2
        return result + 1


    def hash(self, ints):
        """Hash receives a clause and returns a unique DIMACS variable assigned to it in the hash table."""
        self.varnumber = self.varnumber + 1
        self.hash_table[''.join(map(str, ints))] = self.varnumber
        return self.varnumber



    def contains(self, ints):
        """Method Contains, returning True or False, checks whether hash table contains an entry for the clause received as an argument."""
        return ''.join(map(str, ints)) in self.hash_table


    def tseitin(self, ints):
        CNF = []
        if self.contains(ints):
            return CNF
        else:
            clause = []
            h = self.hash(ints)
            #add h to clause
            clause.append(h)
            for i in ints:
                #add -i to clause
                clause.append(-i)
            #add clause to CNF
            CNF.append(clause)
            for i in ints:
                #add {-h,i} to CNF
                CNF.append([-h, i])
            return CNF


    def precedes(self, ID, ids):
        CNF = []
        for x in range(1, self.n+1):
            clause = []
            for i in self.convert(ID, x):
                #add -i to clause
                clause.append(-i)
            for i in ids:
                CNF.append(Encoding.tseitin(self, self.convert(i.ID, x + 1)))
                #add the output of Encoding.Hash(Encoding.convert(i,x + 1)) to clause
                clause.append(Encoding.hash(self, self.convert(i.ID, x + 1)))
                #add the output of Tseitin(Convert(i,x + 1)) to CNF

            #add clause to CNF
            CNF.append(clause)
        return CNF


    def isequal(self, ID, x):
        CNF = []
        for i in self.convert(ID, x):
            CNF.append(i)
        return CNF


    def encode(self, puzzle, outputfile):
        CNF = []
        for b in puzzle.puzzle:
            for c in b:
                ids = puzzle.listNeighbourhood(c.ID)
                for clau in Encoding.precedes(self, c.ID, ids):
                    CNF.append(clau)
                #CNF.append(Encoding.precedes(self, c.ID, ids))
        for b in puzzle.puzzle:
            for c in b:
                if c.value != 0:
                    #CNF.append(Encoding.isequal(self, c.ID, c.value))
                    for clau in self.isequal(c.ID, c.value):
                        CNF.append(clau)
        #print(CNF)
        with open(outputfile, 'w') as file:
            file.write("p cnf ")
            file.write(str(self.n*self.n))
            file.write(" ")
            file.write(str(len(CNF)))
            file.write("\n")
            for clauso in CNF:
                clauso = str(clauso).replace("[","")
                clauso = str(clauso).replace("]","")
                clauso = str(clauso).replace(",","")
                print(clauso)
                file.write(clauso)
                file.write(" 0")
                file.write("\n")
