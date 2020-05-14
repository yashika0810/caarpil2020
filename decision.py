'''x=int(input("Enter any integer"))
if x<0:
    if x>-5:
        print("result is greater than -5")
    else:
        print("result is less than -5")   
elif x==0:
    print("result is 0")
elif x>0 and x<30:
    print("result is positive and in the range 30")
else:
    print("result is greater than 30")


while True:
    print("Enter a number but -1 will quit the loop and -2 will keep you in the loop")
    x=int(input("enter your number"))
    if x==-1:
        break
    if x==-2:
        continue
    print("I am inside the loop")
print("I am outside the loop")


avg=0
total=0
count=0
print("Enter the grade (-1 to quit)")
grade=int(input("Enter your grades"))
while grade!=-1:
    total=total+grade
    count=count+1
    print("Enter the grade (-1 to quit)")
    grade=int(input("Enter your grades"))
    if count==5:
        break

avg=total/count
print("Avg of subjects is",avg)


numbers=[1,2,3,4,5,6,7]
new_list=[]
for i in numbers:
    if i%2==0:
        new_list.append(i**2)
print(new_list)


my_list=[]
for i in [20,40,60]:
    for j in [2,4,6]:
        my_list.append(i*j)
print(my_list)
'''


n=2
s="consultadd"
print(s*2)


#chunks of list
#[1,2,3,4,5,6]--> [[1,2],[3,4],[5,6]]

def chunk(list,size):
    return [list[i:i+size] for i in range(0,len(list),size)]
print(chunk([1,2,3,4,5,6],2))


# join , split

training=["Java","python","aws"]
print("my trainings are")
print(" ".join(training))

#using split

s="Hello"
a=s.split()
print(a)

def split(word):
    return [i for i in word]
print(split("hello"))


def get_vowel(string):
    return [i for i in string if i not in 'aieou']
print(get_vowel("consultadd"))


def palindrom(a):
    return a==a[::-1]
print(palindrom("abcd"))



