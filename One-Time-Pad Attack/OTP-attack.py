from collections import Counter
def split_hex_string(hex_string):
    # Split the hexadecimal string into substrings of length 2
    hex_list = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
    return hex_list

def xor_hex(hex_str1, hex_str2):
    int1 = int(hex_str1, 16)
    int2 = int(hex_str2, 16)
    res = int1 ^ int2

    return hex(res)

def trans_to_string(lst):
    res = ""
    for item in lst:
        if item == '*':
            res += "*"
        else:
            res += chr(int(item, 16))
    return res

cipher_text = ["315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e",
               "234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f",
               "32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb",
               "32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa",
               "3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070",
               "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4",
               "32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce",
               "315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3",
               "271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027",
               "466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83"]

target_cipher_text = "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"

key = ["00" for i in range(len(cipher_text[6]))]

element_list = []

xored_list = []

for text in cipher_text:
    row = split_hex_string(text)
    element_list.append(row)

for i in range(0, 9):
    xor_length = 0
    first_text_length = len(element_list[i])
    for j in range(i+1, 10):
        xored_row = []
        second_text_length = len(element_list[j])
        if first_text_length > second_text_length:
            xor_length = second_text_length
        else:
            xor_length = first_text_length
        for k in range(0, xor_length):
            xored_element = xor_hex(element_list[i][k], element_list[j][k])
            xored_row.append(xored_element)
        xored_list.append(xored_row)

texts = ["" for i in range(45)]
for i in range(0, len(xored_list)):
    texts[i]=""
    for j in range(len(xored_list[i])):
        if int(xored_list[i][j], 16)>=0x41 and int(xored_list[i][j], 16)<=0x5a:
            texts[i]=texts[i]+chr(int(xored_list[i][j], 16))
        else:
            texts[i]=texts[i]+"*"

#from 1 
key[2]=xor_hex(element_list[0][2], "20")
key[6]=xor_hex(element_list[0][6], "20")
key[13]=xor_hex(element_list[0][13], "20")
key[17]=xor_hex(element_list[0][17], "20")
key[24]=xor_hex(element_list[0][24], "20")
#key[25]=xor_hex(element_list[0][25], "20")
# key[26]=xor_hex(element_list[0][26], "20")
key[27]=xor_hex(element_list[0][27], "20")
key[32]=xor_hex(element_list[0][32], "20")
key[40]=xor_hex(element_list[0][40], "20")
key[50]=xor_hex(element_list[0][50], "20")
key[51]=xor_hex(element_list[0][51], "20")
key[54]=xor_hex(element_list[0][54], "20")
key[58]=xor_hex(element_list[0][58], "20")
key[63]=xor_hex(element_list[0][63], "20")
key[70]=xor_hex(element_list[0][70], "20")
key[74]=xor_hex(element_list[0][74], "20")
key[81]=xor_hex(element_list[0][81], "20")
key[83]=xor_hex(element_list[0][83], "20")
key[84]=xor_hex(element_list[0][84], "20")
key[89]=xor_hex(element_list[0][89], "20")
key[91]=xor_hex(element_list[0][91], "20")
key[95]=xor_hex(element_list[0][95], "20")
key[103]=xor_hex(element_list[0][103], "20")
key[106]=xor_hex(element_list[0][106], "20")
key[111]=xor_hex(element_list[0][111], "20")
key[117]=xor_hex(element_list[0][117], "20")
key[123]=xor_hex(element_list[0][123], "20")
key[124]=xor_hex(element_list[0][124], "20")
key[125]=xor_hex(element_list[0][125], "20")
key[132]=xor_hex(element_list[0][132], "20")
#from 2:
key[5]=xor_hex(element_list[1][5], "20")
key[10]=xor_hex(element_list[1][10], "20")
key[14]=xor_hex(element_list[1][14], "20")
key[20]=xor_hex(element_list[1][20], "20")
key[26]=xor_hex(element_list[1][26], "20")
key[31]=xor_hex(element_list[1][31], "20")
key[39]=xor_hex(element_list[1][39], "20")
key[47]=xor_hex(element_list[1][47], "20")
key[55]=xor_hex(element_list[1][55], "20")
key[57]=xor_hex(element_list[1][57], "20")
key[64]=xor_hex(element_list[1][64], "20")
key[70]=xor_hex(element_list[1][70], "20")
key[80]=xor_hex(element_list[1][80], "20")
key[82]=xor_hex(element_list[1][82], "20")
key[93]=xor_hex(element_list[1][93], "20")
key[96]=xor_hex(element_list[1][96], "20")
key[102]=xor_hex(element_list[1][102], "20")
key[104]=xor_hex(element_list[1][104], "20")

#from 3:
key[3]=xor_hex(element_list[2][3], "20")
key[8]=xor_hex(element_list[2][8], "20")
key[14]=xor_hex(element_list[2][14], "20")
key[20]=xor_hex(element_list[2][20], "20")
key[28]=xor_hex(element_list[2][28], "20")
key[31]=xor_hex(element_list[2][31], "20")
key[38]=xor_hex(element_list[2][38], "20")
key[53]=xor_hex(element_list[2][53], "20")
key[63]=xor_hex(element_list[2][63], "20")
key[65]=xor_hex(element_list[2][65], "20")
key[69]=xor_hex(element_list[2][69], "20")
key[72]=xor_hex(element_list[2][72], "20")
key[78]=xor_hex(element_list[2][78], "20")
key[83]=xor_hex(element_list[2][83], "20")
key[85]=xor_hex(element_list[2][85], "20")
key[89]=xor_hex(element_list[2][89], "20")

#from 4:
key[23]=xor_hex(element_list[3][23], "20")
key[33]=xor_hex(element_list[3][33], "20")
key[44]=xor_hex(element_list[3][44], "20")
key[54]=xor_hex(element_list[3][54], "20")
key[60]=xor_hex(element_list[3][60], "20")
key[68]=xor_hex(element_list[3][68], "20")
key[71]=xor_hex(element_list[3][71], "20")
key[91]=xor_hex(element_list[3][91], "20")
key[94]=xor_hex(element_list[3][94], "20")
key[103]=xor_hex(element_list[3][103], "20")
key[114]=xor_hex(element_list[3][114], "20")
key[124]=xor_hex(element_list[3][124], "20")
key[126]=xor_hex(element_list[3][126], "20")

#from 5:
#key[7]=xor_hex(element_list[4][7], "20")
key[17]=xor_hex(element_list[4][17], "20")
key[21]=xor_hex(element_list[4][21], "20")
key[27]=xor_hex(element_list[4][27], "20")
key[30]=xor_hex(element_list[4][30], "20")
key[34]=xor_hex(element_list[4][34], "20")
#key[39]=xor_hex(element_list[4][39], "20")
key[46]=xor_hex(element_list[4][46], "20")
key[50]=xor_hex(element_list[4][50], "20")
key[66]=xor_hex(element_list[4][66], "20")
key[69]=xor_hex(element_list[4][69], "20")
key[78]=xor_hex(element_list[4][78], "20")
key[90]=xor_hex(element_list[4][90], "20")
key[100]=xor_hex(element_list[4][100], "20")
key[114]=xor_hex(element_list[4][114], "20")

#from 6:
key[19]=xor_hex(element_list[5][19], "20")
key[22]=xor_hex(element_list[5][22], "20")
key[36]=xor_hex(element_list[5][36], "20")
key[37]=xor_hex(element_list[5][37], "20")
key[42]=xor_hex(element_list[5][42], "20")
key[48]=xor_hex(element_list[5][48], "20")
key[76]=xor_hex(element_list[5][76], "20")
key[88]=xor_hex(element_list[5][88], "20")
key[105]=xor_hex(element_list[5][105], "20")
key[121]=xor_hex(element_list[5][121], "20")
key[139]=xor_hex(element_list[5][139], "20")
key[154]=xor_hex(element_list[5][154], "20")

#from 7:
key[9]=xor_hex(element_list[6][9], "20")
key[35]=xor_hex(element_list[6][35], "20")
key[98]=xor_hex(element_list[6][98], "20")
key[108]=xor_hex(element_list[6][108], "20")
key[112]=xor_hex(element_list[6][112], "20")
key[129]=xor_hex(element_list[6][129], "20")
key[130]=xor_hex(element_list[6][130], "20")
key[148]=xor_hex(element_list[6][148], "20")

#from 8:
key[10]=xor_hex(element_list[7][10], "20")
key[49]=xor_hex(element_list[7][49], "20")
key[61]=xor_hex(element_list[7][61], "20")
key[73]=xor_hex(element_list[7][73], "20")
key[87]=xor_hex(element_list[7][87], "20")
key[115]=xor_hex(element_list[7][115], "20")
key[116]=xor_hex(element_list[7][116], "20")
key[120]=xor_hex(element_list[7][120], "20")

#from 9:
key[1]=xor_hex(element_list[8][1], "20")
key[15]=xor_hex(element_list[8][15], "20")
key[16]=xor_hex(element_list[8][16], "20")
key[41]=xor_hex(element_list[8][41], "20")
key[43]=xor_hex(element_list[8][43], "20")
key[62]=xor_hex(element_list[8][62], "20")
key[97]=xor_hex(element_list[8][97], "20")
key[107]=xor_hex(element_list[8][107], "20")
#key[123]=xor_hex(element_list[8][123], "20")
key[143]=xor_hex(element_list[8][143], "20")

#from 10:
key[4]=xor_hex(element_list[9][4], "20")
key[12]=xor_hex(element_list[9][12], "20")
key[29]=xor_hex(element_list[9][29], "20")
key[45]=xor_hex(element_list[9][45], "20")
key[52]=xor_hex(element_list[9][52], "20")
key[59]=xor_hex(element_list[9][59], "20")
key[67]=xor_hex(element_list[9][67], "20")
key[75]=xor_hex(element_list[9][75], "20")
key[77]=xor_hex(element_list[9][77], "20")
key[79]=xor_hex(element_list[9][79], "20")

#from guess:
key[0]=xor_hex(element_list[2][0], "54")
key[18]=xor_hex(element_list[9][18], "64")
key[25]=xor_hex(element_list[9][25], "6e")
key[56]=xor_hex(element_list[4][56], "70")
key[11]=xor_hex(element_list[4][11], "61")
key[86]=xor_hex(element_list[9][86], "67")
key[7]=xor_hex(element_list[4][7], "27")
key[36]=xor_hex(element_list[3][36], "63")
plain_text_list = []
for i in range(10):
    row = []
    for j in range(len(element_list[i])):
        
        if key[j]!="00":
            x = xor_hex(key[j], element_list[i][j])
            row.append(x)
        else:
            row.append("*")
    plain_text_list.append(row)
#print(plain_text_list)

plain_text = []
for row in plain_text_list:
    element = trans_to_string(row)
    #print(element)
    plain_text.append(element)

for pt in plain_text:
    print(pt)

target_list = []
target_list = split_hex_string(target_cipher_text)

result = []
for i in range(len(target_list)):
    tmp = xor_hex(target_list[i], key[i])
    result.append(tmp)

target_plain_text = ""
for i in range(len(target_list)):
    if key[i]=="00":
        target_plain_text += "*"
    else:
        target_plain_text += chr(int(result[i], 16))
print()
print(target_plain_text)

