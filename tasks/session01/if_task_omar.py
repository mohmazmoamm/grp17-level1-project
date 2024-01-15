# calaculator program
T = ["+", "-", "*", "/"]
a = str(input("hey , enter your name  :  "))
b = int(input("HEY " + a + " Enter your first number  :  "))
c = input("enter your sign  :  ")
d = int(input("enter your second number  :  "))

if c == "+":
    print(T[0], b + d)
elif c == "-":
    print(T[1], b - d)
elif c == "*":
    print(T[2], b * d)
elif c == "/":
    print(T[3], b / d)
else:
    print("error")