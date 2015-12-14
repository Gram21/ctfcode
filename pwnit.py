#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

# Python exploit template.
#
# Author: Jan Keim aka Gram21, Gramarye

from pwn import *

####################################
#          Target System           #
####################################
# Server Connection
target = "localhost"
port = 1337

# Process Connection
#binary = "./binary"

# Context: i386/amd64/... and linux/freebsd/windows
context.update(arch='i386', os='linux')

####################################
#            Settings              #
####################################
# Set the context level to debug:
DEBUG = False
# Set if recv should automatically print
PRINTER = True
# Std timeout for the connection
TIMEOUT = 2
# Std print color. None means no extra color
STD_COL = None

####################################
#             Colors               #
####################################
class col:
    BLACK = '30'
    RED = '31'
    GREEN = '32'
    BROWN = '33'
    YELLOW = '33'
    BLUE = '34'
    MAGENTA = '35'
    CYAN = '36'
    WHITE = '37'
    CLEAR = '0'

    UNDERLINE = '4'
    BOLD = '1'

    ESCAPE_START = '\033['
    ESCAPE_END = 'm'

####################################
#          print methods           #
####################################
"""method to print a string more pretty"""
def prettyprint(s, color=STD_COL):
    if color == None:
        print s
    else:
        # TODO differentiate between printable and "hex"?
        coloring = col.ESCAPE_START + color + col.ESCAPE_END
        clear = col.ESCAPE_START + col.CLEAR + col.ESCAPE_END
        print  coloring + s + clear

def print_good(s):
    prettyprint(s, color=col.GREEN)

def print_bad(s):
    prettyprint(s, color=col.RED)

def print_info(s):
    prettyprint(s, color=col.YELLOW)

def print_bold(s):
    prettyprint(s, color=col.BOLD)

def print_underline(s):
    prettyprint(s, color=col.UNDERLINE)

####################################
#       convenience wrappers       #
####################################

def send():
    r.send()

"""send with a newline at the end"""
def sendline(s):
    r.sendline(s)

"""recvuntil then send"""
def sendafter(delim, data, shallprint=PRINTER, color=STD_COL):
    tmp = r.sendafter(delim, data)
    if shallprint:
        prettyprint(tmp, color)
    return tmp

"""recvuntil then sendline"""
def sendlineafter(delim, data, shallprint=PRINTER, color=STD_COL):
    tmp = r.sendlineafter(delim, data)
    if shallprint:
        prettyprint(tmp, color)
    return tmp

"""sendline and then recvuntil"""
def sendlinethen(delim, data, shallprint=PRINTER, color=STD_COL):
    tmp = r.sendlinethen(delim, data)
    if shallprint:
        prettyprint(tmp, color)
    return tmp

"""send and then recvuntil"""
def sendthen(delim, data, shallprint=PRINTER, color=STD_COL):
    tmp = r.sendthen(delim, data)
    if shallprint:
        prettyprint(tmp, color)
    return tmp

def recv(shallprint=PRINTER, color=STD_COL):
    tmp = r.recv()
    if shallprint:
        prettyprint(tmp, color)
    return tmp

"""recv until a newline is found"""
def recvline(shallprint=PRINTER, color=STD_COL):
    tmp = r.recvline()
    if shallprint:
        prettyprint(tmp, color)
    return tmp

"""recv until s appeared. drop s if drop=true"""
def recvuntil(s, shallprint=PRINTER, drop=False, color=STD_COL):
    tmp = r.recvuntil(s,drop)
    if shallprint:
        prettyprint(tmp, color)
    return tmp

"""recv n bytes"""
def recvn(n, shallprint=PRINTER, color=STD_COL):
    tmp = r.recvn(n)
    if shallprint:
        prettyprint(tmp, color)
    return tmp

"""recv until regex is found"""
def recvregex(r, shallprint=PRINTER, exact=False, color=STD_COL):
    tmp = r.recvregex(r, exact)
    if shallprint:
        prettyprint(tmp, color)
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
pause() # requires user input to start (e.g. waiting for server etc)
pwn()


# When there is a shell
# r.interactive()