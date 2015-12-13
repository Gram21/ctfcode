#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Python exploit template.
#
# Author: Jan Keim aka Gram21, Gramarye

from pwn import *

####################################
#          Target System           #
####################################
target = "localhost"
port = 1337
binary = "./binary"

# set the context: i386, amd64
context.update(arch='i386', os='linux')

####################################
#            Settings              #
####################################
# Set the context level to debug:
DEBUG = False
# Set if recv should automatically print
PRINTER = True
TIMEOUT = 2

####################################
#       convenience wrappers       #
####################################

def send():
	r.send()

def sendline(s):
	r.sendline(s)

"""recvuntil then send"""
def sendafter(delim, data, shallprint=PRINTER):
	tmp = r.sendafter(delim, data)
	if shallprint:
		log.success(tmp)
	return tmp

"""recvuntil then sendline"""
def sendlineafter(delim, data, shallprint=PRINTER):
	tmp = r.sendlineafter(delim, data)
	if shallprint:
		log.success(tmp)
	return tmp

"""sendline and then recvuntil"""
def sendlinethen(delim, data, shallprint=PRINTER):
	tmp = r.sendlinethen(delim, data)
	if shallprint:
		log.success(tmp)
	return tmp

"""send and then recvuntil"""
def sendthen(delim, data, shallprint=PRINTER):
	tmp = r.sendthen(delim, data)
	if shallprint:
		log.success(tmp)
	return tmp

def recv(shallprint=PRINTER):
	tmp = r.recv()
	if shallprint:
		log.success(tmp)
	return tmp

def recvline(shallprint=PRINTER):
	tmp = r.recvline()
	if shallprint:
		log.success(tmp)
	return tmp

"""recv until s appeared. drop s if drop=true"""
def recvuntil(s, shallprint=PRINTER, drop=False):
	tmp = r.recvuntil(s,drop)
	if shallprint:
		log.success(tmp)
	return tmp

def recvn(n, shallprint=PRINTER):
	tmp = r.recvn(n)
	if shallprint:
		log.success(tmp)
	return tmp

def recvregex(r, shallprint=PRINTER, exact=False):
	tmp = r.recvregex(r, exact)
	if shallprint:
		log.success(tmp)
	return tmp

####################################
#               PWN                #
####################################
if DEBUG:
	context.log_level = 'debug'
# Connect to target
r = remote(target, port, timeout=TIMEOUT)
# Connect to process
#r = process(binary)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#         Your code here
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Things that can be used:
# time.sleep(1)
# cyclic(100), cyclic_find("aaaa")
# p32(0xdeadbeef), u32(s), p32(0xdeadbeef, endian='big') etc.
# asm(shellcraft.sh()) or similar
# pause()/pause(n) -> waits for user input or n seconds

def pwn():
    pass

# start the pwn
pause() # requires user input to start (e.g. for wating for server)
pwn()


# When there is a shell
# r.interactive()