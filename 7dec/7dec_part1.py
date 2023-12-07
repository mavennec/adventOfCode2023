#!/usr/bin/env python3 
# author : Mael Avennec

import sys
from enum import Enum

class Type(Enum):
    UNKNOWN=0
    HIGH=1
    ONE_PAIR=2
    TWO_PAIR=3
    BRELAN=4
    FULL=5
    SQUARE=6
    FIVE=7

class CamelCard:

    def __init__(self, hand, bid):
        self._cards={}
        self._cardValue={'2':1, '3':2, '4':3, '5':4 , '6':5, '7':6 , '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}
        self._hand=hand
        self._bid=int(bid)
        self._type=Type.UNKNOWN
        self.setCards()
        self.setType()

    def getHand(self):
        return self._hand
    
    def getType(self):
        return self._type
    
    def getBid(self):
        return self._bid

    def setType(self):
        cardOccurences=list(self._cards.values())
        # five
        if(5 in cardOccurences):
            self._type=Type.FIVE
        # carre
        elif(4 in cardOccurences):
            self._type=Type.SQUARE

        elif(3 in cardOccurences):
            # full 
            if(2 in cardOccurences):
                self._type=Type.FULL
            # brelan
            else:
                self._type=Type.BRELAN
        elif(2 in cardOccurences):
            # remove the first two value to check if another one exists
            cardOccurences.pop(cardOccurences.index(2))
            # double pair
            if(2 in cardOccurences):
                self._type=Type.TWO_PAIR
            # one pair
            else :
                self._type=Type.ONE_PAIR
        # high card
        else:
            self._type=Type.HIGH

    def setCards(self):
        for i in self._hand:
            if i in self._cards.keys():
                self._cards[i]+=1
            else :
                self._cards[i]=1 
    
    def isGreaterThan(self, otherHand):
        if self._type.value > otherHand.getType().value :
            return True
        elif self._type.value == otherHand.getType().value :
            otherHandCards = otherHand.getHand()
            i=0
            while i < len(self._hand) :
                if self._cardValue[self._hand[i]] > self._cardValue[otherHandCards[i]] :
                    return True
                elif self._cardValue[self._hand[i]] < self._cardValue[otherHandCards[i]] :
                    return False
                else : 
                    i+=1
        else :
            return False    

def camelCards_partOne(file):
    """
    Camel cards enigma part one

    Args :
    file (str) -- the input file path
    
    Return :
    totalWinnings (int) -- the total of winnings (sum of bid*rank)
    """
    f = open(file, "r")
    camelCardOrderedAsc=[]
    totalWinnings=0

    line=f.readline()
    while (line != '') : 
        line=line.replace('\n','')

        hand=line.split(' ')[0]
        bid=line.split(' ')[1]

        camelCard = CamelCard(hand,bid)
        if(len(camelCardOrderedAsc)==0) :
            camelCardOrderedAsc.append(camelCard)
        else : 
            i=0
            isAdded=False
            while (i<=len(camelCardOrderedAsc) and isAdded==False):
                if(i==len(camelCardOrderedAsc)):
                    # add at the end
                    camelCardOrderedAsc.append(camelCard)
                    isAdded=True
                elif(camelCard.isGreaterThan(camelCardOrderedAsc[i])) :
                    i+=1
                else :
                    # add before the camelCard who is greater  
                    camelCardOrderedAsc=camelCardOrderedAsc[0:i] + [camelCard] + camelCardOrderedAsc[i:]
                    isAdded=True
        
        line = f.readline()
        
    rankNb=0
    for camelCardOrdered in camelCardOrderedAsc : 
        rankNb+=1
        totalWinnings+=rankNb*camelCardOrdered.getBid()

    f.close()
    return totalWinnings

def main():
    arg1 = sys.argv[1]
    print('# Day 7 - part 1')
    print('----------------')
    print('Result => {}'.format(camelCards_partOne(arg1)))

if __name__=="__main__":
    main()

