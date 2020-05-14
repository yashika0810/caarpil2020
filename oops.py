'''class employee:
    def name(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
obj=employee()
print(obj.name("welcome","training"))


class candidate:
    def check(self,par1,par2):
        return par1+par2
obj1=candidate()
print(obj1.check(1,2))


class test:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj1=test('yashika',24)
print(obj1.name,obj1.age)
'''

class consultadd:           #parent/super/base
    def __init__(self,domain):
        self.domain=domain
    def getname(self):
        return self.domain
    def candidate_attend(self):
        return False

class pcandidate(consultadd):    #child class
    def candidate_attend(self):
        return True

c=consultadd("Python")
print(c.getname(),c.candidate_attend())
p=pcandidate("Java")
print(p.getname(),p.candidate_attend())

#Polymorphism --> 

class candidate:
    def domain(self):
        print("I am learning Python")
    def language(self):
        print("Python")
    def level(self):
        print("Intern")
class Trainer:
    def domain(self):
        print("I train in Python")
    def language(self):
        print("Python")
    def level(self):
        print("Expert")

c=candidate()
t=Trainer()
for i in (c,t):
    i.domain()
    i.language()
    i.level()


