import random

class RSA():
    p = random.randint(10 , 100)
    q = random.randint(10 , 100)
    for i in range(2 , p):
        if(p % i == 0):
            p += 1
            i = 2
    for i in range(2 , q):
        if(q % i == 0):
            q += 1
            i = 2
    n = p * q
    φ = (p - 1) * (q - 1)
    e = random.randint(2 , φ-1)

    for i in range(2 , e + 1) :
        if (e % i == 0 and φ % i == 0) :
            e -= 1
            i = 2
        else :
            i += 1
    d = 2
    while( (d * e) % φ != 1 ):
        d += 1
    def encrypt(self , text):
        encrypt_text = list()
        for i in text:
            encrypt_text.append(ord(i))
        plaintext = list()
        for i in encrypt_text:
            plaintext.append((i ** self.e) % self.n)
        print("plaintext:" , plaintext)
        return plaintext
    def decrypt(self , plaintext):
        ciphertext = list()
        ciphertext2 = list()
        for i in plaintext:
            ciphertext.append((i ** self.d) % self.n)
        for i in ciphertext:
            ciphertext2.append(chr(i))
        ciphertext2 = "".join(ciphertext2)
        print("ciphertext:" , ciphertext2)



print("Write **1923** anywhere if u want to exit")


while True:

    you = RSA( )
    he_or_she = RSA( )

    x = input("You:")
    if(x == "**1923**"):
        break
    text = you.encrypt(x)
    he_or_she.decrypt(text)
    y = input("He/She:")
    if(y == "**1923**"):
        break
    text = he_or_she.encrypt(y)
    you.decrypt(text)



