x = open('mp.pdf','w')
x.write('Hey guys!\n')
x.write('I am your boss\n')
x.close()
y = open('mp.pdf','r')
text = y.read()
print(text)
y.close()










