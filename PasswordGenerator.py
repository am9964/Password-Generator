from random import *
import string
#print(randint(15,16))
print("The password generated by us will have the following characteristics -\n--------------------------------------------------------------------------\
\n1. At least 8 characters\n2. At least 1 special character\n3.\
 At least 1 digit\n4. At least 1 lowercase character\n5. At least 1 uppercase charcter")
print("Enter the length of the password that you want to generate:")
l=int(input())
k=0
if(l<8):
    print("Enter greater than 8")
else:
    alphabet_string = string.ascii_lowercase
    lo = list(alphabet_string)
    alphabet_string = string.ascii_uppercase
    up = list(alphabet_string)
    sp=['!','@','#','$','%','^','&','*']
    dig=['0','1','2','3','4','5','6','7','8','9']
    w=""
    while(k<l):
        w+=choice(up)
        k+=1
        if(k==l):
            break
        w+=choice(lo)
        k+=1
        if(k==l):
            break
        w+=choice(dig)
        k+=1
        if(k==l):
            break
        w+=choice(sp)
        k+=1
        if(k==l):
            break
        w+=choice(up)
        k+=1
        if(k==l):
            break
        w+=choice(lo)
        k+=1
        if(k==l):
            break
        w+=choice(dig)
        k+=1
        if(k==l):
            break
        w+=choice(sp)
        k+=1
    print(w)