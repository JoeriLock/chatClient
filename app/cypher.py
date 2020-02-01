class Cypher:

    key = ""
    mod = ""
    def __init__(self,key,mod):
        self.key = int(key)
        self.mod = int(mod)

    def chyperString(self, plain):
        cypherList = []
        for c in plain:
            cypherList.append(self.chyperVal(ord(c)))
        return cypherList

    def deChyperList(self, list):
        cypher = ""
        for i in list:
            cypher += chr(self.chyperVal(i))
        return cypher


    def chyperVal(self, num):
        numVal = num**self.key % self.mod
        return numVal
