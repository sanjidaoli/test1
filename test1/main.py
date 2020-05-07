import logging
from time import sleep,ctime
import  _thread
logging.basicConfig(level=logging.INFO)

loops=[2,4]
def loop(nloop,nsec,lock):
    logging.info("start loop at "+str(nloop)+ ctime())
    sleep(4)
    logging.info("end loop0 at "+ str(nloop)+ctime())
    lock.release()
# def loop1():
#     logging.info("start loop1 at "+ ctime())
#     sleep(2)
#     logging.info("end loop1 at "+ ctime())

def main():
    logging.info("start all at "+ ctime())
    locks=[]
    nloops=range(len(loops))
    for i in nloops:
        lock=_thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        _thread.start_new_thread(loop,(i,nloops[i],locks[i]))
    for i in  nloops:
        while locks[i].locked():pass
    sleep(6)
    logging.info("end all at "+ctime())

if __name__=="__main__":
    main()