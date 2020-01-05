import random


class Encryption:

    # two random primes
    p = 10181
    q = 283
    # mod i use to dycrpt
    n = 0
    phiN = 0
    # my public key e
    pub = 0
    # private Key d
    private = 0

    def __init__(self, p, q):
        self.n = p*q  # Mod
        self.phiN = self.getPhiOf(p, q)
        self.pub = self.getPublicKey(p, q)
        self.private = self.getPrivateKey(self.phiN)

    def getPrivateKey(self, phiN):
        d = (phiN * random.randint(1, 3)) - 1
        if ((self.pub*d) % phiN != 1):
            print('private key check went wrong')
        return d

    #  Probaly goes wrong
    def getPublicKey(self, p, q):
        eList = self.getCommenCoPrimes(p*q)
        eList.remove(1)
        return random.choice(eList)

    # gets the amount of posible co primes
    def getPhiOf(self, a, b):
        return (a-1)*(b-1)

    def getCoPrimes(self, n):
        print('--- corpimes of ' + str(n) + '---')
        numbers = list(range(2, n))
        for i in numbers[:]:  # not sure what [:] does
            if n % i == 0:
                for ii in numbers[i-2::i]:
                    numbers[ii-2] = 0  # there we be some numbers be getting removed twice
        numbers = list(set(numbers))  # filter duplicates
        numbers.remove(0)
        print(numbers)
        return [1] + numbers

    # get Commen co primes from n and phi(n)
    def getCommenCoPrimes(self, n):
        coPrimeList = self.getCoPrimes(n)
        coPrimeListTwo = self.getCoPrimes(len(coPrimeList))
        matches = list(set(coPrimeList).intersection(coPrimeListTwo))  # how do set work?
        return matches  # we want a number above 1
