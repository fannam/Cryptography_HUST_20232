import os
import time 

def generate_random_80_bit_string():
    random_bytes = os.urandom(10)
    iv = [int(bit) for byte in random_bytes for bit in f"{byte:08b}"]
    return iv

class Trivium:
    def __init__(self, key, iv):
        self.state = [0] * 288 #register A+B+C
        self.key = key
        self.iv = iv
        self.load_key_iv(key, iv)
    
    def load_key_iv(self, key, iv):
        #80 bit iv loaded into 80 bit leftmost of register A
        #80 bit key is loaded into 80 bit leftmost of register B
        for i in range(80):
            self.state[i] = iv[i]
            self.state[i+93] = key[i]
        #c109 = c110 = c111 = 1
        self.state[285] = 1
        self.state[286] = 1
        self.state[287] = 1
        

    def clock(self, N, is_warm_up_phase = False):
        key_stream = []
        for _ in range(N):
            t1 = self.state[65] ^ self.state[92]
            t2 = self.state[161] ^ self.state[176]
            t3 = self.state[242] ^ self.state[287]
            z = t1 ^ t2 ^ t3
            t1 = t1 ^ (self.state[90] & self.state[91]) ^ self.state[170]
            t2 = t2 ^ (self.state[174] & self.state[175]) ^ self.state[263]
            t3 = t3 ^ (self.state[285] & self.state[286]) ^ self.state[68]

            for i in range(93, 0, -1):
                self.state[i] = self.state[i-1]
            self.state[0] = t3
            for i in range(176, 93, -1):
                self.state[i] = self.state[i-1]
            self.state[93] = t1
            for i in range(287, 177, -1):
                self.state[i] = self.state[i-1]
            self.state[177] = t2
            key_stream.append(z)
        if not is_warm_up_phase:
            return key_stream
    def encrypt(self, plaintext, output_file):
        self.load_key_iv(key, iv)
        ciphertext = [chr(ord(plaintext[i]) ^ key_stream[i]) for i in range(len(plaintext))]
        ciphertext_str = ''.join(ciphertext)

        # Write the ciphertext to the output file
        with open(output_file, 'w') as file:
            file.write(ciphertext_str)

with open('alice29.txt', 'r') as file:
    plaintext = file.read()

#80 bit initial vector
iv =    [0, 0, 0, 1, 1, 1, 1, 1,
        0, 1, 0, 1, 0, 0, 0, 0, 
        1, 0, 1, 1, 1, 0, 1, 1, 
        0, 1, 1, 0, 0, 1, 0, 0,
        0, 1, 1, 1, 0, 0, 0, 1, 
        0, 0, 1, 1, 1, 0, 1, 0, 
        0, 0, 1, 1, 0, 0, 1, 0, 
        0, 1, 1, 0, 1, 1, 1, 1, 
        0, 0, 0, 0, 1, 0, 1, 0, 
        0, 1, 0, 0, 1, 1, 0, 0]
#80 bit key 
key =   [1, 0, 1, 0, 0, 1, 0, 1,  
        1, 0, 1, 1, 0, 0, 1, 0,
        0, 1, 1, 0, 1, 0, 0, 1,
        1, 1, 0, 0, 1, 1, 0, 1,
        0, 1, 0, 1, 1, 0, 0, 1,
        1, 0, 1, 0, 0, 1, 1, 0,
        0, 1, 0, 1, 0, 1, 1, 0,
        1, 0, 1, 0, 1, 0, 0, 1,
        1, 0, 0, 1, 1, 0, 1, 1,
        0, 1, 1, 0, 1, 0, 1, 0]

start_time = time.time()
trivium = Trivium(key, iv)
trivium.clock(1152, True)
output_file = "alice29_encrypted.txt"
key_stream = trivium.clock(len(plaintext), False)
ciphertext = trivium.encrypt(plaintext, output_file)
end_time = time.time()
total_time = end_time - start_time
print(total_time)
