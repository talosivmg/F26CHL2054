import sys                                  #Import sys module
temperatureMode = sys.argv [1]              #Assign sys argument 1 to variable

with open ("challenge.data", "r") as rawFile:   #Opens and reads file. 
    contents = rawFile.read().strip()           #Reads contents, strips characters, assigns to variable. 
    contentsValue = float(contents)             #Converts contents to decimal. 

print (contents)
print (temperatureMode)







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