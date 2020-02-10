import itertools
import xlsxwriter
import csv


results = []

with open("input.csv", "r") as f:
    lines = csv.reader(f)
    for line in lines:
        results.append([(i) for i in line])


# takes array and creates combinations
result = list(itertools.product(*results))

f.close()

print(result)


workbook = xlsxwriter.Workbook("arrays22.xlsx")
worksheet = workbook.add_worksheet()
col = 0

for row, data in enumerate(result):
    worksheet.write_row(row, col, data)

workbook.close()
