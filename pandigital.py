def is_pandigital(num):
    num_str = str(num)
    n = len(num_str)
    return set(num_str) == set(str(i) for i in range(1, n + 1))

num = int(input("Enter a number: "))
if is_pandigital(num):
    print("Yes")
else:
    print("No")