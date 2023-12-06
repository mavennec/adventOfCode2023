#!/usr/bin/env python3 
# Xdec_partY.py
# author : Mael Avennec

import sys

def ZZZZ_partOne(file):
    """
    ZZZZ enigma part one

    Args :
    file (str) -- the input file path
    
    Return :
    ??? (int) -- ???
    """
    f = open(file, "r")
    line=f.readline()
    while (line != '') : 
        line=line.replace('\n','')
        
        line = f.readline()
    f.close()
    return count

def main():
    arg1 = sys.argv[1]
    print('### Day X : ZZZZZ ###')
    print(ZZZZ_partOne(arg1))

if __name__=="__main__":
    main()

