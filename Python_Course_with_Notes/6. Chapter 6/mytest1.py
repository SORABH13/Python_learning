a = int(input("please enter first number: "))
b = int(input("please enter second number: "))
c = int(input("please enter third number: "))
d = int(input("please enter fourth number: "))

if a>d:
    f1 = a
else:
    f1 = d
if b>c:
    f2 = b
else:
    f2 = c

if f1>f2:
    print(str(f1) + " is greatest number")
else:
    print(str(f2) + " is greatest number")


