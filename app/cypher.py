class Cypher:

    key = ""
    mod = ""
    def __init__(self,key,mod):
        self.key = int(key)
        self.mod = int(mod)



    def chyperString(self, plain):
        cypherString = ""
        for c in plain:
            cypherString += str(self.chyperVal(ord(c)))+","
        return cypherString[:-1]

    def deChyperList(self, list):
        cypher = ""
        for i in list:
            cypher += chr(self.chyperVal(i))
        return cypher


    def chyperVal(self, num):
        numVal = int(num)**self.key % self.mod
        return numVal
