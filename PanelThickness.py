# input for panel thickness

print ('Panel thickness:')

panelThickness = int(input())

if panelThickness == 66:
    machinedPlankthickness1 = 22
    machinedPlankthickness2 = 22
    machinedPlankthickness3 = 22
    roughPlankthickness1 = 25
    roughPlankthickness2 = 25
    roughPlankthickness3 = 25

elif panelThickness == 77:
    machinedPlankthickness1 = 22
    machinedPlankthickness2 = 33
    machinedPlankthickness3 = 22
    roughPlankthickness1 = 25
    roughPlankthickness2 = 38
    roughPlankthickness3 = 25

elif panelThickness == 88:
    machinedPlankthickness1 = 33
    machinedPlankthickness2 = 22
    machinedPlankthickness3 = 33
    roughPlankthickness1 = 38
    roughPlankthickness2 = 25
    roughPlankthickness3 = 38

elif panelThickness == 99:
    machinedPlankthickness1 = 33
    machinedPlankthickness2 = 33
    machinedPlankthickness3 = 33
    roughPlankthickness1 = 38
    roughPlankthickness2 = 38
    roughPlankthickness3 = 38

elif panelThickness == 110:
    machinedPlankthickness1 = 22
    machinedPlankthickness2 = 22
    machinedPlankthickness3 = 22
    machinedPlankthickness4 = 22
    machinedPlankthickness5 = 22
    roughPlankthickness1 = 25
    roughPlankthickness2 = 25
    roughPlankthickness3 = 25
    roughPlankthickness4 = 25
    roughPlankthickness5 = 25

elif panelThickness == 121:
    machinedPlankthickness1 = 22
    machinedPlankthickness2 = 22
    machinedPlankthickness3 = 33
    machinedPlankthickness4 = 22
    machinedPlankthickness5 = 22
    roughPlankthickness1 = 25
    roughPlankthickness2 = 25
    roughPlankthickness3 = 38
    roughPlankthickness4 = 25
    roughPlankthickness5 = 25

elif panelThickness == 132:
    machinedPlankthickness1 = 22
    machinedPlankthickness2 = 33
    machinedPlankthickness3 = 22
    machinedPlankthickness4 = 33
    machinedPlankthickness5 = 22
    roughPlankthickness1 = 25
    roughPlankthickness2 = 38
    roughPlankthickness3 = 25
    roughPlankthickness4 = 38
    roughPlankthickness5 = 25

elif panelThickness == 143:
    machinedPlankthickness1 = 33
    machinedPlankthickness2 = 22
    machinedPlankthickness3 = 33
    machinedPlankthickness4 = 22
    machinedPlankthickness5 = 33
    roughPlankthickness1 = 38
    roughPlankthickness2 = 25
    roughPlankthickness3 = 38
    roughPlankthickness4 = 25
    roughPlankthickness5 = 38

elif panelThickness == 165:
    machinedPlankthickness1 = 33
    machinedPlankthickness2 = 33
    machinedPlankthickness3 = 33
    machinedPlankthickness4 = 33
    machinedPlankthickness5 = 33
    roughPlankthickness1 = 38
    roughPlankthickness2 = 38
    roughPlankthickness3 = 38
    roughPlankthickness4 = 38
    roughPlankthickness5 = 38


else:
    print ('This is not a standard length')

if panelThickness < 100:
    print(machinedPlankthickness1)
    print(machinedPlankthickness2)
    print(machinedPlankthickness3)
    print(roughPlankthickness1)
    print(roughPlankthickness2)
    print(roughPlankthickness3)

elif panelThickness > 100:
    print(machinedPlankthickness1)
    print(machinedPlankthickness2)
    print(machinedPlankthickness3)
    print(machinedPlankthickness4)
    print(machinedPlankthickness5)
    print(roughPlankthickness1)
    print(roughPlankthickness2)
    print(roughPlankthickness3)
    print(roughPlankthickness4)
    print(roughPlankthickness5)

else:
    print("I'm not sure")
