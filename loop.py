'''
for i in x:
    print("list elements:",i)
print("the list has", len(x),"elements")


x=[1,2,3,4,5,6]
# range(len(x))--> len(x)-->6-->range(6)
for i in range(len(x)):
    x[i]=x[i]+6
print(x)


for i in range(3):
    for x in range(10,14):
        print(i,x)


#n=5/6
#{1:1,2:4,3:9,4:16,5:25}

n=int(input("enter any number"))
d=dict()
for i in range(1,n+1):
    d[i]=i**2
print(d)


#consultadd123

s=input("enter any word")
d={"Digits":0,"Letter":0}
for i in s:
    if i.isdigit():
        d["Digits"]+=1
    elif i.isalpha():
        d["Letter"]+=1
    else:
        pass  #executes nothing

print("Letters: ", d["Letter"])

print("Digits: ", d["Digits"])


x=[1,7,5,7]
for elements in x:
    if elements % 2==0:
        print("List contains an even no")
        break
        print("list does not contain even no")

# this else executes only if break is NEVER reached and loop terminates after all iterations
#else:
    #print("list does not contain even no")
    

while True:
    x=int(input("enter a no"))

    y=int(input("enter a no"))
    res=x/y
    print(res)
'''
