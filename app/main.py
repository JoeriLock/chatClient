from cypher import Cypher
from encryption import Encryption

print('---enc---')
enc = Encryption(79, 41)

print("Pub:" + str(enc.pub))
print("Priv:" + str(enc.private))
print("mod:" + str(enc.n))
print("phiN:" + str(enc.phiN))

print('---text---')
text = 2
c = Cypher()
crypt = c.cypherNum(text, enc.pub, enc.n)
print("plain:" + str(text))
print("encrypt:" + str(crypt))
print("decrypt:" + str(c.cypherNum(crypt, enc.private, enc.n)))
