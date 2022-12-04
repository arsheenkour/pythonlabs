if z==j or i==o:
    print("same")
else:
    print("not same")'''
#create a list with 10 member after enter a data creat
'''x=input()
y=x.split(',')
print(y[1:-1:2])
print(y[0:-1:2])'''
'''m=input("enter the data ")
x=m.split(',')
y_even=[]
z_odd=[]
for i in range(0,len(x)):
    if (i%2==0):
        y_even.append(x[i])
    else:
        z_odd.append(x[i])
print(x)
print(y_even)
print(z_odd)'''
#del keyword is use to delet the keyword from the string
'''m=input("enter the data ")
x=m.split(',')
for i in range(0,len(x)):
    if (i%2==0):
        x[i]=int(x[i])
print(x)
del(x[3])
print(x)
#deletion  for multiple part
del(x[0:2])
print(x)
del(x[])
print(x)'''
'''x=[1,2,3,45,6]
print(x)
x.remove(3)
print(x)
x.clear()
print(x)
z=x.pop()# pop is the operation use to remove the operator from the last position
print(z)'''
#write a program to remove duplicate from a list
#this question is not write
'''x=input()
y=x.split(',')
"""z=[]
for i in range(len(x)):
    if z not in y:
        z.append(y[i])
print👍
print(z)"""
s=0
for i in range(int(y)):
    i=i+1
    s=s+1
print(s)'''
'''#listfunctions
x=[1,2,3,4,0]
print(all(x))
print(any(x))
print(list(enumerate(x)))
print(len(['w','e','r','r'',']))'''
# for finding the largest number of the list we are useing the max,min for largest in al list:
'''x=input()
y=x.split(',')
d=max👍
f=min👍
g=d-f
print(g)
print(d)
print(f)'''


'''x=input()
y=x.split(" ")
z=[eval(i) for i in y]
print(z)
k=int(input())
if (k<0) or (k not in range(len(z))):
    print("Invalid Index")
else:
    l=str(z[k])
    m=list(l)
    print(len(m))'''

x=input()
y=x.split(" ")
z=[eval(i) for i in y]
z.pop(min(z))
k=min[z]
print(z)


import random
class check:
    pass
A=int(input("Enter the number 1: "))
B=int(input("Enter the number 2: "))
r=random.randint(A,B)
def  che(A,B):
    if r >= 0:
        print(r, "is a positive number")
    else:
        print(r, "is an negative number")
    if r % 2 == 0:
        print(r, "is an even number")
    else:
        print(r, "is an odd number")
    if r > 1:
        for i in range(2, r):
            if (r % i) == 0:
                break
        else:
            print(r, "is an prime number")
    else:
        print(r, "is an composite number")
che(A,B)


import random # We import the random function
A=int(input("Enter the number 1: "))
B=int(input("Enter the number 2: "))
r=random.randint(A,B) # We are using here random function
if r>=0:
    print(r,"is a positive number")
else:
    print(r,"is an negative number")
# In above condition we check that it is a positive or negative number
if r%2==0:
    print(r,"is an even number")
else:
    print(r,"is an odd number")
# In above condition we check that it is a even or odd number
if r>1:
    for i in range(2,r):
        if(r%i) == 0:
            break
    else:
        print(r,"is an prime number")
else:
    print(r,"is an composite number")
# In above condition we check that it is prime or composite number


def myfun(a,b):
    return a+b
x=map(myfun, ("apple","banana","cherry"),("orange","lemon","pineapple"))
print(x)
print(list(x))



#a=int(input("a: "))
#b=int(input("b: "))
#def sum(a,b):
    #return a+b ,(a+b)/2
#def sub(a,b):
    #return a-b
#def mul(a,b):
    #return a*b
#x=sum(a,b)
#y=sub(a,b)
#z=mul(a,b)
#print("sum,average: ",x)
#print("subtraction: ",y)
#print("multiplication: ",z)
#a=int(input("a: "))
#b=int(input("b: "))
#def x(a,b):
    #return a+b
#def y(a,b):
    #return a-b
#s=x(a,b)
#d=y(a,b)
#print("addition:",s)
#print("subtraction:",d)
#def s(username):
def s(user):
    g="Hello"
    print(g,user)
l =[1,2,3,4,5,5]

s(l)


def square(n):

    for i in range(1,n+1):

        for j in range(1,n+1):
            if(i==1 or i==n or j==1 or j==n):
                print('*',end='')
            else:
                print('',end='')

        print()
num=int(input())
square(num)