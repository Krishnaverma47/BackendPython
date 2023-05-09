#import Thread class
from threading import Thread,current_thread

#Create a function containing code to be excuted parallaly
def Display(n,msg):
    print("T1 thread details.",current_thread())
    for i in range(n):
        print("Hello ",msg)
#Create new thread here
T1 = Thread(target=Display, args=(4,"Ram")) #if you pass one argument then pass args=(4,), you can pass keyword argument using kwargs={'hello':'world'}

#start the new thread
T1.start()

print("Main thread details.",current_thread())
for i in range(4):
    print("Welcome Krishna")