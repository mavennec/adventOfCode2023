#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def cubeConundrum_partTwo(file):
    """
    Cube conundrum enigma part two

    Args :
    file -- the input file
    
    Return :
    count -- the sum of powers
    """
    f = open(file, "r")
    line=f.readline()
    gamePowers=[]
    while (line != '') : 
        line=line.replace('\n','')
        maximum={'red':0,'green':0,'blue':0}
        game = line.split(':')
        gameNumber=game[0].split('Game ')[1]
        sets = game[1].split(';')
        for currentSet in sets :
            cubes = currentSet.split(',')
            for cube in cubes :
                currentCube = cube[1:].split(' ')
                number=int(currentCube[0])
                color=currentCube[1]
                if(maximum[color]<number):
                    maximum[color]=number

        power=maximum['red']*maximum['green']*maximum['blue']
        gamePowers.append(power)

        line = f.readline()
    f.close()
    count = sum(gamePowers)
    return count

def main():
    print('# Day 2 - part 2')
    print('----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(cubeConundrum_partTwo(arg1)))

if __name__=="__main__":
    main()

