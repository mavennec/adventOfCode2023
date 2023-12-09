#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def hauntedWasteland_partOne(file):
    """
    Haunted Wasteland enigma part one

    Args :
    file (str) -- the input file path
    
    Return :
    steps (int) -- the number of steps to reach ZZZ
    """
    f = open(file, "r")
    nodes={}
    steps=0
    
    # Read the first line (instructions)
    line=f.readline()
    line=line.replace('\n','')
    instructions=line
    line=f.readline()

    while (line != '') : 
        if(line[0] != '\n') :
            line=line.replace('\n','')
            nodeTitle=line.split('=')[0].split(' ')[0]
            tmp=line.split('=')[1:][0][1:][1:-1]
            tmp=tmp.split(',')
            navigation=(tmp[0],tmp[1][1:])
            nodes[nodeTitle]=navigation

        line = f.readline()
    f.close()

    # Process
    i=0
    nav='AAA'
    while nav!='ZZZ' :
        if(i==len(instructions)):
            i=0
        direction=instructions[i]
        if(direction=='L'):
            nav=nodes[nav][0]
        else :
            nav=nodes[nav][1]
        steps+=1
        i+=1
    
    return steps

def main():
    arg1 = sys.argv[1]
    print('# Day 8 - part 1')
    print('----------------')
    print('Result => {}'.format(hauntedWasteland_partOne(arg1)))

if __name__=="__main__":
    main()

