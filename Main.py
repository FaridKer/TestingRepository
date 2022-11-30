#Is it okay to make .py at the end of file?
#Btw i am using Sublime text first time. I used Wing IDLE before and not familiar with Sublime. I do not even understand what is the difference between Sublime and common Notebook

#so i want to try to redone excersise from stepik. The original code was:
#from functools import *
#
#data = [['Tokyo', 35676000, 'primary'],
#        ['New York', 19354922, 'nan'],
#        ['Mexico City', 19028000, 'primary'],
#        ['Mumbai', 18978000, 'admin'],
#        ['Sao Paulo', 18845000, 'admin'],
#        ['Delhi', 15926000, 'admin'],
#        ['Shanghai', 14987000, 'admin'],
#        ['Kolkata', 14787000, 'admin'],
#        ['Los Angeles', 12815475, 'nan'],
#        ['Dhaka', 12797394, 'primary'],
#        ['Buenos Aires', 12795000, 'primary'],
#        ['Karachi', 12130000, 'admin'],
#        ['Cairo', 11893000, 'primary'],
#        ['Rio de Janeiro', 11748000, 'admin'],
#        ['Osaka', 11294000, 'admin'],
#        ['Beijing', 11106000, 'primary'],
#        ['Manila', 11100000, 'primary'],
#        ['Moscow', 10452000, 'primary'],
#        ['Istanbul', 10061000, 'admin'],
#        ['Paris', 9904000, 'primary']]
#
#new_data = list(filter(lambda city: city if city[2] == 'primary' else city == [], data))
#new_data2 = list(filter(lambda city: city if city[1] > 10000000 else city == [], new_data))
#
#print('Cities:', end = ' ')
#cities = []
#for i in sorted(new_data2):
#    cities.append(i[0])
#
#print(*sorted(cities), sep = ', ')

#The task of this excersise - to create new list of cities, which are 'primary' and have population bigger than 10 000 000 people
#I want to try to split data between several files to get how files working with each other. Lets try it out:
from functools import *
data = [['Tokyo', 35676000, 'primary'],
	['New York', 19354922, 'nan'],
	['Mexico City', 19028000, 'primary'],
	['Mumbai', 18978000, 'admin'],
	['Sao Paulo', 18845000, 'admin'],
	['Delhi', 15926000, 'admin'],
	['Shanghai', 14987000, 'admin'],
	['Kolkata', 14787000, 'admin'],
	['Los Angeles', 12815475, 'nan'],
	['Dhaka', 12797394, 'primary'],
	['Buenos Aires', 12795000, 'primary'],
	['Karachi', 12130000, 'admin'],
	['Cairo', 11893000, 'primary'],
	['Rio de Janeiro', 11748000, 'admin'],
	['Osaka', 11294000, 'admin'],
	['Beijing', 11106000, 'primary'],
	['Manila', 11100000, 'primary'],
	['Moscow', 10452000, 'primary'],
	['Istanbul', 10061000, 'admin'],
	['Paris', 9904000, 'primary']]

with open('inputdata.txt', 'w', encoding='utf-8') as file:
    for i in data:
        print(*i, sep = ', ', end = '\n', file=file)                                #i literally want to save this data to a file like a normal text

with open('taskresult.txt', 'w', encoding='utf-8') as result, open('inputdata.txt', 'r', encoding='utf-8') as inputdata:
    listofcities = inputdata.readlines()                                            #trying to take data from file and to make it look like before saving to file
    listofcities = [i.rstrip('\n') for i in listofcities]                           #first of all i need to get rid of '\n'
    
    new_list = []                                                                   #i still did not get why i cant change lists inside of list, probably it is not allowed, 
                                                                                    #so i create a new list to append every inner list of listofcities
    for i in listofcities:
        temp = i.split(', ')                                                        #some cities have several words, so i have to split it in that way to not fuck it up
        new_list.append(temp)
    
    new_list = list(filter(lambda city: city if city[2] == 'primary' else city == [], new_list))    #first of all i filter that list, removing every city, that do not have 'primary' 
                                                                                                    #word inside of list
    new_list = list(filter(lambda city: city if int(city[1]) > 10000000 else city == [], new_list)) #second of all i filter list, removing every city, that do not have enough
                                                                                                    #population. I have to convert population to int, because it has str type    
    
    print('Cities:', end = ' ', file=result)
    cities = []
    for i in sorted(new_list):
        cities.append(i[0])   
    print(*sorted(cities), sep = ', ', file=result)                                 #task has one of objectives - recombine cities in alphabetical order, 
                                                                                    #so i created a list of cities, and after that i sorted them
    print(file=result)
    print('P.S. Wow, i actually did it. I am not complete useless :)', file=result) #well. At least i see that i understand what i am doing...i hope