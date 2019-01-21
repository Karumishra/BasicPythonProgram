

rev = 0
n = 111
while n > 0:
    d = n%10
    rev = rev*10 + d
    n = n/10

if rev == 111:
    print("N is palindrome")
else:
    print("N is not palindrome")



