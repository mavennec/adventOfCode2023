#!/usr/bin/env python3 
# author : Mael Avennec

import sys
import math

def hauntedWasteland_partTwo(file):
    """
    Haunted Wasteland enigma part two

    Args :
    file (str) -- the input file path
    
    Return :
    steps (int) -- the number of steps to reach all xxZ
    """
    f = open(file, "r")
    nodes={}
    startNodes=[]
    allSteps=[]
    
    # Read the first line (instructions)
    line=f.readline()
    line=line.replace('\n','')
    instructions=line

    line=f.readline() # Continue to read the lines
    while (line != '') : 
        if(line[0] != '\n') :
            line=line.replace('\n','')

            # Parse input
            nodeTitle=line.split('=')[0].split(' ')[0]
            tmp=line.split('=')[1:][0][1:][1:-1]
            tmp=tmp.split(',')
            navigation=(tmp[0],tmp[1][1:])
            # Associate node title and his navigation infos in a map
            nodes[nodeTitle]=navigation

            # If the node title finish with an A, add it in list of start nodes
            if(nodeTitle[-1:]=='A'):
                startNodes.append(nodeTitle)
        
        line = f.readline()

    for startNode in startNodes : 
        steps=calculateStepsForANode(startNode, instructions, nodes)
        allSteps.append(steps)
    f.close()

    steps=math.lcm(*allSteps)
    
    return steps

def calculateStepsForANode(startNode, instructions, nodes):
    """
    Calculate the number of steps to reach xxZ node for a starting node

    Args :
    startNode (str)     -- the starting node
    instructions (list) -- list of instructions (L or R)
    nodes (dict)        -- the map of all nodes with their directions

    Return : 
    steps (int) -- the number of steps
    """
    steps=0
    i=0
    nextNode=startNode
    while (nextNode[-1] != 'Z') :
        
        # If end of instructions, restart from the first one
        if(i==len(instructions)):
            i=0
  
        direction=instructions[i]
        if(direction=='L'):
            nav=nodes[nextNode][0]
        else :
            nav=nodes[nextNode][1]
        nextNode=nav

        steps+=1
        i+=1
    return steps
    

def main():
    arg1 = sys.argv[1]
    print('# Day 8 - part 2')
    print('----------------')
    print('Result => {}'.format(hauntedWasteland_partTwo(arg1)))

if __name__=="__main__":
    main()

