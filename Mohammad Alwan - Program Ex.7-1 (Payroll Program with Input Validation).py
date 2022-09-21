#Mohammad Alwan, Program Ex.7-1 (Payroll Program with Input Validation)

#Inputs for the hours worked and hourly pay rate of employee
hourlyPayRate = float(input("Please input hourly pay rate: "))

while not( hourlyPayRate >= 7.50 and hourlyPayRate <= 18.25):
    print("Invalid input")
    hourlyPayRate = input("Please input hourly pay rate between 7.50 to 18.25: ")

HoursWorked = int(input("Please input amount nuber of hour(s) worked: "))
while not(HoursWorked >= 0 and HoursWorked <= 40):
    print("Invalid input")
    HoursWorked = input("Please input amount nuber of hour(s) worked between 0 to 40: ")

GrossPay = (HoursWorked * hourlyPayRate)

print("You worked",HoursWorked,"hour(s) and your hourly pay rate is",hourlyPayRate,)
print("Your total gross pay will be",GrossPay)
