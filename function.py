'''def add(x,y):  #Formal parameters
   # x=10
   # y=30
    #result=x+y
    return x*y

print(add(12,7)) #Actual parameters
 
#with argument with return type
def add(a,b):
    print("this is the first type")
    print(a+b)
x=add(2,4)
print(x)

#without argument with return type

def add():
    print("second type")
    a=int(input("enter a no"))
    b=int(input("enter value of b"))
    print(a*b)

x=add()
print(x)
print(type(x))
'''

def is_even(l):
    list1=[]
    for i in l:
        if i%2==0:
            list1.append(i)
    return list1
print(is_even([1,2,3,6,5,3,8]))



def reverse(str1):
    new=''
    index=len(str1)
    while index>0:
        new+=str1[index-1]
        index=index-1
    return new
print(reverse("consultadd123"))

x=[1,2,3,4,5]
y=[1,8,6,3,2]
var=map(lambda x,y:x+y, x,y)
new=list(var)
print(new)

