#!/usr/bin/env python3 
# template_Xdec_partY.py
# author : Mael Avennec

import sys

def ZZZZ_partOne(file):
    """
    ZZZZ enigma part one

    Args :
    file -- the input file
    
    Return :
    count -- the sum of ids
    """
    f = open(file, "r")
    line=f.readline()
    while (line != '') : 
        line = f.readline()
    
    f.close()
    return count

def main():
    arg1 = sys.argv[1]
    print(ZZZZ_partOne(arg1))

if __name__=="__main__":
    main()

