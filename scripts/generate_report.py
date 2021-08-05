#!/usr/bin/env python3
# Now, import the CSV module.
import csv
#Define the function read_employees. This function takes file_location (path to employees.csv) as a parameter.

def read_employees(csv_file_location):
  csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
  employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
  employee_list = []
  for data in employee_file:
    employee_list.append(data)
  return employee_list

employee_list = read_employees("c:/Users/queen/Python/handling-files/data/employees.csv")
# print(employee_list)

# The second function process_data() should now receive the employee_list as a parameter and return a dictionary of department:amount.
def process_data(employee_list):
  department_list = []
  for employee_data in employee_list:
    department_list.append(employee_data['Department'])
  department_data = {}
  for department_name in set(department_list):
    department_data[department_name] = department_list.count(department_name)
  return department_data

dictionary = process_data(employee_list)
# print(dictionary)

# we will write the function write_report. This function writes a dictionary of department: amount to a file.
def write_report(dictionary, report_file):
  with open(report_file, "w+") as f:
    for k in sorted(dictionary):
      f.write(str(k)+':'+str(dictionary[k])+'\n')
    f.close()

write_report(dictionary, 'c:/Users/queen/Python/handling-files/data/report.txt')
# This script does not generate any output, but it creates a new file named report.txt within the data directory.