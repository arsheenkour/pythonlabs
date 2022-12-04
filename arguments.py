
# keyword argument
#the passing of argument in any order by passing the name asign th name in write parameter is known as kwy word argument
#writeing a function  know ad fun ction name is marks is function name which contain 3 argument fisrt is class test float type 2nd is project float type 3rd is mtt defalt value is =0 and 4th is o0nline evaluation
x=float(input("ca"))
y=float(input("project"))
u=float(input("online test"))
z=float(input("mtt"))
def marks(x,y,u,z=0):
    return (x+y+u+z)
i=marks(x,y,u,z)
print(i)
marks(23,4,44)



import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake game by Edureka')
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

pygame.quit()
quit()
import pygame

pygame.init()
dis = pygame.display.set_mode((400, 300))

pygame.display.set_caption('Snake game by Edureka')

blue = (0, 0, 255)
red = (255, 0, 0)

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.draw.rect(dis, blue, [200, 150, 10, 10])
    pygame.display.update()
pygame.quit()
quit()


#qwrite a program to calculate taxQ6
x=int(input("salary"))
y=int(input("percent"))
def tax(x,y=20):
    print(x*(y/100))
tax(x,y)


# Evaluation topic sparse matrix : -
'''q.{
0,0,3,0,4
0,0,5,7,0
0,0,0,0,0
0,2,6,0,0
}
s.
{
0,0,1,1,3,3
2,4,5,3,1,2
3,4,5,7,2,6
}'''
# Read the sparsh matrix


# Multilevel inheritance:-
class one:
    x=20
    def fun1(self):
        print(self.x)
class two(one):
    y=200
    def fun2(self):
        print(self.y)
class three(two):
    z=150
    def fun3(self):
        print(one.x+two.y+self.z)
t1=three()
t1.fun1()
t1.fun2()
t1.fun3()



class Input:
    a=None
    b=None
    c=None
    def data(self):
        Input.a=int(input('enter a'))
        Input.b=int(input('enter b'))
class Sum(Input):
    def add(self):
        Input.c=Input.a + Input.b
        print(Input.c)
class Avg(Sum):
    def av(self):
        print((Input.c)/2)
d = Avg()
d.data()
d.add()
d.av()




#this is the more important method as far as constructor of the class:
class a:
    def _init_(self):
        print("parrents")
class b(a):
    def _init_(self):
        super()._init()# or we can w=use a.__init_(self) use the comment one this is better
        print("child")
obj2=b()
# Drive claas constractor will take the responsibility to pass the data to base class



class CA:
    Marks1=None
    def data(self):
        CA.Marks1=int(input('enter 1'))
class CA2(CA):
    Marks2=None
    def data(self):
        CA2.Marks2=int(input("enter 2"))
class CA3(CA,CA2):
    marks3=None
    def data(self):
        CA3.marks3 = int(input('enter 1'))
        def fun3(self):
            print(CA.Marks1+CA2.Marks2)
            def com:(CA,CA2,CA3)
            if CA.Marks1>CA2.Marks2 and CA2.Marks2>CA3.marks3:
                print(CA.Marks1+CA2.Marks2)
            else:
                print(CA.Marks1+CA3.marks3)

#class bestca:
#d = CA()
#d.CA2()
#d.CA3()
#d.data()
d.com()


class one:
    _x=20
    def fun1(self):
        print(self._x)
class two(one):
    y=200
    def fun2(self):
        print(one._x+self.y)
t1=two()
t1.fun1()
t1.fun2()
#t1.one()
#t1.fun1()

print(".....................herarchical Inheritance.................")
class superc:
    x=3
class sub(superc):
    pass
class sub2(superc):
    pass
class sub3(superc):
    pass
a=sub()
b=sub2()
c=sub3()
print(a.x,b.x,c.x)


a=int(input("a: "))
b=int(input("b: "))
if (a>b):
    print("maximum")
else:
    print("minimum")


n=input("Name")
r=input("Roll-no")
g=input("Registration number")
m=input("CGPA")
p=input("Phn.No")
d=(n,[r],g,[m],[p])
d[1][0]=43
d[3][0]=12
d[4][0]=1213132
a=tuple(d)
print(a)






"""
r+
w+ for read abnd write both
a+
"""
f=open("myfileq.txt","w")
l=["this is delhiu\n","this is paris\n","this is london\n"]
f.writelines(l)
f.close()
f=open("myfileq.txt","a")
f.write("today\n")
f.close()
f=open("myfileq.txt","r")
h=f.read()
print(h)
f1=open("myfileq.txt","rb")
print("output of readline after appending")
#print(f1.readlines())
print(f1.readline().decode('utf-8'))
print()


f1=open("kkkk.txt","w+")
n="hello to python file"
f1.write👎
f1.seek(0)
print(f1.read(6))
f1.close()
f1=open("kkkk.txt","r")
print(f1.read())
f1.close()
f2=open("kkkk.txt","a+")
f2.seek(5)
print(f2.tell())
print(f2.read())#after moveing the 5 posoition thne it read the next  characters till the position you want if you enter a value the it print till these values
f2.close()


f1=open("kkkk.txt","w+")
n="hello to python file"
f1.write👎
f1.seek(0)
print(f1.read(6))
f1.close()
f1=open("kkkk.txt","r")
print(f1.read())
f1.close()
f2=open("kkkk.txt","a+")
f2.seek(5)
print(f2.tell())
print(f2.read())#after moveing the 5 posoition thne it read the next  characters till the position you want if you enter a value the it print till these values
f2.close()


n=int(input(""))
if n//2!=0:
    print("Weird")
elif n//2==0 and 2<n<5:
    print("Not Weird")
elif n//2==0 and 6<n<20:
    print("Weird")
elif n>20 and n//2==0:
    print("Not Weird")



a = int(input("a: "))
b = int(input("b: "))
def sum(a,b):
    return a+b,(a+b)/2
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
sum(a,b)
sub(a,b)
mul(a,b)


def r(k):
    if(k>0):
        a = k + r(k-1)
        print(a)
    else:
        a=0
    return a
r(6)


#progrmas to  print something by useing while loops
#program to print first 10 even numbers
#first 10 odd numbers
x=1
while x<=9:
    x=x+2
    print(x)


str1 = input()
repo = "0123456789"
count = 0
str2 = " "
for i in str1:
      if i is repo:
            count += 1
      else:
            str2 = str2 + i
print(count)
print(str2)



import math
x = int(input())
y = int(input())
x = math.radians(x)
y = math.radians👍
r = math.sin(x)*math.cos(y)+math.cos(x)*math.sin👍
print(f"{r:.2f}")


#txt = "We are the so-called "Vikings" from the north."
#print(txt)
txt = "We are the so-called \"Vikings\" from the north."
print(txt)



#by default
def funname(a="param",b=6,c=78):
    print(a,b,c)
#for for loop
funname("koml",7800)
def f(*num):
    sum=0
    for i in range(len(num)):
        sum=i+num[i]
    print(sum)
#arguments and comments
f(1,2,3,4,5)
def fun(*args,**kwargs) :#arbitary and arbitrary keyword argument
    print("args: ",args)
    print("kwargs:",kwargs)

fun('geeks','for',"naman",first="geeks",mid="for",last="geeks",complete="effsdnfnsdkf")
#positional
def funname(a,b,c):
    print(a,b,c)
funname("naman",23,3.5)
funname(34,"kamal",40.75)
funname(4.678,12,"kailash")


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if _name_ == '_main_':
    print_hi('PyCharm')


# program to print the table of a number
i=1
num=int(input("enter the number:- "))
while i<= 9:
    i=i+1
    print(num,"*",i,"=",num*i)


# program to print the table of a number
i=1
num=int(input("enter the number:- "))
while i<= 9:
    i=i+1
    print(num,"*",i,"=",num*i)


#progrmas to  print something by useing while loops
#program to print first 10 even numbers
#first 10 odd numbers
x=1
while x<=9:
    x=x+2
    print(x)


# sliceing with negative indexing
str="This is my first string"
print(str[::-1])
print(str[4:0:-1])
print(str[::-2])
print(str[10:0:-5])
print(str[::-3])
print(str[8:0:-1])


# now this for the concatenation of the strings
#x=input()
#y=x[0:2]
#z=x[-3:-2]
#print(y+z)
#program for misssin first and last character
#x=input("input")
#y=x[1:-1:1]
#print👍
#x=input()
#if len>2:
    #y=x[0]
    #z=x[-1]
    #d=z
    #v=y
    #f=x[1:-1]
    #print(d+f+v)
#else:
    #print("wrong")
#x=input()
#y=input()
#print(x+y+y+x)
# program to remove a specific position removeing
#x=input()
#y=int(input())
#if y>0 and y<len(x):
#print(str[:n]+str[n+1:])
#last question for today
#enter your name print name in reverse
#x=input()
#print(x[-1:1:2])


#s=input()
#y=input()
#x=s[1:]
#z=y[1:]
#print(x+z)
# IN not in programs for python
#string="namankumar"
#print("p"in string)
#s=input()
#z=s[::-1]
#print(s*4)
#print(z*3)
#a=input()
#z=len(a)
#if z>=3:
    #print(a[0:4]*4)



#x=input()
#y=int(input())
#print(x*y)
#x=input()
#s=int(input())
#z=len(x)
#if s>z and s>0:
    #print(x*s)
#s=input()# we cannot delet the single character from the string
#s[0]='j'#del dosen't work for single character
#print(s)
#a="Welcome to Python"
#print(a.capitalize())#The first chartes is capital all are small
#print(a.upper())
#print(a.lower())
#print(a.title()) #frisrt char of every string is treated as capital
#print(a.swapcase())# small letters will become capital and capital become small
#print(a.split()) #will be comleted into this
#print(a.center(50,"")) #use for printing anything in the printing format like degin********raedfdf******** like that only we can use a single character
#b="hello how are you,hello"
#print(b.count("hello"))
#print(b.count("hello h"))
#print(b.replace('hello','bye'))



#join
#a="ab"
#l=["1","2","3","4","5"]
#print(a.join(l)) # for joining something ton the list
#a=input()
#b=len(a)
#print(a.capitalize())#The first chartes is capital all are small
#print(a.upper())
#print(a.lower())
#print(a.title()) #frisrt char of every string is treated as capital
#print(a.swapcase())# small letters will become capital and capital become small
#print(a.split()) #will be comleted into this
#use for printing anything in the printing format like degin*********raedfdf******** like that only we can use a single character
#b="@"




#print(b.join(a))
#a="Pellp Python"
#print(a.isupper())
#b="dkfbnsdc"
#print(b.islower())
#print(a.isalpha())
#print(a.isalnum()) it return true for both
#print(a.isdigit())
#print(a.isspace()) it is uses for cheking that the string has a blank space
#print(a.istitle()) if my string entered in in title case
##b=input()
#print(a*3+b)
#s=input()
#b=input()
#z=len(s)
#x=len(b)
#if z==x:
    #print("String ar same")
#else:
    #print(b+s+b)
#a="Hello Python"
#print(a.startswith('h'))
#print(a.endswith('n'))
#print(a.find('py')) for finding the position it gives us the first index whre search if search is not find then -1
#print(min(a))
#print(max(a))
#x=input("str")
#y="python"
#z="programing"
#if min(x)==y and max(x)==z:
    #print(min(x))
    #print(max(x))
#print("hello\t\thow ar you")
#print("hello \n\n how are ypu")
#print("it\'s very powerfull")



# practise code for the class 4 nov of python
# program for repr
#x="123\t456\n2432"
#print(repr(x))
# now we are ging to discuus the module program
# this is about tbhe string module
#import string
#print(string.punctuation)
#print(string.capwords("dfsff sefasf"))
#print(string.digits)
#print(string.hexdigits)
#print(string.octdigits)
#x=input()
#z=len(x)
#if z%2==0:
    #print(x[:len(x)//2])
#else:
    #print(x[length//2+1:])



# Lists for the python program:-
# lists are mutable type but string s are not (indexing,sliceing all allowed).
'''l1=[11,22,33,44,55,"naman"]
print(l1)
print(l1[0])
print(l1[4])
print(l1[5])
l2=[]
print(l2)
l3=list(("kamal",44,7777))
print(l3)
# list  is a fix name it will take a sequence according to  it code will be created a word constructor know about it on internet'''
#x=input()
#print(x.split(","))
'''l1=[1,2,3,4,"naman"]
l2=["kamal",5,6,7,99]
print(3*(l1+l2))
l1[2]=11
print(l1)
#aading any member in the list we use .apend
l1.append(3.5)
l1.append('ggj')
print(l1)'''
"""x=input()
y=list[x]
print👍
z=len👍
u=int(input())
if u>0 and u<z:
    print(y[u])
else:
    print("Invalid")"""
#program for the extend of the list
'''l1=[2323,3,3434,34,34]
l1.append(l1)
print(l1)
l2=[234234,324,34,3,4324,23]
l1.extend(l2)
print(l1)
l1.extend([23,4,5,5])
print(l1)
print(23  not in l1)
print(l2[::2])'''
'''x=input()
y=x.split()
if y[0]==3 or y[-1]==3:
    print("True")
else:
    print("False")
#this is homework
"""x=input()
y=x.split()
# if 1 and last is lower case case convert in in upeer case
if y[0].islower() or y[-1].islower():
    print(y[0].isupper)
else:
    print("invalid")"""

"""x=[1212,234,22323,23,23,23]
y=[1,1,1,1,1]
z=[1,1,1,1,1]
print(y==z)
print(x!=y)"""
"""s=0
x=[11,2,2,3,44,44,21]

z=x[0::2]
print(z)
u=x[0::3]
print(z[::-1])
print(u*5)"""
x=input()
s = x[len(x)//2:]
print(s)'''



s=input("")
print(len(s))
y="abCcdstu"
def length(str1):
    sum=""
    for i in range(0,len(str1)):
        if (s[i] in y):
            k=s[i]
            sum=sum+k
    print(len(s)-len(sum))
length(s)
'''s=input()
def lower(str1):
    print(str1.lower())
lower(s)'''



s=input()
def lower(str1):
    print(str1.lower())
print(lower(s))




# program for the tuple
#tuple is imutable
'''t=(1,2,3,4)
print(t[-2])# indexcing is dito same as list and string
print(type(t))
l=list(t)
l[3]='s'
print(l)
t2=tuple(l)
print(t2)
t3=('a',[2,3],'naman')
t3[1][1]=9
print(t3)'''
'''x=input()
    y=x.split(',')
z=list👍
u=tuple👍
print(u)
print(z)'''
#for crating a single element a coma sepration is minimum required
'''x=(1,"a",3.5,[1,2,3],(4,5,6),"python")
x[3][1]="2000"
print(x)'''
'''x=input()
y=x.split(',')
z=len👍
u=int(input())
if u<z:
    print(y[u])
else:
    print("Invalid index")
print👍
print(tuple(y))'''
'''l=['1','2','3','4']
v,b,n,m=l
print(v)
print(b)
print👎
print(m)'''
#swaping of variabkle without useing anything
'''a=20
b=50
c=9
(a,b,c)=(b,a,a)
print("value after",a,b,c)'''
#x=a,b,c,d
#print(type(x)
'''x=input()
y=x.split(',')
z=tuple👍
print(z)
o=int(input())
print(o in z)'''
'''x=('a','b','c','d',[1,2,3])
y=x.split(',')
del y[1][2]
print(tuple(y))'''
'''x=input()
y=x.split()
z=int(input())
f=len👍
g=input()
if z<f:
    y[z]=g
    print(tuple(y))
else:
    print("enter a valid number")'''
'''x=input()
y=x.split(',')
z=len👍
u=int(input())
if u<z:
    print(tuple( del y[u]))
else:
    print("enter a valid")'''
'''x=input()
y=x.split(',')
z=input()
for i in y:
    i=i+1
    if y[i]==z:
        f=del y[i]
        print(f)
    else:
        print("Not a valid (")'''
'''x=input()
y=x.split(',')
z=int(input())
u=int(input())
i=y[z:u]
print(tuple(i))'''
'''print(all((' ', ',','1','2')))
print(any((' ','1','2')))
x=(1,2,3,4,5,5)
print(tuple(enumerate(x)))'''
# program to print the number of times a list enter in a tuple
'''x=input()
y=x.split(',')
x=int(input())
z=len👍
if x<z:
    for  i in  range(z):
        if i==i:
            print(i)
        else:'''
'''x=input()
element=input()
z=tuple(x.split(","))
for i in range (0,len(z)):
    if x[i]==element:
        print(i)
else:
print("not in tuple")'''



# Python program to do the editing in the python program:-
#take input and create a tuple 1 and then create atuple
x=input()
y=x.split(",")
print(tuple(y))
q=tuple👍
z=input()
u=z.split(",")
i=tuple(u)
print(tuple(u))
(i,q)=(q,i)
print(i)
print(q)
#create a tuple
x=input()
y=x.split(",")
z=x.sorted()
k=z[1:-2]
print(tuple(k))



# dicctionaries:-
x=input("data1: ")
y=x.split(",")
d=input("data2:")
z=d.split(",")
di=dict(zip(y,z))
print(di.items())

g=input("key")
print(g in di)


# you have create a list contain key account balance
# yyou have to enter balance
# minimum balance is 1000
# sum one add minimum balace print ammount 1000
#and then print the updated list
x=input("data1: ")
y=x.split(",")
d=input("data2:")
z=d.split(",")
di=dict(zip(y,z))
print(di.items())
for i in z:
    if int(i)<1000:
        print(i==1000)
else:
    print(di.items())


file1 = open("myf.txt","w")#by changeing it into  a we ret new data
L = ["this  is delhi \n","this is paris \n","this is london \n"]
file1.write("Hello\n")
file1.writelines(L)
file1.close()

file1 = open("myf.txt","a")
file1.write("Today\n")
file1.close()

file1 = open("myf.txt","r")
print("output of readdding after appending")
print(file1.readlines())
print()

# create a tuple with data name first is name then roolno then your reg no then cgpa then your contact no
#roll no is modifiable
#cgpa will change and phn no
#update all thing one
#0name,1rollno,2regno,3cgpa,4contactno
x=input("Detail:")
y=x.split(',')
print(tuple(y))
y[1]='12'
y[2]='12312'
y[3]='93.2'
y[4]='9412439875'
print(tuple(y))



# dictionaries starting
x11={}
print(x11,type(x11))
x1={"x":1,"y":2,"z":3}
print(x1)
d=dict([("jan",1),("feb",2),("march",3)])#This is the fixed format#this is the fixed criteria
print(d)
print(d["march"])
#get method
print(d.get("jan"))
#indexing with key is allowed but not by the value is allowed
#we can use dict as a constructor
# in dictionaries indexing is by number not by value
# in dictionaries we can use indexing by provideing byt the keyvaluse not by  the number or like before we do  indexing
#none is also a keyword



#create a Dict with regno as a key and cgpa as value and contain 5 pair
d=dict([("regno",1),("cgpa",2),("name",3),("class",12),("id",12)])
x=int(input("regno"))
y=d.get("regno")
if x==y:
    z=d.get("cgpa",3)
    k=int(z+1)
    l=d.get("cgpa",k)
print(d)




my={"game":"chess","dish":"ch","sd":"ds"}
print(my.get('game'))
print(my['dish'])
print(my.get('sd'))
my['game']="cricekt"
print(my['game'])



# program to get the zip(zip is a master key)
l=[44,22,33]
print(tuple(zip(l)))
l1=["name","kamal","param"]
print(list(zip(l1)))
dict1=dict(zip(l,l1))
l3=[1,2,3]
dict2=tuple(zip(l,l1,l3))# this is use for the printing it in to  three values
print(dict2)#
print(sorted(dict1))
print(sorted(dict1.items()))#item is use for getiing the sorted values
# length must  be same for the both list



x=input("data1: ")
y=x.split(",")
d=input("data2:")
z=d.split(",")
di=dict(zip(y,z))
print(di.items())
for (i,j) in \
        (di):
    i=i+1
    j=j+1
    print(i,j)


x=input("data1: ")
y=x.split(",")
d=input("data2:")
z=d.split(",")
if len(y)==len(z):
    di=tuple(dict(zip(y,z)))
    print(sorted(di.items()))
else:
    print("Lenth should be equal")



x=input("data1: ")
y=x.split(",")
d=input("data2:")
z=d.split(",")
di=dict(zip(y,z))
print(di.items())
for (i,j) in \
        (di):
    i=i+1
    j=j+1
    print(i,j)


my={"game":"chess","dish":"ch","sd":"ds"}
my.pop("game")
print(my)
print(my.popitem())
print(my.clear())


#cretae a dict from 2 tples 1st tuple comtai nt ne value ind num from 0 2 is value ssun,sto sat
x=input("data1: ")
y=x.split(",")
j=tuple👍
d=input("data2:")
z=d.split(",")
k=tuple(z)
di=dict(zip(j,k))
print(di.items())
h=len(di)
s=0
for i in range(h):
    if i%2==0:
        s=s+1
print(s)




x=input("data1: ")
y=x.split(",")
d=input("data2:")
z=d.split(",")
di=dict(zip(y,z))
k=di.items()
print(all(k))
print(len(k))


x=input("data1: ")
y=x.split(",")
d=input("data2:")
z=d.split(",")
di=dict(zip(y,z))
print(di.items())
print(sorted(di.values()))






x=input("Enter the data for first list")
l1=x.split()
y=input("Enter the data for second list")
l2=y.split(",")
z=[eval(i) for i in l2]
d1=dict(zip(l1,z))
print(d1)
for i in d1:
    if(d1[i]<1000):
        d1[i]


d1={('a','b','c'):[1,2,3,4,5]}
print(d1['a','b','c'][3])
for i,j,k in d1:
    print(j,i,k)
    print(i,j,k)



#COMPREHENSION
d=[1,2,3,4,5,6,7,8,9,10]
l1=[i for i in d if(i%2==0)]
print(l1)

x=20
print(["even" if x%2==0 else "odd"])
print([a*b for a in [1,2,3] for b in [4,5,61]])

print([a for a in [1,22,33] for b in [1,33,44] if a==b])


l=[1,2,3,4,5]
d={key:value for key,value in enumerate(l)}
print(d)
d={k:v for k,v in enumerate(l,6)}
print(d)
d2={i:i+2 for i in range(10)}
print(d2)
d3={k:"pythonnn" for k in "codetantra"}
print(d3)



# second method for clas in pyrthion
'''class emp:
    name=None#(this is the other way wothout useing the pass int that case we needd to  define it before geting or useing it in the print time we need to define it above)
    sal=None
    age=None
emp1=emp()
name=input("name")
emp1.name=name
sal1=int(input("enter sal"))
emp1.sal=sal1
age1=int(input("enter age"))
emp1.age=age1
print(emp1.name)
print(emp1.sal)
print(emp1.age)'''
class kk:
    pass
k=kk()
name = input("Enter the name")
k.name=name
j=kk()
rollno = input("Enter the rollno")
j.rollno=rollno
h=kk()
hello = input("Enter the hello")
h.hello=hello
u=kk()
cl=kk()
cle=input("Enter the gym")
cl.cle=cle
print(k.name)
print(j.rollno)
print(h.hello)
print(cl.cle)





#the purpose of self is belong to the current object or int the class we work
'''class teacher:
    name=None
    uid=None
    sal=None
    def cal_tax(self):
        name="kb"
        uid=14335
        sal=60000
        tax=sal*0.20
        return tax
t1=teacher()#obj create
print(t1.cal_tax())'''
'''class kk:
    j=None
    i=None
    k=None
    def por(self):
        i=12
        j=23
        k=4
        return (j*i*k)
h=kk()
print(h.por())'''


'''class teacher:
    #name=None
    uid=None
    sal=None
    pass
    def _init_(self,x,y,z):#constructoe meythod tp init the data member
        self.name=x
        self.sal=y
        self.uid=z
    def cal_tax(self):#fun def
        tax=self.sal*0.20
        return tax
t1=teacher("sds",14335,65000)#obj created
print(t1.cal_tax())'''
#python program made by using the self function
class u:
    b=None
    x=None
    y=None
    g=None
    def _init_(self,q,w,e,t):
        self.b=q
        self.x=w
        self.y=e
        self.g=t
    def pro(self):
        z=self.b*self.y*self.x*self.g
        return z
t=u(1,2,3,4)
print(t.pro())


#define a class name as mathematics haveing two attributes var1,var2 write one method two initialize the two return the sum of these two variable return diff
class teacher:
    '''name=None
    uid=None
    sal=None'''
    pass
    def _init_(self,x,y):#constructoe meythod tp init the data member
        self.var1=x
        self.var2=y
    def sum(self):#fun def
        su =self.var1+self.var2
        print(su)
    def diff(self):
        di=self.var1-self.var2
        print(di)
t1=teacher(140335,65000)#obj created
print(t1.sum())
print(t1.diff())


#abstaction is use to hidding the detail private only i can,public all can see,protected i decide who can see
#the hidden thongs are comes in abstraction
class car():
    def setDetails(self,m,r):
    self.m=m
    self.r=r
    def g(self):
        return self.m
    def gr(self):
        return self.r
h=car()
o=car()
u=input("c1")
i=input("c1 r")
u1=input("c2")
i2=input("c2 r")
h.setDetails(u.i)
o.setDetails(u2,i2)
print(" h cars",h.g(),h.gr())
print(("m car",o.g(),o.gr()))


class cn:
    def (self,n=None,w=None):
        print👎
        print(w)
o=cn()
o.m()
o.m("pm")
o.m("sd","iud")


class animal():
    def speak(self):
        print("Animal speaking")
class Dog(animal):# derived class mane(parently)
    def bark(self):
        print("dog barkinng")
d=Dog()#single level inheritance int that one parent and one child class that is a single inhertance