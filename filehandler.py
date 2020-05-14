'''with open("data.txt",'r') as file:
    data=file.readline()
    for i in data:
        word=i.split()
        print(word)


try:
    filehandler=open("dat.txt",'r')
    content=filehandler.read()
    print(content[:20])
    print(type(content))
except:
    print("enter the correct name of file")
finally:
    filehandler.close()

try:
    fh=open("test.txt",'r')
    fh.read()
except IOError:
    print("Error! can't find file or read data")
else:
    print("Written content successfully")
    fh.close()


from sys import argv
name_of_program, filename=argv

print("Name of program is", name_of_program)
print("Name of file is",filename)


while True:
    try:
        fh=open(filename,'r')
        content=fh.read()
        print(content)
        fh.close()
        break

    except:
        print("The name entered is wrong. Provide correct name")
        try_again= input("Do you want to try again?? Press 'Y' for yes and 'N' for no")
        if try_again=='Y':
            filename= input("please enter the name correctly this time")
        else:
             break
'''

#CLASS INSIDE CLASS

class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

   
    def show(self):
        print(self.name,self.rollno) #so we dont have to use print(s1.name,s1.rollno) all the time

    class laptop(): #creating class inside class, object is defined outside
        def __init__(self):
            self.brand='acer'
            self.cpu='i5'

        def show(self): #this showis for laptop(inside class)
            print(self.brand,self.cpu)
            self().lap.show()
        


s1= student('Jace',1)
s2=student('Aman',2)

s1.show()
 








