#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import sys, os
import scapyClassDdos

def daemonize():
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)  #first parent out
    except OSError, e:
        sys.stderr.write("fork #1 failed: (%d) %s\n" %(e.errno, e.strerror))
        sys.exit(1)
    
    os.chdir("/")
    os.umask(0)
    os.setsid()
    
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0) #second parent out
    except OSError, e:
        sys.stderr.write("fork #2 failed: (%d) %s]n" %(e.errno,e.strerror))
        sys.exit(1)

    

def _example_main():
    import time
#    sys.stdout.write('Daemon started with pid %d\n' % os.getpid())
#    sys.stdout.write('Daemon stdout output\n')
#    sys.stderr.write('Daemon stderr output\n')
    print '%d\n' % os.getpid()
   
   
def lyuePrint():
    while True:
#    for i in range(0,1000):
        print 'lyue'


def main():
    daemonize()
    scapyClassDdos.main()

main()
