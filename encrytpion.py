p = 2
q = 7
n = p*q


def getCoPrimesFromPrimes(a, b):
    return (a-1)*(b-1)

def getCoPrimes(n):
    numbers = list(range(2,n))
    for i in numbers[:]: # not sure what [:] does
        if n % i == 0:
            for ii in range(i, n, i):
                numbers.remove(ii)
    return [1] + numbers
