n = int(input())
n = bin(n)
print(int(''.join(reversed(n[2:6])),2))