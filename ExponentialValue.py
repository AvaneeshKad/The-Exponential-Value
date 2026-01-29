import math

x = int(input("Enter the number of which the exponential is supposed to be calculated : "))

e_x = []
for i in range(0,11):
    e_x.append(x ** i / math.factorial(i))

print("Number of Terms:\tEstimates: ")
for i in range(len(e_x)-1):
    print("{0} \t\t\t {1}".format(i, e_x[i]))
