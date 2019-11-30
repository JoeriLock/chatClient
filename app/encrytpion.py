p = 2
q = 7
n = p*q

test = getCoPrimes(222)
len(test)


list(range(7,221,7))

def getCoPrimesFromPrimes(a, b):
    return (a-1)*(b-1)

def getCoPrimes(n):
    numbers = list(range(2, n))
    for i in numbers[:]:  # not sure what [:] does
        if n % i == 0:
            for ii in range(i, n, i):
                numbers.remove(ii)                    
    return [1] + numbers


# get Commen co primes from n and phi(n)
def getCommenCoPrimes(n):
    coPrimeList = getCoPrimes(n)
    coPrimeListTwo = getCoPrimes(len(coPrimeList))
    matches = list(set(coPrimeList).intersection(coPrimeListTwo))  # how do set work?
    return matches  # we want a number above 1
