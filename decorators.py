def decorator(func1):
    def inner():
        print("This is before function execution")
        x=int(input("enter a value"))
        y=int(input("enter a value"))
        res=x+y
        print(res)
        func1()
    return inner

#main code starts
@decorator
def need():
    print("I need to be decorated")

#need=decorator(need)
need()
