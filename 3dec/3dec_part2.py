#!/usr/bin/env python3 
# author : Mael Avennec

import sys

boardTest = {(0, 0): '4', (1, 0): '6', (2, 0): '7', (3, 0): '.', (4, 0): '.', (5, 0): '1', (6, 0): '1', (7, 0): '4', (8, 0): '.', (9, 0): '.', (0, 1): '.', (1, 1): '.', (2, 1): '.', (3, 1): '*', (4, 1): '.', (5, 1): '.', (6, 1): '.', (7, 1): '.', (8, 1): '.', (9, 1): '.', (0, 2): '.', (1, 2): '.', (2, 2): '3', (3, 2): '5', (4, 2): '.', (5, 2): '.', (6, 2): '6', (7, 2): '3', (8, 2): '3', (9, 2): '.', (0, 3): '.', (1, 3): '.', (2, 3): '.', (3, 3): '.', (4, 3): '.', (5, 3): '.', (6, 3): '#', (7, 3): '.', (8, 3): '.', (9, 3): '.', (0, 4): '6', (1, 4): '1', (2, 4): '7', (3, 4): '*', (4, 4): '.', (5, 4): '.', (6, 4): '.', (7, 4): '.', (8, 4): '.', (9, 4): '.', (0, 5): '.', (1, 5): '.', (2, 5): '.', (3, 5): '.', (4, 5): '.', (5, 5): '+', (6, 5): '.', (7, 5): '5', (8, 5): '8', (9, 5): '.', (0, 6): '.', (1, 6): '.', (2, 6): '5', (3, 6): '9', (4, 6): '2', (5, 6): '.', (6, 6): '.', (7, 6): '.', (8, 6): '.', (9, 6): '.', (0, 7): '.', (1, 7): '.', (2, 7): '.', (3, 7): '.', (4, 7): '.', (5, 7): '.', (6, 7): '7', (7, 7): '5', (8, 7): '5', (9, 7): '.', (0, 8): '.', (1, 8): '.', (2, 8): '.', (3, 8): '$', (4, 8): '.', (5, 8): '*', (6, 8): '.', (7, 8): '.', (8, 8): '.', (9, 8): '.', (0, 9): '.', (1, 9): '6', (2, 9): '6', (3, 9): '4', (4, 9): '.', (5, 9): '5', (6, 9): '9', (7, 9): '8', (8, 9): '.', (9, 9): '.'}
numbersTest = {(0, 0): '467', (5, 0): '114', (2, 2): '35', (6, 2): '633', (0, 4): '617', (7, 5): '58', (2, 6): '592', (6, 7): '755', (1, 9): '664', (5, 9): '598'}

def gearRatios_partTwo(file):
    """
    Gear ratios enigma part one

    Args :
    file (str) -- the input file path
    
    Return :
    count (int) -- the sum of ratios
    """
    f = open(file, "r")
    line=f.readline()
    board={}
    numbers={}
    mapMultiply={}
    count=0
    y=0
    
    while (line != '') : 
        line=line.replace('\n','')

        # Add all coordinates of the line in board
        x=0
        while x < len(line) :
            coordinates = (x,y)
            board[coordinates]=line[x]
            x+=1

        # For each line, recover the numbers and save them in numbers list
        i=0
        while i < len(line) : 
            if checkIsDigit(line[i]):
                numbers[(i,y)]=line[i]
                j=1
                while(i+j < len(line) and checkIsDigit(line[i+j])):
                    numbers[(i,y)]+=line[i+j]
                    j+=1
                i+=j
            i+=1

        line = f.readline()
        y+=1
    f.close()

    # For each number found, check if symbol multiply is adjacent, if it is, add it to multiply symbol map with the number coordinate in list values
    for coordinates in numbers : 
        multiplyCoordinates = getCoordinatesIfNumberAdjacentToSymbolMultiply(coordinates, len(numbers[coordinates]), board, x, y)
        if multiplyCoordinates :
            if multiplyCoordinates in mapMultiply.keys():
                mapMultiply[multiplyCoordinates].append(coordinates)
            else :
                mapMultiply[multiplyCoordinates]=[coordinates]

    # For each multiply symbol, check if the list associated contains exactly 2 coordinates (that corresponding to two numbers adjacent)
    for multiply in mapMultiply.keys() :
        if len(mapMultiply[multiply])==2 :
            count+=(int(numbers[mapMultiply[multiply][0]])*int(numbers[mapMultiply[multiply][1]]))

    return count

def getCoordinatesIfNumberAdjacentToSymbolMultiply(numberCoordinates, numberLength, board, boardSizeX, boardSizeY):
    """
    Get the coordinates of the multiply symbol if is adjecent to the number

    Args : 
    numberCoordinates (tuple)   -- the coordinates of the first digit of the number
    numberLength (int)          -- the number length
    board (dict)                -- the board
    boardSizeX (int)            -- the maximum X size of the board
    boardSizeY (int)            -- the maximum Y size of the board

    Return : 
    (tuple/boolean) -- The tuple coordinates of the multiply symbol if is adjcent to the number, False otherwise
    """
    i=0
    while (i<numberLength) :
        newCoordinates=(numberCoordinates[0]+i,numberCoordinates[1])
        coordinates=getCoordinatesIfDigitAdjacentToSymbolMultiply(newCoordinates,board,boardSizeX,boardSizeY)
        if(coordinates):
            return coordinates
        i+=1
    return False

def getCoordinatesIfDigitAdjacentToSymbolMultiply(coordinates, board, boardSizeX, boardSizeY):
    """
    Get the coordinates of the multiply symbol if is adjecent to the digit

    Args :
    coordinates (tuple) -- the coordinates of the digit
    board (dict)        -- the board
    boardSizeX (int)    -- the maximum X size of the board
    boardSizeY (int)    -- the maximum Y size of the board

    Return :
    (tuple/boolean) -- The tuple coordinates of the multiply symbol if is adjcent to the digit, False otherwise
    """
    x=int(coordinates[0])
    y=int(coordinates[1])

    i=-1
    while i<=1:
        j=-1
        while j<=1:
            if(x+i>=0 and y+j>=0 and x+i<(boardSizeX) and y+j<(boardSizeY)) :
                if(checkIsSymbolMultiply(board[x+i,y+j])):
                    return (x+i,y+j)
            j+=1
        i+=1
    return False

def checkIsDigit(element):
    """
    Check if the element given can be convert to int

    Args :
    element (str) -- an element (symbol or digit)

    Return :
    (boolean) -- True if can be convert to integer, False otherwise
    """
    try :
        int(element)
        return True
    except ValueError :
        return False

def checkIsSymbolMultiply(element):
    """
    Check if the character 

    Args :
    element (str) -- a character

    Return :
    (boolean) -- False is a digit or a point '.', True otherwise
    """
    if (element=='*'):
        return True
    else : 
        return False

def main():
    print('# Day 3 - part 2')
    print('----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(gearRatios_partTwo(arg1)))

if __name__=="__main__":
    main()

