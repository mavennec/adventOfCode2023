#!/usr/bin/env python3 
# author : Mael Avennec

import sys

def giveASeedAFertilisze_partOne(file):
    """
    If You Give A Seed A Fertilizer enigma part one

    Args :
    file (str) -- the input file path
    
    Return :
    seeds (int) -- the lowest location for inital seeds
    """
    f = open(file, "r")
    line=f.readline()
    line=line.replace('\n','')
    seeds=remove_items(line.split(':')[1].split(' '),'')
    seeds_category_to_check=[]

    # Create a list with the same length of seeds list with boolean value (to know if it is already checked for the category)
    for seed in seeds:
        seeds_category_to_check.append(True)
    line=f.readline()

    while (line != '') : 
        line=line.replace('\n','')

        current_line=line.split(' ')
        if(isRangeLine(current_line)):
    
            destination=int(current_line[0])
            source=int(current_line[1])
            length=int(current_line[2])

            i=0
            while i<len(seeds) : 
                seed=int(seeds[i])
                if(seed>=source and (source + length >= seed) and seeds_category_to_check[i]==True):
                    seeds[i]=seed+destination-source
                    # The seed is checked in the category, set it to False
                    seeds_category_to_check[i]=False
                i+=1
        elif(line==''):
            # It's a break line, set all seeds_category_to_check to True, because it will start a new category
            j=0
            while j < len(seeds) : 
                seeds_category_to_check[j]=True
                j+=1

        line=f.readline()
    return min(seeds)


def isRangeLine(current_line):
    """
    Check if the current line is a range line (line with 3 numbers)

    Args :
    current_line (str) -- the current line

    Return :
    (boolean) -- True if it is a range line, False otherwise
    """
    try :
        int(current_line[0])
        return True
    except ValueError :
        return False

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

# def giveASeedAFertilisze_partOneBis(file):
#     """
#     If You Give A Seed A Fertilizer enigma part one

#     Args :
#     file (str) -- the input file path
    
#     Return :
#     locations (int) -- the lowest location for inital seeds
#     """
#     f = open(file, "r")
#     line=f.readline()
#     line=line.replace('\n','')
#     seeds_start=remove_items(line.split(':')[1].split(' '),'')
#     seeds=[]
#     index=0
#     while index < len(seeds_start):
#         if ((index % 2) == 0) :
#             start_range = int(seeds_start[index])
#             length_range = int(seeds_start[index+1])
#             range_incr=0
#             while range_incr < length_range :
#                 seeds.append(start_range+range_incr)
#                 range_incr+=1
#         index+=1
#     categories=[]
#     locations=[]

#     while (line != '') : 
#         line=line.replace('\n','')

#         # seed-to-soil
#         if(line=='seed-to-soil map:'):
#             seed_to_soil={}
#             seed_to_soil=range_to_map(seed_to_soil,f)
#             categories.append(seed_to_soil)
#             # print('soil ===> '+str(dict(sorted(seed_to_soil.items()))))
#             print('SEED-TO-SOIL FINISHED')

#         # soil-to-fertilizer
#         if(line=='soil-to-fertilizer map:'):
#             soil_to_fertilizer={}
#             soil_to_fertilizer=range_to_map(soil_to_fertilizer,f)
#             categories.append(soil_to_fertilizer)
#             # print('fertilizer ===> '+str(dict(sorted(soil_to_fertilizer.items()))))
#             print('SOIL-TO-FERTILIZER FINISHED')

#         # fertilizer-to-water
#         if(line=='fertilizer-to-water map:'):
#             fertilizer_to_water={}
#             fertilizer_to_water=range_to_map(fertilizer_to_water,f)
#             categories.append(fertilizer_to_water)
#             # print('water ===> '+str(dict(sorted(fertilizer_to_water.items()))))
#             print('FERTILIZER-TO-WATER FINISHED')

#         # water-to-light
#         if(line=='water-to-light map:'):
#             water_to_light={}
#             water_to_light=range_to_map(water_to_light,f)
#             categories.append(water_to_light)
#             # print('light ===> '+str(dict(sorted(water_to_light.items()))))
#             print('WATER-TO-LIGHT FINISHED')
            

#         # light-to-temparature
#         if(line=='light-to-temperature map:'):
#             light_to_temperature={}
#             light_to_temperature=range_to_map(light_to_temperature,f)  
#             categories.append(light_to_temperature)
#             # print('temperature ===> '+str(dict(sorted(light_to_temperature.items()))))
#             print('LIGHT-TO-TEMPERATURE FINISHED')

#         # temperature-to-humidity
#         if(line=='temperature-to-humidity map:'):
#             temperature_to_humidity={}
#             temperature_to_humidity=range_to_map(temperature_to_humidity,f)
#             categories.append(temperature_to_humidity)
#             # print('humidity ===> '+str(dict(sorted(temperature_to_humidity.items()))))
#             print('TEMPERATURE-TO-HUMIDITY FINISHED')

#         # humidity-to-location
#         if(line=='humidity-to-location map:'):
#             humidity_to_location={}
#             humidity_to_location=range_to_map(humidity_to_location,f)
#             categories.append(humidity_to_location)
#             # print('location ===> '+str(dict(sorted(humidity_to_location.items()))))
#             print('HUMIDITY-TO-LOCATION FINISHED')
            
#         line = f.readline()
    
#     print('READ FILE FINISHED')

#     for seed in seeds:
#         current_seed=int(seed)
#         print()
#         print('SEED : '+str(seed))
#         for category in categories : 
#             if(current_seed in category.keys()):
#                 print(str(current_seed)+' => '+str(category[current_seed]))
#                 current_seed=category[current_seed]
#             else:
#                 print(str(current_seed)+' => '+str(current_seed))
#                 current_seed=current_seed
#         locations.append(current_seed)

#     f.close()
#     return min(locations)

# def range_to_map(current_map,file):
#     """
#     Link the sources to destination for each map

#     Args : 
#     current_map (dict)  -- a dictionnary
#     file (file)         -- the file

#     Return :
#     current_map (dict) -- the dictionnary with all sources linked to destination
#     """
#     line = file.readline()
#     while(line != '\n' and line != '') : 
#         line=line.replace('\n','')
#         current_line=line.split(' ')

#         destination=current_line[0]
#         source=current_line[1]
#         length=current_line[2]
#         i=0
#         while i < int(length) :
#             current_map[int(source)+i]=int(destination)+i
#             i+=1

#         line=file.readline()
    
#     return current_map

def main():
    print('# Day 5 - part 1')
    print('----------------')
    arg1 = sys.argv[1]
    print('Result => {}'.format(giveASeedAFertilisze_partOne(arg1)))

if __name__=="__main__":
    main()

