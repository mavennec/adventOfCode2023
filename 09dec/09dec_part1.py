#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def mirageMaintenance_partOne(file):
    """
    Mirage Maintenance enigma part one

    Args :
    file (str) -- the input file path
    
    Return :
    sumValues (int) -- the sum of the extrapolated values
    """
    f = open(file, "r")
    line=f.readline()
    sumValues=0
    report=[]

    while (line != '') : 
        line=line.replace('\n','')
        
        sequence=[int(x) for x in line.split(' ')]
        history=[]
        history.append(sequence)

        # Check each steps 
        while (sum(sequence) != 0) :

            # Check each value of the step to add the differences
            differences=[]
            i=0
            while i < len(sequence)-1:
                value = sequence[i]
                nextValue = sequence[i+1]
                differences.append(nextValue-value)
                
                i+=1
            sequence=differences
            history.append(sequence)        

        # When the read of each step is read, find the prediction value
        j=0
        history.reverse()
        val=0
        while j < len(history)-1 : 
            val+=history[j+1][-1]
            j+=1
        report.append(val) # Add the prediction value to the report list
        
        line = f.readline()
    
    sumValues=sum(report)
    f.close()
    return sumValues

def main():
    arg1 = sys.argv[1]
    print('# Day 9 - part 1')
    print('----------------')
    print('Result => {}'.format(mirageMaintenance_partOne(arg1)))

if __name__=="__main__":
    main()

