def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Cannot divide by zero"
    return a/b
def floor_division(a,b):
    if b==0:
        return "cannot divide by zero"
    return a//b
def modulus(a,b):
    if b==0:
        return "Cannot find modulus with zero"
    return a%b
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("\n--- Calculator Results ---")

print("Addition:", addition(num1, num2))
print("Subtraction:", subtraction(num1, num2))
print("Multiplication:", multiplication(num1, num2))
print("Division:", division(num1, num2))
print("Floor division:",floor_division(num1,num2))
print("Modulus:", modulus(num1, num2))

