employee_file = open("employee.txt", "r" ) #r means read
print(employee_file.readlines()[1])
#print(employee_file.readline()) #prints second line
employee_file.close()
#readlines prints all lines
