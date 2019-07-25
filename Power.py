def power(base, pow):
    result = 1
    for i in range(pow):
        result *= base
    return result
base = int(input("Base: "))
pow = int(input("Power: "))
print(power(base, pow))