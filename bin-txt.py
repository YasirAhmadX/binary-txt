def TxtToBin(s):
    bin_s = "";
    for i in s:
        bin_s = bin_s + bin(ord(i)).lstrip('0b') + ' '
    return bin_s

#print(TxtToBin("ysr"))

def BinToTxt(bin_s):
    s = "";
    for i in bin_s.split():
        n = 0;
        i = i[::-1]
        for j in range(0,len(i)):
            n += int(i[j])*2**j
        s += chr(n)
    return s

#print(BinToTxt(TxtToBin("ysr")))
        

z = int(input("1. Text to Binary\n2. Binary To Text\nChoice: "))
match z:
    case 1:
        s = input("Enter string: ")
        print(TxtToBin(s))
    case 2:
        s = input("Enter binary seq: ")
        print(BinToTxt(s))
    case _:
        print("Invalid input")
    
        
