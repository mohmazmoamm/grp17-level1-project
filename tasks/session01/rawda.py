i = 2
res = 1+2*i - ((2-5*i)/(3-i))
print (str(res))

#ex2
n=2
result=((n * 2) + 10) / (n + 1)
print (str(result))
#ex3
import math
r=2
v=((4/3)*math.pi* math.pow( r, 3))
A=(4*math.pi* math.pow( r, 2))
print (str(v))
print (str(A))
#ex4
i=2
re=((1+i* math.sqrt(2))*(2-3*i)*(3+i))
print (str(re))
#ex5
S=2
resu=((-((math.sqrt(2))/2) -(math.sqrt(2))/2))*S

resu= -math.sqrt(2)/2 - math.sqrt(2)/2*S
print (str(resu))
#ex6
B=2
RESULT=(math.pow( 1+B, 3)/math.pow( 1-B, 5))
print (str(RESULT))
#ex7
a = 1
b = 5
c = 2
root = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
print (str(root))
#ex8
loanAmount = 100000
monthlyInterestRate = 0.01
noYears = 7
monthlyPayment = loanAmount * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-noYears * 12))
totalPayment = monthlyPayment * noYears * 12
print("Monthly payment:", round(monthlyPayment, 2))
print("Total payment:", round(totalPayment, 2))
