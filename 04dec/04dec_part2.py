#!/usr/bin/env python3 
# author : Mael Avennec

import sys

from datetime import datetime

def scratchcards_partTwo(file):
    """
    Scratchcards enigma part one

    Args :
    file -- the input file
    
    Return :
    totalCards -- the sum of cards
    """
    f = open(file, "r")
    line=f.readline()
    allCardsCopy={}
    cardWinningNumbers={}

    while (line != '') : 
        line=line.replace('\n','')

        card = line.split(':')
        cardNumber=card[0].split(' ')[-1]
        if cardNumber in allCardsCopy.keys():
            allCardsCopy[cardNumber]+=1
        else :
            allCardsCopy[cardNumber]=1

        numbers = card[1].split('|')
        gameNumbers = numbers[0].split(' ')
        remove_items(gameNumbers,'')
        winningNumbers = numbers[1].split(' ')
        remove_items(winningNumbers,'')

        j=0
        while j<allCardsCopy[cardNumber]:

            # Calculate the numbers of winning numbers
            if (cardNumber not in cardWinningNumbers.keys()):
                incrWinningNumbers=0
                for gameNumber in gameNumbers : 
                    if gameNumber in winningNumbers :
                        incrWinningNumbers+=1
                cardWinningNumbers[cardNumber]=incrWinningNumbers
            
            i=1
            while i<=cardWinningNumbers[cardNumber] : 
                if str(int(cardNumber)+i) in allCardsCopy.keys():
                    allCardsCopy[str(int(cardNumber)+i)]+=1
                else :
                    allCardsCopy[str(int(cardNumber)+i)]=1
                i+=1        
            j+=1
        line = f.readline()
    f.close()
    totalCards=sum(allCardsCopy.values())
    return totalCards


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
    print('# Day 4 - part 2')
    print('----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(scratchcards_partTwo(arg1)))

if __name__=="__main__":
    main()

