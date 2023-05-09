#Threading inhreating thread method.

from time import sleep
from threading import Thread

videos = ['OOPS Syllabus','Constructor','Destructor','File handling']

def Upload(vid):
    for video in vid:
        print(f"{video} started uploading...")
        sleep(1) 
        print(f"{video} uploaded.")  
    
class New_Thread(Thread):
    def run(self):
        Upload(videos) 
            
T1 = New_Thread()
T1.start()

for i in range(4):
    sleep(0.5)
    print("Checking copyrights")
    


            