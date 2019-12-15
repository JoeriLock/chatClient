import random

# two random primes
p = 7686544500740926489
q = 10367748245344531429
# mod i use to dycrpt
n = p*q
# my public key
e = 0
# private Key
d = 0


def __init__(self):
    e = getPublicKey(p,q)
    d = getPrivateKey(getCoPrimesFromPrimes(p,q))
    print(e)
    print(d)


# ord(char) < mod
def chyperChar(char, key, mod):
    numVal = ord(char)**key % mod
    return chr(numVal)


def getPrivateKey(phiN):
    return (phiN * random.randint(0, 1000)) - 1


def getPublicKey(p,q):
    eList = getCommenCoPrimes(p*q)
    eList.remove(1)
    return random.choice(eList)


# gets the amount of posible co primes
def getCoPrimesFromPrimes(a, b):
    return (a-1)*(b-1)


def getCoPrimes(n):
    numbers = list(range(2, n))
    for i in numbers[:]:  # not sure what [:] does
        if n % i == 0:
            for ii in numbers[i-2::i]:
                numbers[ii-2] = 0  # there we be some numbers be getting removed twice
    numbers = list(set(numbers))
    numbers.remove(0)
    return [1] + numbers


# get Commen co primes from n and phi(n)
def getCommenCoPrimes(n):
    coPrimeList = getCoPrimes(n)
    coPrimeListTwo = getCoPrimes(len(coPrimeList))
    matches = list(set(coPrimeList).intersection(coPrimeListTwo))  # how do set work?
    return matches  # we want a number above 1
