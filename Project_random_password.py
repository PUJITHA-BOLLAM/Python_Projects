import secrets
import string
import math
characters=string.ascii_letters+string.digits+string.punctuation
n=int(input("Enter the length of the password you want (min.charcters 8) "))
if(n>8):
    list1=[]
    for i in range(n):
        list1.append(secrets.choice(characters))
    password=''.join(list1)
    entropy=n*math.log2(len(characters))
    print("Password - ",password)
    print("Entropy - ",round(entropy,2),"bits")
else:
    print("Password must be more than 8 characters")
