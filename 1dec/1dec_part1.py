#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def trebuchet_partOne(file):
    """
    Trebuchet enigma part one

    Args :
    file -- the input file
    
    Return :
    count -- the calibration value
    """
    f = open(file, "r")
    line=f.readline()
    count=0
    while (line != ''):
        tmp=''
        i=0
        j=1

        while (i<len(line)):
            if (checkIfIsInteger(line[i])):
                tmp+=line[i]
                i=len(line)
            else:
                i+=1

        while (j<len(line)+1):
            if (checkIfIsInteger(line[-j])):
                tmp+=line[-j]
                j=len(line)+1
            else:
                j+=1

        count+=int(tmp)
        line=f.readline()
    f.close()
    return count

def checkIfIsInteger(char):
    """
    Check if a string character can be convert to integer

    Args :
    char -- a string character
    
    Return :
    boolean -- True if is a digit, False otherwise
    """
    try:
        int(char)
        return True
    except ValueError :
        return False


def main():
    print('# Day 1 - part 1')
    print('----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(trebuchet_partOne(arg1)))

if __name__=="__main__":
    main()

