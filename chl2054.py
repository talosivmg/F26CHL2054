import sys                                  #Import sys module
temperatureMode = sys.argv [1]              #Assign sys argument 1 to variable

with open ("challenge.data", "r") as rawFile:   #Opens and reads file. 
    contents = rawFile.read().strip()           #Reads contents, strips characters, assigns to variable. 
    contentsValue = float(contents)             #Converts contents to decimal. 

def FtoC(contentsValue):                        #Function if parameter is FtoC. 
    tempCalculation = ( contentsValue -32 ) * 5 / 9
    return tempCalculation

def CtoF(contentsValue):                        #Function if parameter is CtoF. 
    tempCalculation = (contentsValue * 9 / 5 ) + 32
    return tempCalculation


if temperatureMode == "FtoC":
    result = FtoC(contentsValue)
elif temperatureMode == "CtoF":
    result = CtoF(contentsValue)


with open ("challenge.out", "w") as outputFile:
    outputFile.write(str(result))



"""
CLI py clg2054.py argument
- argument will be FotC or CtoF

import sys

assign argument 1 to challengeDataValue

open challenge.data read

define function FtoC
define function CtoF

if mode
    is FtoC : then calculate
    else if CtoF then calculate

write to challenge.out



"""