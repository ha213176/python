i = 100
tmp = 0
digit = 0
while i < 1000:
    tmp = i
    a = tmp//100
    tmp -= a*100
    b = tmp//10
    tmp -= b*10
    c = tmp
    result = a**3 + b**3 + c**3
    if result == i:
        print(i)
    i += 1
