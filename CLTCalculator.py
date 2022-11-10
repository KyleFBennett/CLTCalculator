'''
a calculator for XLAM to calculate
the length of each plank and number of
planks needed
'''

import math
from tabulate import tabulate   # for table 
import xlsxwriter               # for exporting to excel

print('Project title:')
project = input()

print('Panel thickness:')
panelThickness = int(input())    

print('Grain length?')
grainLength = input()
print('short length?')
shortLength = input()

# panel thickness from input 

if panelThickness == 66:
    machinedPlankthickness = [22,22,22]
    roughPlankthickness = [25,25,25]

elif panelThickness == 77:
    machinedPlankthickness = [22,33,22]
    roughPlankthickness = [25,38,25]

elif panelThickness == 88:
    machinedPlankthickness = [33,22,33]
    roughPlankthickness = [38,25,38]

elif panelThickness == 99:
    machinedPlankthickness = [33,33,33]
    roughPlankthickness = [38,38,38]

elif panelThickness == 110:
    machinedPlankthickness = [22,22,22,22,22]
    roughPlankthickness = [25,25,25,25,25]

elif panelThickness == 121:
    machinedPlankthickness = [22,22,33,22,22]
    roughPlankthickness = [25,25,38,25,25]

elif panelThickness == 132:
    machinedPlankthickness = [22,33,22,33,22]
    roughPlankthickness = [25,38,25,38,25]

elif panelThickness == 143:
    machinedPlankthickness = [33,22,33,22,33]
    roughPlankthickness = [38,25,38,25,38]

elif panelThickness == 154:
    machinedPlankthickness = [33,33,22,33,33]
    roughPlankthickness = [38,38,25,38,38]

elif panelThickness == 165:
    machinedPlankthickness = [33,33,33,33,33]
    roughPlankthickness = [38,38,38,38,38]

else:
    print ('This is not a standard length')

# machined dimensions

plankWidth = int(140)

# rough dimensions

roughWidth = int(152)

# quantity of planks

grainPlanks = math.ceil(int(shortLength) / plankWidth + 1)
shortPlanks = math.ceil(int(grainLength) / plankWidth + 1)

# length of planks

shortNestedLength = int(grainPlanks * plankWidth) - 50
grainNestedLength = int(shortPlanks * plankWidth) - 50

# print ('Waste: ' + str(waste) + '%')

# table 

mydata = [
    [grainPlanks, grainNestedLength],
    [shortPlanks, shortNestedLength],
    [grainPlanks, grainNestedLength]
    ]

head = ['QTY', 'Length']

print(tabulate(mydata, headers=head, tablefmt='grid'))

# excel export

workbook = xlsxwriter.Workbook(project + 'test.xlsx.')      # creates file name 
worksheet = workbook.add_worksheet()                        # creates sheet name in brackets, defaults to sheet 1

bold = workbook.add_format({'bold':True})                   # for bold cells

merge_format = workbook.add_format({
    'bold': True,
    'align': 'center',
    })                                                      # to merge cells 

# heading -             ROW 1

worksheet.merge_range('A1:J1', 'N1', merge_format)

# machined & rough -    ROW 2

worksheet.merge_range('C2:F2', 'Machined', merge_format)
worksheet.merge_range('G2:J2', 'Rough', merge_format)

# titles -              ROW 3 

worksheet.write('A3', 'QTY',            bold)
worksheet.write('B3', 'Length (mm)',    bold)
worksheet.write('C3', 'Thickness (mm)', bold)
worksheet.write('D3', 'Width (mm)',     bold)
worksheet.write('E3', 'Volume (m3)',    bold)
worksheet.write('F3', 'Weight (kg)',    bold)
worksheet.write('G3', 'Thickness (mm)', bold)
worksheet.write('H3', 'Width (mm)',     bold)
worksheet.write('I3', 'Volume (m3)',    bold)
worksheet.write('J3', 'Weight (kg)',    bold)

# for 3 layer and 5 layer


# all formulas below 

worksheet.write('D7', 'TOTAL', bold)            # totals for final row
worksheet.write('H7', 'TOTAL', bold)            # totals for final row 

# formulas for machined volume

worksheet.write_formula('E4', '=round(A4*(B4/1000)*(C4/1000)*(D4/1000),3)')
worksheet.write_formula('E5', '=round(A5*(B5/1000)*(C5/1000)*(D5/1000),3)')
worksheet.write_formula('E6', '=round(A6*(B6/1000)*(C6/1000)*(D6/1000),3)')

# formulas for machined weight

worksheet.write_formula('F4', '=round(E4*480,3)')
worksheet.write_formula('F5', '=round(E5*480,3)')
worksheet.write_formula('F6', '=round(E6*480,3)')

# formulas for rough volume

worksheet.write_formula('I4', '=round(A4*(B4/1000)*(G4/1000)*(H4/1000),3)')
worksheet.write_formula('I5', '=round(A5*(B5/1000)*(G5/1000)*(H5/1000),3)')
worksheet.write_formula('I6', '=round(A6*(B6/1000)*(G6/1000)*(H6/1000),3)')

# formulas for rough weight

worksheet.write_formula('J4', '=round(I4*480,3)')
worksheet.write_formula('J5', '=round(I5*480,3)')
worksheet.write_formula('J6', '=round(I6*480,3)')

if panelThickness < 100:
    
    # formula for total machined voulme and weight

    worksheet.write_formula('E7', '=SUM(E4,E5,E6)', bold)
    worksheet.write_formula('F7', '=SUM(F4,F5,F6)', bold)

    # formula for total machined voulme and weight

    worksheet.write_formula('I7', '=SUM(I4,I5,I6)', bold)
    worksheet.write_formula('J7', '=SUM(J4,J5,J6)', bold)

    # table info

    FJmachining = (
        [grainPlanks, grainNestedLength, machinedPlankthickness[0], plankWidth, roughPlankthickness[0], roughWidth],
        [shortPlanks, shortNestedLength, machinedPlankthickness[1], plankWidth, roughPlankthickness[1], roughWidth],
        [grainPlanks, grainNestedLength, machinedPlankthickness[2], plankWidth, roughPlankthickness[2], roughWidth]
        )

else:
    # formulas for machined volume

    worksheet.write_formula('E7', '=round(A7*(B7/1000)*(C7/1000)*(D7/1000),3)')
    worksheet.write_formula('E8', '=round(A8*(B8/1000)*(C8/1000)*(D8/1000),3)')

    # formulas for machined weight

    worksheet.write_formula('F7', '=round(E7*480,3)')
    worksheet.write_formula('F8', '=round(E8*480,3)')

    # formulas for rough volume

    worksheet.write_formula('I7', '=round(A7*(B7/1000)*(G7/1000)*(H7/1000),3)')
    worksheet.write_formula('I8', '=round(A8*(B8/1000)*(G8/1000)*(H8/1000),3)')

    # formulas for rough weight

    worksheet.write_formula('J7', '=round(I7*480,3)')
    worksheet.write_formula('J8', '=round(I8*480,3)')

    # formula for total machined voulme and weight

    worksheet.write_formula('E9', '=SUM(E4,E5,E6,E7,E8)', bold)
    worksheet.write_formula('F9', '=SUM(F4,F5,F6,F7,F8)', bold)

    # formula for total machined voulme and weight

    worksheet.write_formula('I9', '=SUM(I4,I5,I6,I7,I8)', bold)
    worksheet.write_formula('J9', '=SUM(J4,J5,J6,J7,J8)', bold)

    # table info

    FJmachining = (
        [grainPlanks, grainNestedLength, machinedPlankthickness[0], plankWidth, roughPlankthickness[0], roughWidth],
        [shortPlanks, shortNestedLength, machinedPlankthickness[1], plankWidth, roughPlankthickness[1], roughWidth],
        [grainPlanks, grainNestedLength, machinedPlankthickness[2], plankWidth, roughPlankthickness[2], roughWidth],
        [shortPlanks, shortNestedLength, machinedPlankthickness[3], plankWidth, roughPlankthickness[3], roughWidth],
        [grainPlanks, grainNestedLength, machinedPlankthickness[4], plankWidth, roughPlankthickness[4], roughWidth]
        )

# end of panel thickness

row = 3                                         # starts under titles so that it does not erase
col = 0

for planks, length, plankThickness, plankWidth, roughThickness, roughWidth in (FJmachining):
    worksheet.write(row, col, planks)
    worksheet.write(row, col + 1, length)
    worksheet.write(row, col + 2, plankThickness)
    worksheet.write(row, col + 3, plankWidth)
    worksheet.write(row, col + 6, roughThickness)
    worksheet.write(row, col + 7, roughWidth)
    row += 1

workbook.close()
