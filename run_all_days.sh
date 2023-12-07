#!/bin/bash

challenge_days=(
    ""
    Trebuchet
    "Cube conundrum"
    "Gear ratios"
    Scratchcards
    "If You Give A Seed A Fertilize"
    "Wait For It"
    "Camel Cards"
)

for day in {1..25}
do
    FOLDER=$day
    FOLDER+="dec"
    if [[ -d "$FOLDER" ]]; then 
        INPUT="$FOLDER"
        INPUT+="_input"
        PART1=$FOLDER
        PART1+="_part1"
        PART2=$FOLDER
        PART2+="_part2"

        
        top="############"
        bottom="############"
        for (( i=0; i<${#challenge_days[day]}; i++ )); do
            top+="#"
            bottom+="#"
        done
        
        name="# DAY $day : ${challenge_days[day]} #"
        echo $top
        echo $name
        echo $bottom
    
        echo ""
        python3 $FOLDER/$PART1.py $FOLDER/inputs/$INPUT.txt
        echo ""
        python3 $FOLDER/$PART2.py $FOLDER/inputs/$INPUT.txt
        echo ""
        echo ""
    fi
done