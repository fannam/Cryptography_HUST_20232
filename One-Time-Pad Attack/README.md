#same cipher key One-Time-Pad Attack 

#Basis knowledge: 
With the same cipher key, the OTP method is vulnerable since with two plaintexts:
- plaintext1 XOR key = ciphertext1
- plaintext2 XOR key = ciphertext2

So that: plaintext1 XOR plaintext2 = ciphertext1 XOR ciphertext2.
We know that in a normal English paragraph, the 'space' character appears frequently.
Let take A to Z XOR with space (0x20 in hexadecimal) then we get some 'printable' characters like @ ; ' etc.
Similary, take a to z XOR with space, we get A to Z respectively.


Follow my approach, we will use these tricks to find the key. 

Let's take a look in some paragraphs and you will see that the 'space' characters in one paragraph is seems to be not usually placed in the same position in different paragraph.
For example, 4 lines above has the 'space' characters in positions that is a non-space character of other paragraph.

So we just need to XOR a ciphertext with others and repeat for every ciphertexts. (Group 1 XOR 2,3,4... for example, then put them in lines consecutively. I will call 1 in this case is the root ciphertext)

For me, I used Excel to avoid coding too much. You will have to add a space between every characters to use split data to cell in Excel.
After that, it's very clear that the potential space must be the position that includes many capitalized characters (A to Z) because the frequency of normal characters (a to z) in an English paragraph is extremely high.

After found these positions, we will XOR the root ciphertext in these position with 0x20 (aka space).

You might see that some words are not correct in syntax. It's normal because the 'normalize' every special characters such as : ? ' " etc into 'space'. But we still can guess because it's still an English paragraph. 

