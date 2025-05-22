
import csv
from prettytable import PrettyTable

# context manager
with open("Employee.csv", "r") as CSVR:
    emp_details = csv.reader(CSVR)
    prtyTbl = PrettyTable(next(emp_details))
    # colNames = next(emp_details)
    # print(colNames)

    for row in emp_details:
        # print(*row)
        prtyTbl.add_row(row)

print(prtyTbl)