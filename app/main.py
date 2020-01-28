from cypher import Cypher
from encryption import Encryption

print('---enc---')
enc = Encryption(79, 11)

print("Pub:" + str(enc.pub))
print("Priv:" + str(enc.private))
print("mod:" + str(enc.n))
print("phiN:" + str(enc.phiN))

print('---text---')
text = 'ik ben joeri'
c = Cypher()
crypt = c.chyperString(text, enc.pub, enc.n)
print("plain:" + str(text))
print("encrypt:")
print(crypt)
print("decrypt:" + str(c.deChyperList(crypt, enc.private, enc.n)))
