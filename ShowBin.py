# -*- coding: UTF-8 -*-

import sys,os


# Syntax: python -u ShowBin.py File1 addr length
# => output differences

def show0xXX(lst):
    for _ch in lst:
        print(hex(_ch)+",", end="")
    print("")

def showXX(lst, wrap=16):
    _len = 0
    for _ch in lst:
        _len += 1
        if _len%8 == 0 and _len%16 != 0:
            # print("{0:x} - ".format(_ch), end="")
            print("%02X - " % _ch, end="")
        else:
            # print("{0:x} ".format(_ch), end="")
            print("%02X " % _ch, end="")
        if _len%16 == 0:
            print("")
    print("")

if __name__ == '__main__':
    fBin = open(sys.argv[1], "rb")
    _tmp = sys.argv[2]
    Addr = int(_tmp,16)
    _tmp = sys.argv[3]
    Length = int(_tmp,16)
    fBin.seek(0,2) # position the end of file
    Size = fBin.tell()
    fBin.seek(Addr,0) # position to start of file

    if Length > (Size-Addr):
        Length = Size-Addr
    print("%s (addr:%d, length:%d, size:%d) loading..." % (sys.argv[1], Addr, Length, Size))

    tmp = list(fBin.read(Length))

    # show0xXX(tmp)
    showXX(tmp)

    fBin.close()
    print("\n------------ exit! ------------", '\n')
