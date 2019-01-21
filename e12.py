#String Palindrome
x = "mom"
lw = 0
hg = len(x) - 1
while hg > 1:
    if x[hg] != x[lw]:
        hg-=1
        lw+=1
        print('No pali')
        break







