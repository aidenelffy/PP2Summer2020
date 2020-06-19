l, r = [int(x) for x in input().split()]
for n in range(l, r + 1):
    if n % 7 == 1 or n % 7 == 2 or n % 7 == 5:
        print(n, end = ' ')
