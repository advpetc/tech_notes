# Symbolics
* **p** and **q** are two very large primes
* **n** = p * q : Modulus
* **phi** = (p-1) * (q-1) : Totient
* **e** Public Key: is the prime number chosen in the range [3, phi(n)]
* **d** Secret Key

# Calculate **d** and Encrypt the message
1. using extended-Euclid's algorithm to find the resulting equation when gcd = 1: it should always look like this: 
  * 1 = (a) * phi + (b) * e
  * And d = phi * k - b (k is any integer that could make d > 0)
  * To verify: e * d = 1 mod phi, this could be done easily
2. Encrypt the message using public key e and n:
  * M ^ e mod n
  * the result **C** is the encrypted message

# Decrypt C using private key
1. M = c ^ d mod n
2. Sometimes it's being called the signature sign