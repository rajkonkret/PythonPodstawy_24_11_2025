import openpyxl

# pip install openpyxl

workbook = openpyxl.load_workbook('sales.xlsx')
print(workbook)  # <openpyxl.workbook.workbook.Workbook object at 0x000002163E30C1A0>
worksheet = workbook.active
print(worksheet)  # <Worksheet "Arkusz1">

lista = []
for i in worksheet:
    print(i)
# <Worksheet "Arkusz1">
# (<Cell 'Arkusz1'.A1>, <Cell 'Arkusz1'.B1>, <Cell 'Arkusz1'.C1>)
# (<Cell 'Arkusz1'.A2>, <Cell 'Arkusz1'.B2>, <Cell 'Arkusz1'.C2>)
# (<Cell 'Arkusz1'.A3>, <Cell 'Arkusz1'.B3>, <Cell 'Arkusz1'.C3>)
# (<Cell 'Arkusz1'.A4>, <Cell 'Arkusz1'.B4>, <Cell 'Arkusz1'.C4>)
# (<Cell 'Arkusz1'.A5>, <Cell 'Arkusz1'.B5>, <Cell 'Arkusz1'.C5>)