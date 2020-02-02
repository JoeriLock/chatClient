from cypher import Cypher
from encryption import Encryption

print('---enc---')
enc = Encryption(79, 83)

print("Pub:" + str(enc.pub))
print("Priv:" + str(enc.private))
print("mod:" + str(enc.n))
print("phiN:" + str(enc.phiN))

print('---text---')
text = 'ik ben joeri' #message
c = Cypher(enc.pub, enc.n)
c2 = Cypher(enc.private, enc.n)
crypt = c.chyperString(text)
print("plain:" + str(text))
print("encrypt:")
print(crypt)
print("decrypt:" + str(c2.deChyperList(crypt.split(','))))
