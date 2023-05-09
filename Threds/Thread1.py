# Threads for method

from threading import Thread

class Example:
    def Display(self):
        for i in range(4):
            print("Hello World")
 
E1 = Example()           
T1 = Thread(target=E1.Display)
T1.start()

for i in range(5):
    print("Welcome") 