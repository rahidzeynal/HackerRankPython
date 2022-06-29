n = int(input())

while n < 0:
    pass
else:
    for i in range(n):
        t = " ".join(str(i+1))
print(hash(t))
