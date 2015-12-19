#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

## Stump for submitting flags to the submission server in attack&defense-style ctf
## This actually needs proper implementation of the various functions etc.
## This stump was created during an A&D-ctf by our team KITCTF (www.kitctf.de)

## TODO: make this more than a stump

import re
import traceback
import par


flagformat = r'FAUST_[A-Za-z0-9/\+]{32}'
submission_server = ('10.67.2.1', 666)
attackservers = '10.66.%d.2'
port = 1337
TIMEOUT = 8

def submit(flags):
    s = socket.create_connection(submission_server)
    already_sub = open("flags", "r").read()
    with open("flags", "a") as out:
        for f in flags:
            if f not in already_sub:
                out.write(f + "\n")
                s.send(f + "\n")
    s.close()

def findflags(str):
    submit(re.findall(flagformat, str))

def get(i):
    print "Getting",i
    try:
        r = pwnit.remote(attackservers%i, port, timeout=TIMEOUT)
        pwn(r)
    except Exception, e:
        print "Exception for %d" % i
        traceback.print_exc(e)

def execute():
    while(True):
        par.iter_parallel(get, list(range(1,240)), n=16)
        pause(30)

def pwn(target):
    pass

if __name__ == '__main__':
    execute()