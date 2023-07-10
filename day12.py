# Find the Largest Among Three Numbers

a=int(input("Enter The value of a : "))
b=int(input("Enter The value of b : "))
c=int(input("Enter The value of c : "))

if a>b and a>c:
    print("A is Largest")
elif b>a and b>c:
    print("B is Largest")
else:
    print("C is Largest")