from bitstring import BitArray, BitStream
import math
import hashlib

class Encoding:

    def __init__(self, n):
        self.n = n
        self.hash_table={} #this is dictionary to hash function


    def decode(self, puzzle, inputFile):
        for i in range(1, puzzle.n):
            ints = []
            # ints <- first x literals from inputFile
            # remove the first x literals from inputFile
            # add the output of iConvert(ints) to values
            values = []
            values.append(Encoding.iconverse(ints))
        # use Puzzle as a template to typeset values into output file--
        print(values)        
        
        
    def convert(self, ID, x):
        x -= 1
        b = math.log2(self.n)
        b = int(math.ceil(b))
        ints = []
        xbit = BitArray(uint=x, length=b)
        for i in range(1, b):
            if xbit[-1]:
                ints.append(((ID-1)*b+1))
            else:
                ints.append(-((ID - 1) * b + 1))
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
        #1 TO CHECK
        hash_key = hashlib.sha512(ints).hexdigest()
        if hash_key in ints:
            return ints[hash_key]
        #2 TO CHECK 
        else:
            return None #if don't exist return None
        
        #Hash receives a clause and returns a unique DIMACS variable assigned to it in the hash table.


    def contains(self, ints):
        #2 TO CHECK
        hash_key = hashlib.sha512(ints).hexdigest()
        
        if hash_key in ints:
            return True
        else:
            return False
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


    def precedes(self, ID, ids):
        CNF = []
        for x in range(1, self.n):
            clause = []
            for i in Encoding.convert(self, ID, x):
                #add -i to clause
                clause.append(-i)
            for i in ids:
                #add the output of Encoding.Hash(Encoding.convert(i,x + 1)) to clause
                clause.append(Encoding.hash(self, Encoding.convert(self, i.ID, x + 1)))
                #add the output of Tseitin(Convert(i,x + 1)) to CNF
                CNF.append(Encoding.tseitin(Encoding.convert(self, i.ID, x + 1)))
            #add clause to CNF
            CNF.append(clause)
        return CNF


    def isequal(self, ID, x):
        CNF = []
        for i in Encoding.convert(ID, x):
            CNF.append(i)
        return CNF


    def encode(self, puzzle, outputfile):
        CNF = []
        for b in puzzle.puzzle:
            for c in b:
                ids = puzzle.listNeighbourhood(c.ID)
                CNF.append(Encoding.precedes(self,c.ID, ids))
        for b in puzzle.puzzle:
            for c in b:
                if c.x != 0:
                    CNF.append(Encoding.isequal(c.ID,c.x))
        print(CNF)
        #with open(outputfile, 'w') as file:
        #    file.write(CNF)
