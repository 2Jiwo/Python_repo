import math

print("a, b, c' 3개의 값을 입력하시오")
a = int(input("a의 값을 입력하시오.: "))
b = int(input("b의 값을 입력하시오.: "))
c = int(input("c의 값을 입력하시오.: "))

d= math.sqrt(b*b) - (4*a*c); 
x1 = (-b + d) / (2 * a) 
x2 = (-d - d) / (2 * a)

print(x1, x2)