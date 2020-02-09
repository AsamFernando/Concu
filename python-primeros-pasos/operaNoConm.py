import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

var1=3
lock= threading.Lock()

def dormir():
    time.sleep(3)

def sumarUno():
    global var1
    global lock
    try:
        lock.acquire()
        var1+=1
    finally:
        lock.release()
def multiplicarPorDos():
    global var1
    var1*=2
    try:
        lock.acquire()
        var1*=2
    finally:
        lock.release()


logging.info('creando los threads')
t1=threading.Thread(target=sumarUno)
t2=threading.Thread(target=multiplicarPorDos)


#dormir()

t1.start()

dormir()
t2.start()


t1.join()
t2.join()

logging.info(f'var1 es: {var1}')

