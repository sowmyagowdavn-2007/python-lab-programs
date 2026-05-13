def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

x = maximum(5, 4, 9)
print("Maximum number =", x)
    
