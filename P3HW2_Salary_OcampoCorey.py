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
  gross_pay = hours * payrate
print("Hours Worked   Pay Rate     OverTime     OverTime Pay    RegHour Pay   Gross Pay")
print("-------------------------------------------------------------------------------------")
print(f'{hours}           {payrate}         {ovt_hrs}          {ovt_pay}          {reg_pay}         {gross_pay}')


