#!/usr/bin/python
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
#line of hyphens same length as string
print("This is a line of hyphens the same length as my Belgium string:")
print("-" * len(Belgium))
#Need to investigate sep... print(Belgium, sep=":")
print("This is my string with comma separators replaced by colons using the str.replace('old', 'new') method:")
print(Belgium.replace(",", ":"))
#Sliced the string to extract figures - feels like a messy method! Recast as integers.
#NB strings indexed from 0 and str[start:end+1]
#Could have done this without creating variable but code seems more readable with (see below)
PopBelgium = int(Belgium[8:16])
PopBrussels = int(Belgium[26:32])
print("The Population of Belgium plus the population of Brussels is: " + str(PopBelgium + PopBrussels))
#print("The Population of Belgium plus the population of Brussels is: " + str(int(Belgium[8:16]) + int(Belgium[26:32])))


