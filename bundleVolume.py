# divide volume by bundle volume to create order list 

def bundleVolume(numberOfPlanks, plankWidth, plankHeight, plankLength, units):
    volume = numberOfPlanks * plankWidth * plankHeight * plankLength / units
    return volume

#25mm bundles 

twenty52400 = bundleVolume(126, 152, 25, 2400, 1000000000)
twenty52700 = bundleVolume(126, 152, 25, 2700, 1000000000)
twenty53000 = bundleVolume(126, 152, 25, 3000, 1000000000)
twenty53600 = bundleVolume(126, 152, 25, 3600, 1000000000)
twenty54200 = bundleVolume(126, 152, 25, 4200, 1000000000)
twenty54800 = bundleVolume(126, 152, 25, 4800, 1000000000)

twenty5 = [twenty52400, twenty52700, twenty53000, twenty53600, twenty54200, twenty54800] 

#38mm bundles 

thirty82400 = bundleVolume(84, 152, 38, 2400, 1000000000)
thirty82700 = bundleVolume(84, 152, 38, 2700, 1000000000)
thirty83000 = bundleVolume(84, 152, 38, 3000, 1000000000)
thirty83600 = bundleVolume(84, 152, 38, 3600, 1000000000)
thirty84200 = bundleVolume(84, 152, 38, 4200, 1000000000)
thirty84800 = bundleVolume(84, 152, 38, 4800, 1000000000)

thirty8 = [thirty82400, thirty82700, thirty83000, thirty83600, thirty84200, thirty84800]

# input volme and divide by bundle volumes 

print('Thickness:')

thickness = int(input())

print('Volume:')

volume = int(input())

if thickness == 25: 
    newList = [volume / x for x in twenty5]
    print(newList)

else:
    newList = [volume / x for x in thirty8]
    print(newList)
    
