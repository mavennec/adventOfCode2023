#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def cubeConundrum_partOne(file):
    """
    Cube conundrum enigma part one

    Args :
    file -- the input file
    
    Return :
    count -- the sum of ids
    """
    bag = {'red':12, 'green':13, 'blue':14}
    f = open(file, "r")
    line=f.readline()
    gamePossible=[]
    while (line != '') : 
        line=line.replace('\n','')
        isGamePossible=True
        game = line.split(':')
        gameNumber=game[0].split('Game ')[1]
        sets = game[1].split(';')
        for currentSet in sets :
            cubes = currentSet.split(',')
            for cube in cubes :
                currentCube = cube[1:].split(' ')
                number=int(currentCube[0])
                color=currentCube[1]
                if(number > bag[color]):
                    isGamePossible=False
                    break
        if(isGamePossible):
            gamePossible.append(int(gameNumber))
                
        line = f.readline()
    f.close()
    count = sum(gamePossible)
    return count

def main():
    print('# Day 2 - part 1')
    print('----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(cubeConundrum_partOne(arg1)))

if __name__=="__main__":
    main()

