p = 2
q = 7
n = p*q
phiN = (p-1)*(q-1)
e = 5
d = 11


class Cypher:

    def chyperString(self, plain, key, mod):
        cypherList = []
        for c in plain:
            cypherList.append(self.chyperVal(ord(c), key, mod))
        return cypherList

    def deChyperList(self, list, key, mod):
        cypher = ""
        for i in list:
            cypher += chr(self.chyperVal(i, key, mod))
        return cypher


    def chyperVal(self, num, key, mod):
        numVal = num**key % mod
        return numVal
