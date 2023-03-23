# CTI-110
# P3HW2 - Salary
# Corey Ocampo
# 3-23-2023
#

name = (input("Enter employee's name: "))
hours = float(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's pay rate: "))
print("-----------------------------------------------")
print(f'{name}')
if hours > 40:
  reg_pay = payrate * 40
  ovt_hrs = hours - 40
  ovt_pay = payrate * ovt_hrs * 1.5
  gross_pay = ovt_pay + reg_pay
else:
  reg_pay = hours * payrate
  ovt_pay = 0
  ovt_hrs = 0
  gross_pay = reg_pay + ovt_pay
  
print("Hours Worked   Pay Rate     OverTime     OverTime Pay    RegHour Pay   Gross Pay")
print("-------------------------------------------------------------------------------------")
print(f'{hours:<15.2f}{payrate:<13.2f}{ovt_hrs:<13.2f}{ovt_pay:<16.2f}{reg_pay:<14.2f}{gross_pay:<13.2f}')


