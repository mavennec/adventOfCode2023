#!/usr/bin/env python3 
# author : Mael Avennec

import sys
import math

def waitForIt_partOne(file):
    """
    Wait For It enigma part one

    Args :
    file (str) -- the input file path
    
    Return :
    numberOfWays (int) -- the number of ways multiplied together
    """
    f = open(file, "r")
    line=f.readline()
    times=[]
    distances=[]
    numberOfWays=[]

    # Read file input
    while (line != '') : 
        line=line.replace('\n','')
        currentType=line.split(':')[0]
        if(currentType == 'Time'):
            times = remove_items(line.split(':')[1].split(' '),'')
        elif(currentType == 'Distance'):
            distances = remove_items(line.split(':')[1].split(' '),'')
        line = f.readline()

    # Process
    i=0
    while i < len(times):
        time=int(times[i])
        distance=int(distances[i])
        numberOfWays.append(0)
        x=0
        pace=0
        while x < time :
            
            time_remaining=time-x
            distance_millimeters=pace * time_remaining
            if (distance_millimeters) > distance :
                numberOfWays[i]+=1
            x+=1
            pace+=1
        i+=1
    
    f.close()
    return math.prod(numberOfWays)

def remove_items(test_list, item): 
    """
    Remove all occurences of items in list

    Args :
    test_list (list)    -- a list 
    item (str)          -- an item

    Return : 
    test_lest (list) -- return the list without items
    """
    while item in test_list :
        test_list.remove(item)
    return test_list

def main():
    print('# Day 6 - part 1')
    print('----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(waitForIt_partOne(arg1)))

if __name__=="__main__":
    main()

