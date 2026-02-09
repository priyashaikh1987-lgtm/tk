pc = int(input("enter a number: "))
pc2 = int(input("enter another number: "))
print("1 = add, 2 = subtract, 3 = multply, 4 = division")
s = int(input("enter a number 1 to 4: "))
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mult(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
if s == 1:
    add(pc,pc2)
elif s == 2:
    sub(pc,pc2)
elif s == 3:
    mult(pc,pc2)
elif s == 4:
    div(pc,pc2)
else:
    print("invalid input")