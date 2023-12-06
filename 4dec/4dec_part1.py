#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def scratchcards_partOne(file):
    """
    Scratchcards enigma part one

    Args :
    file -- the input file
    
    Return :
    totalPoints -- the sum of points
    """
    f = open(file, "r")
    line=f.readline()
    gamePoints=0
    totalPoints=0
    while (line != '') : 
        line=line.replace('\n','')
        
        gamePoints=0
        card = line.split(':')
        numbers = card[1].split('|')
        gameNumbers = numbers[0].split(' ')
        remove_items(gameNumbers,'')
        winningNumbers = numbers[1].split(' ')
        remove_items(winningNumbers,'')

        incrWinningNumbers=0
        for gameNumber in gameNumbers : 
            if gameNumber in winningNumbers :
                incrWinningNumbers+=1
            
        if(incrWinningNumbers>0):
            gamePoints=2**(incrWinningNumbers-1)
        totalPoints+=gamePoints

        line = f.readline()
    f.close()
    return totalPoints


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
    print('# Day 4 - part 1')
    print('----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(scratchcards_partOne(arg1)))

if __name__=="__main__":
    main()

