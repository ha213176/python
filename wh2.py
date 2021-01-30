buf = int(input())

i = 2
g = 1
while i < buf:
    if buf%i == 0:
        g = 0
        break
    i += 1
if g == 1:
    print("is")
else:
    print("isn't")