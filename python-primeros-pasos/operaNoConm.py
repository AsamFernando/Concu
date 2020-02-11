import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

var1=1
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
    global lock
    try:
        lock.acquire()
        var1*=2
    finally:
        lock.release()

def dividirPorDos():
    global var1
    global lock
    try:
        lock.acquire()
        var1/=2
    finally:
        lock.release()

#dormir()
#dormir()

#t2.start()
#t1.start()


#t1.join()
#t2.join()

def logResultado():
    try:
        lock.acquire()
        logging.info(f'el resultado es: {var1}')
    finally:
        lock.release()


