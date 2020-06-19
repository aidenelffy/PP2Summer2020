a = int (input())
b = int (input())
c = a * b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
gcd = a + b
lcm = c // gcd
print (lcm + gcd)