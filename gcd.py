def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("GCD:", gcd(n1, n2))