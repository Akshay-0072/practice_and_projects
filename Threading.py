from threading import *
'''def display():
    for i in range(1, 11):
        print("Child Thread")
t = Thread(target=display())  #creating thread
t.start()
for i in range(1, 11):
    print("Main Thread")'''

'''class MyThread(Thread):
    def run(self):
        for i in range(10):
            print("Child Thread-1")
t=MyThread()
t.start()
for i in range(10):
    print("Main Thread-1")'''

class MyThread:
    def run(self):
        for i in range(10):
            print("Child Thread-2")
t=MyThread()
t = Thread(target=t.run)
t.start()
for i in range(10):
    print("Main Thread-2")