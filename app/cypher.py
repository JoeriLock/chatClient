p = 2
q = 7
n = p*q
phiN = (p-1)*(q-1)
e = 5
d = 11


class Cypher:

    # ord(char) < mod
    def chyperChar(self, char, key, mod):
        numVal = ord(char)**key % mod
        return chr(numVal)

    def cypherNum(self, num, key, mod):
        numVal = num**key % mod
        return numVal
