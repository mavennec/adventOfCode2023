#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def giveASeedAFertilisze_partTwo(file):
    """
    If You Give A Seed A Fertilizer enigma part one

    Args :
    file (str) -- the input file path
    
    Return :
    seeds (int) -- the lowest location for inital seeds
    """
    f = open(file, "r")
    line=f.readline()
    line=line.replace('\n','')
    seeds_start=remove_items(line.split(':')[1].split(' '),'')
    seeds=[]
    seeds_reboot=[]
    
    index=0
    while index < len(seeds_start):
        if ((index % 2) == 0) :
            start_range = int(seeds_start[index])
            length_range = int(seeds_start[index+1])
            range_incr=0
            while range_incr < length_range :
                seeds.append(start_range+range_incr)
                seeds_reboot.append(True)
                range_incr+=1
        index+=1

    line=f.readline()

    while (line != '') : 
        line=line.replace('\n','')

        current_line=line.split(' ')
        if(isRangeLine(current_line)):
    
            destination=int(current_line[0])
            source=int(current_line[1])
            length=int(current_line[2])

            i=0
            while i<len(seeds) : 
                seed=int(seeds[i])
                if(seed>=source and (source + length >= seed) and seeds_reboot[i]==True):
                    seeds[i]=seed+destination-source
                    seeds_reboot[i]=False
                i+=1
        else:
            j=0
            while j < len(seeds) : 
                seeds_reboot[j]=True
                j+=1

        line=f.readline()
    return min(seeds)


def isRangeLine(current_line):
    """
    Check if the current line is a range line (line with 3 numbers)

    Args :
    current_line (str) -- the current line

    Return :
    (boolean) -- True if it is a range line, False otherwise
    """
    try :
        int(current_line[0])
        return True
    except ValueError :
        return False

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
    print('# Day 5 - part 2')
    print('----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format('TODO'))
    #print(giveASeedAFertilisze_partTwo(arg1))

if __name__=="__main__":
    main()

