import string
import random
s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)
while True:
    plen = int(input("Enter Length Of Password: "))
    random.shuffle(s)
    password = s[0:plen]
    print("Your Password Is: ",end="")
    print("".join(password))