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

# machined dimensions

plankWidth = int(140)
plankThickness = int(22)

# rough dimensions

roughWidth = int(152)
roughThickness = int(25)

# quantity of planks

grainPlanks = math.ceil(int(shortLength) / plankWidth + 1)
shortPlanks = math.ceil(int(grainLength) / plankWidth + 1)

# length of planks

shortNestedLength = int(grainPlanks * plankWidth) - 50
grainNestedLength = int(shortPlanks * plankWidth) - 50

panelArea = (int(grainLength) * int(shortLength)) / 100000 
nestedArea = (int(grainNestedLength) * int(shortNestedLength)) / 100000

percentage = round((int(panelArea) / int(nestedArea)) * 100,0)
waste = 100 - int(percentage)

# print (grainPlanks)
# print (shortPlanks)
# print (shortNestedLength)
# print (grainNestedLength)
# print (str(panelArea) + 'm2')  
# print (str(nestedArea) + 'm2')
# print (str(percentage) + '%')
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

# heading

worksheet.merge_range('A1:J1', 'N1', merge_format)

# machined & rough

worksheet.merge_range('C2:F2', 'Machined', merge_format)
worksheet.merge_range('G2:J2', 'Rough', merge_format)

# titles

worksheet.write('A3', 'QTY', bold)
worksheet.write('B3', 'Length (mm)', bold)
worksheet.write('C3', 'Width (mm)', bold)
worksheet.write('D3', 'Thickness (mm)', bold)
worksheet.write('E3', 'Volume (m3)', bold)
worksheet.write('F3', 'Weight (kg)', bold)
worksheet.write('G3', 'Width (mm)', bold)
worksheet.write('H3', 'Thickness (mm)', bold)
worksheet.write('I3', 'Volume (m3)', bold)
worksheet.write('J3', 'Weight (kg)', bold)

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

# formula for total machined voulme and weight

worksheet.write_formula('E7', '=SUM(E4,E5,E6)', bold)
worksheet.write_formula('F7', '=SUM(F4,F5,F6)', bold)

# formula for total machined voulme and weight

worksheet.write_formula('I7', '=SUM(I4,I5,I6)', bold)
worksheet.write_formula('J7', '=SUM(J4,J5,J6)', bold)

# table info

FJmachining = (
    [grainPlanks, grainNestedLength, plankThickness, plankWidth, roughThickness, roughWidth],
    [shortPlanks, shortNestedLength, plankThickness, plankWidth, roughThickness, roughWidth],
    [grainPlanks, grainNestedLength, plankThickness, plankWidth, roughThickness, roughWidth]
    )
 
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










































