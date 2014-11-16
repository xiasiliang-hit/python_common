import Queue;
import threading;
import time;
import pdb;
import sys;
import os

nThread = 8;

datapath = './data/'
processed = './data/processed/'

class Para:
    def __init__(self):
        self.a = 0
        self.b = 0

class MyThread(threading.Thread):    
    def __init__(self, queue, my_num):
        threading.Thread.__init__(self);
        self.queue = queue
        self.my_num = my_num 
    def run(self):
        while True:            
            if self.queue.empty():
                break;
            else:
            #running job of one thread, multi-obj will be in parallel
                #$2 modify here if parameter for a thread need to be processed
                para = self.queue.get()
                singleThread(para)
                        
            #signals to queue job is done
                self.queue.task_done();
                #print ("global contentCount: " + str(crawl.contentCount));
                
        print ("thread terminate:" + str(my_num))
        return
    
def singleThread(para):

    #$3 overwrite single thread here
    return

    
def multiThread():
    queue = Queue.Queue();

    #$1 pass para to each single thread
    #populate queue with data   
    for sth in sth_list:
        queue.put(para);
            
        print(para)
            
    #spawn a pool of threads, and pass them queue instance 
    for i in range(nThread):
        t = MyThread(queue);
        t.setDaemon(True);
        t.start()
                   
    #wait on the queue until everything has been processed     
    queue.join()
    return;

def main():
#    pdb.set_trace();
    start = time.time();
    multiThread()
    
    print("nThread: " + str(nThread));
    print("Time used for multithread: %s" % (time.time() - start));

    return

if __name__ == "__main__":
    main();
