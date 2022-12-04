
# Class for unit 3 the user defined functions :-
def myname():#def of function
    print("hello this is first fun")
    print("will be executed")
    print("ok")

for i in range(4):
    myname()
def yourname():
    print("this is the second fun")


#modifiying the program for +-*/
x=int(input("enter the first"))
y=int(input("enter the second"))
def calculator():
    print("sum is ",x+y)
    print("multiply",x*y)
    print("subtraction",x-y)
    print("divide",x/y)
calculator()

def add():
    x=int(input("num1"))
    y=int(input("num2"))
    print("sum is",x+y)
    print(("sub",x-y))
def sub():
    x=int(input("num1"))
    y=int(input("num2"))
    print("diff is ",x-y)
# Docsting topic:-(docstrings are executable but comments are executable
def abc():
    """function is defined to print string abc
    a--is the firstline
    b---is the second"""
    print(a*b)

# program for docstings
def fun():
    """this is function comments and will be printed my docstring"""
    print(fun._doc_)
    print("hello")
fun()




def fun(a):
    sumodd=0
    sumeven=0
    while (a!=0):#this is the logic to print all the digits by useing for loop
        rem1=a/10
        if(rem1%2==0)
            sumeven=sumeven+rem1
        else:

x = int(input("any digit number"))
fun(x)
rem1=a/10
        sum=sum+rem1
        a=a//10
        if (a%2==0):
            rem1 = a / 10
            sum = sum + rem1
            a = a // 10
            print(sum)
        elif (a%3==0):
            rem1 = a / 10
            sum = sum + rem1
            a = a // 10
            print(sum)
#find the reverse of any  digit iof the number

# program fot defalt arguments
# function call is the ar
def si(rate=1.5,year=1,pr=1000):
    simple=(rate*year*pr)/100
    print(simple)
si(3.75,2)

x=int(input())
for i in range(1,x+1):
    if i%2!=0:
        if x%i==0:
            print(i,end=" ")


#for checking the prime :-
#n=int(input("enter the number"))
#k=0
#if n==0 or n==1:
    #print("not a prime number")
#else:
    #i=2
    #while(i<n):
        #if n%i==0:
            #k=k+1
        #i=i+1
#if k==0:
    #print(n,"is prime")
#else:
    #print(n,"is not prime")
# program to print all the factors of anumber useing for loop
n=int(input("number"))
print("factors are : ")
i = 1
while(i<=n):
    if n%i==0:
        print(i)
    i = i+1


# 12 oct class of python :-
# POSITIONAL ARGUMENTS:-

def funname(a,b,c):
    print(a,b,c)
funname("naman",23,3.5)
funname(34,"kamal",40.75)
funname(4.678,12,"kailash")


def funname(a="param",b=6,c=78):
    print(a,b,c)

funname("koml",7800)
funname()#if second is not defalt then interpreator not work if 1st and 3rd are default


# we need to use length :-
def f(*num):
    sum=0
    for i in range(len(num)):
        sum=i+num[i]
    print(sum)
f(1,2,3,4,5)



def f(*num):

    for i in range(len(num)):
        if i%2!=0:
            print(i)
f(1,2,3,4,5)


# Variable and argument #keyword arguments :-
def nameage(*,name,age):#this is by default positional(*) means dealing with keyword argument(use can use with * or without star
    print(name,age)
nameage(age = 62,name = "ramana")
nameage(name = "raman",age = 62)
nameage(name="rama",age =  87 )
#at the time of calling we must need to  give the keyword


# arbitary arguments use for decideing letter my function will take one argument or 2 arguments
# with * we can do any number of arguments(* is for arbitarary)_
def fun(*name):
    print(name)
    print(name[0])
fun("namf","kaod",23,45.6,"hsda5ss")


def fun(*args,**kwargs) :#arbitary and arbitrary keyword argument
    print("args: ",args)
    print("kwargs:",kwargs)

# now we can use both *args,kwargs
# to pass arguments to this function
fun('geeks','for',"naman",first="geeks",mid="for",last="geeks",complete="effsdnfnsdkf")



# Anonymous function(lambda is reseve word : is what to  do
# Single line subsitution
name = lambda a,b,c,d:a*b*c/d#(lamda is for expresion and lambda is a expression function
print(name(15.6,6,2,10))



x=int(input("salry"))
y=20/100
z=lambda
print(z)


x=int(input("salry"))
y=20/100
z=lambda
print(z)


#4 function with comman input
x=int(input())
y=int(input())
def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def div(x,y):
    print(x/y)
add(x,y)
sub(x,y)
multiply(x,y)
div(x,y)



#Q5
a=int(input())
b=int(input())
def avg(a,b):
    sum=a+b
    avg=sum/2
    return sum,avg
def add(a,b)
# Write a program tp print a pascal triangle nd print the result as shown in example(hw remind in nxt class)
#example
#n=4
#1
#11
#121
#1331


#useing of return function in any program is known as return function:-as fruitfull fun
def process(a,b):
    return(a-b,a+b,a*b,a/b)#multiple return is allowed
x=int(input("enter a number1"))
y=int(input("enter a number2"))
a1,b1,c1,d1=process(x,y)
print(a1,b1,c1,d1)#by defalut return type is none


# gue 3 for docstring
x=int(input())
y=int(input())
z=int(input())

def multiply(x,y,z):
    """this is program in first line
    use for multiplication"""
    print(x*y*z)

print(multiply._doc_)
multiply(x,y,z)


#useing of return function in any program is known as return function:-as fruitfull fun
def process(a,b):
    return(a-b,a+b,a*b,a/b)#multiple return is allowed
x=int(input("enter a number1"))
y=int(input("enter a number2"))
a1,b1,c1,d1=process(x,y)
print(a1,b1,c1,d1)#by defalut return type is none


#docstring
def fun():
    """this function is used for
     demo"""
    print("demo")