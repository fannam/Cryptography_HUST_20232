# Cryptography_HUST_20232

Basis knowledge: with the same cipher key, the OTP method is vulnerable since with two plaintexts:
plaintext1 XOR key = ciphertext1
plaintext2 XOR key = ciphertext2

So that plaintext1 XOR plaintext2 = ciphertext1 XOR ciphertext2 
We know that in a normal English paragraph, the 'space' character appears frequently.
Let take A to Z XOR with space (0x20 in hexadecimal) then we get some 'printable' characters like @ ; ' etc
Similary, take a to z XOR with space, we get A to Z respectively 

Follow my approach, we will use these tricks 

