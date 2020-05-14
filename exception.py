while True:
    try:
        x=int(input("enter a value"))
        y=int(input("enter a value"))
        avg=(x+y)/2

    except ValueError as err:
        print("Please provide an integer value",err)
    else:
        print("AVerage is",avg)
        break
    finally:
        print("Always executed")
    
    