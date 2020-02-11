import logging
import threading

from operaNoConm import sumarUno
from operaNoConm import multiplicarPorDos
from operaNoConm import logResultado



logging.info('creando threads')
t1=threading.Thread(target=sumarUno)
t2=threading.Thread(target=multiplicarPorDos)
t3=threading.Thread(target=logResultado)

logging.info('comenzando thread 1 SumarUno')
t1.start()
logging.info('comenzando thread 2 multiplicarPorDos')
t2.start()

t3.start()