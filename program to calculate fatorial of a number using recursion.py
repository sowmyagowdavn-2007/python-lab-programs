def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

n = int(input("Enter number: "))

res = fact(n)

print("The factorial of", n, "is", res)
