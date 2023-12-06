#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def trebuchet_partTwo(file):
    """
    Trebuchet enigma part two

    Args :
    file -- the input file
    
    Return :
    count -- the calibration value
    """
    f = open(file, "r")
    line=f.readline()
    count=0
    while (line != ''):
        tmp=''
        i=0
        j=1
        line=line.replace('\n','') # remove the line break at the end of the line
        line=replaceLettersByDigit(line)

        while (i<len(line)):
            if (checkIfIsInteger(line[i])):
                tmp+=line[i]
                i=len(line)
            else:
                i+=1

        while (j<len(line)+1):
            if (checkIfIsInteger(line[-j])):
                tmp+=line[-j]
                j=len(line)+1
            else:
                j+=1
        count+=int(tmp)
        line=f.readline()
    f.close()
    return count

def checkIfIsInteger(char):
    """
    Check if a string character can be convert to integer

    Args :
    char -- a string character
    
    Return :
    boolean -- True if is a digit, False otherwise
    """
    try:
        int(char)
        return True
    except ValueError :
        return False

def replaceLettersByDigit(line):
    """
    Replace all number letters by their digit

    Example : eightwothree should become 823 and not 8wo3

    Args :
    line -- a string

    Return : 
    newLine -- the line with letter replaced by digits
    """
    numbers={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    i=0
    j=0
    newLine=''
    while (i<len(line)+1):
        isDigit = checkIfDigitInString(line[j:i])
        if (isDigit != False):
            partLine = line[j:i].replace(isDigit,numbers[isDigit])
            newLine+=partLine
            j=i-1 # careful, you need to take the previous one to allow the possibility of overlapping numbers like eighttwo
        if (i==len(line)): # add even if its the end of the line
            newLine+=line[j:i]
            return newLine
        i+=1
    return newLine

def checkIfDigitInString(string):
    """
    Check if a digit is hidden in string

    Args : 
    string - a string 

    Return :
    number - return the digit in string format if is inside, False otherwise
    """
    numbers={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    for number in numbers :
        if number in string :
            return number
    return False

def main():
    print('# Day 1 - part 2')
    print('----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(trebuchet_partTwo(arg1)))

if __name__=="__main__":
    main()

