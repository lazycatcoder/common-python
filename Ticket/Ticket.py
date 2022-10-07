'''
The lucky ticket is the ticket, in the six-digit number of which the sum of the first three numbers is equal to the sum of the last three numbers
'''
a = int(input('enter 1st six-digit number: '))
b = int(input('enter 2nd six-digit number: '))

x = []
y = []

while a < b+1:
	x.insert(0,str(a))
	a += 1

for i in x:
	if len(i) < 6:
		while len(i) < 6:
			i = '0'+i
	y.insert(-1, i)
del x[0:]

for i in y:
	if (int(i[0])+int(i[1])+int(i[2])) == (int(i[3])+int(i[4])+int(i[5])):
		x.append(i)

print (len(x))   

'''
example:
a=222222, b=222333
res: 
7 (222222, 222231, 222240, 222303, 222312, 222321, 222330)
'''