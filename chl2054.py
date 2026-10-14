import sys                                  #Import sys module
temperatureMode = sys.argv [1]              #Assign sys argument 1 to variable

with open ("challenge.data", "r") as rawFile:   #Opens and reads file. 
    contents = rawFile.read().strip()           #Reads contents, strips characters, assigns to variable. 
    contentsValue = float(contents)             #Converts contents to decimal. 

def modeCalculation(inputMode):                         #Defines a function with a parameter `input mode`. 
    if inputMode == "FtoC":                             #If compares to a string. 
        tempCalculation = ( contentsValue -32 ) * 5 / 9 #Temp calculation 
    elif inputMode == "CtoF":                           #`else if` compares the string. 
        tempCalculation = ( contentsValue * 9 / 5) +32  #Temp calculation 
    print (tempCalculation)                             #Check print temp calculation. 
    print (temperatureMode)                             #Check print temperature mode. 
    print (contents)                                    #Check print contents. 
    return tempCalculation                              #Return capture calculation. 


result = modeCalculation(temperatureMode)               #Calls function, assigns to result 


print (f"mode: , {temperatureMode}")                     #Prints temperature mode. 
print (f"file contents: , {contents}")                   #Prints contents. 
print (f"function result: , {result}")                   #Prints results from function. 







"""
CLI py clg2054.py argument
- argument will be FotC or CtoF

import sys

assign argument 1 to challengeDataValue

open challenge.data read

define function mode FtoC or CtoF

if mode
    is FtoC : then calculate
    else if CtoF then calculate

write to challenge.out



"""