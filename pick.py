# import pickle
# # data={2:33,22:54,66:84}
# # var=open('test.pickle','wb')
# # pickle.dump(data,var)
# # var.close()

# var2=open('test.pickle','rb')
# emp=pickle.load(var2)
# print(emp)

from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(0.2)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.2)

t1=Hello()
t2=Hi()

t1.start()
t2.start()

t1.join()
t2.join()

print("Bye")