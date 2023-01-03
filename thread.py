from time import sleep
from threading import *
import ss
import monitorapp as ma

class App1(Thread):
    def run(self):
        app1 = ma.Monitor()
        app1.mainloop()

class App2(Thread):
    def run(self):
        app2 = ss.ScrRead()
        app2.mainloop()

t2 = App2()
t1 = App1()

t2.start()
sleep(1)
t1.start()
