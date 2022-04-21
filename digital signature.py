# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 20:48:13 2021

@author: hp
"""

#import math
import hashlib
import random
def modinv(a,m):
    a = a%m
    for x in range(1,m):
        if((a*x) % m == 1):
            return(x)
    return(1)
def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True
def hasher(message):
    hash_val = hashlib.sha1(message.encode("UTF-8")).hexdigest()
    return hash_val
p=0
while(1):
    tmp=random.randint(101, 999)
    if isprime(tmp):
        p=tmp
#p = int(input('Enter the value of p(must be a prime number): '))
#print('\nAll possible values for q:')
    temp=[]
    for q in range(2,p):
        if ((p-1)%q == 0) and isprime(q) and q>9:
            temp.append(q)
#q = int(input('Select a value for q from above(must be quite large): '))
    if(len(temp)!=0):
        break
q=temp[0]
print('\nThe value of p is: ',p)
print('The value of q is: ',q)        
flag = True
while(flag):
   # h = int(input("Enter a value for h between 1 and (p-1) : "))
    h=random.randint(1,(p-1))
    if(1<h<(p-1)):
        g=1
        while(g==1):
            g = pow(h,int((p-1)/q)) % p
        flag = False
    else:
        print('Invalid Entry')
print('\nThe value of g is: ',g)
#x = int(input('Enter a random value for x between 1 to (q-1): '))
x=random.randint(1, (q-1))
print("\nThe private key(x) is: ",x)
y = (g**x) % p
print("The public key(y) is: ",y)
def signature(name,p,q,g,x):
    with open(name) as file:
        text = file.read()
        hash_comp = hasher(text)
        print("Hash of the document sent is: ",hash_comp)
    r = 0
    s = 0
    while(s==0 or r==0):
       # k = int(input('Enter a value for k(between 1 to (q-1)): '))
        k=random.randint(1,(q-1))
        r = ((pow(g,k))%p)%q
        i = modinv(k,q)
        hashed = int(hash_comp,16)
        s = (i*(hashed+(x*r))) % q
    return(r,s,k)
def verification(name,p,q,g,r,s,y):
    with open(name) as file:
        text = file.read()
        hash_comp = hasher(text)
        print("Hash of the recieved document is: ",hash_comp)
        w = modinv(s,q)
        print("\nValue of w is: ",w)
        hashed = int(hash_comp,16)
        u1 = (hashed*w) % q
        u2 = (r*w) % q
        v = ((pow(g,u1)*pow(y,u2))%p)%q
        print("Value of u1 is: ",u1)
        print("Value of u2 is: ",u2)
        print("Value of v is: ",v)
        if(v==r):
            print("\nThe Signature is valid")
        else:
            print("\nThe Signature is invalid,The Document is modified")
print()
file_name = input("Enter the File name to sign: ")
comp = signature(file_name,p,q,g,x)
print("\nr(Component of Signature) is: ",comp[0])
print("k(Random number) is: ",comp[2])
print("s(Component of Signature) is: ",comp[1])
print()
file_name = input("Enter the File name to verify: ")
verification(file_name, p, q, g, comp[0], comp[1], y)

