from math import ceil
#problem 3-9 paint the room
areaRoom = 231 #ft
areaPerGallon = 115 #sq ft

#way I told you
gallonsNeeded = areaRoom // areaPerGallon #integer divide like gradeschoo
wallLeft = areaRoom % areaPerGallon #% or mod function gives divide remainder
if wallLeft > 0:
    gallonsNeeded = gallonsNeeded + 1
print ("gallons needed way I told you is", gallonsNeeded)    

#now this is done by function ceil
floatGallonsNeeded = areaRoom/areaPerGallon
print("float gallons needed",floatGallonsNeeded)
gallonsNeeded = ceil(floatGallonsNeeded)
print ("gallons needed with ceil function is", gallonsNeeded)


#Personal Note:
#ch06, slide 20
