items = ['Mango', 'Orange', 'Apple', 'Lemon']
file = open('words1.txt','w')
for  item in items:
	file.write(item+"\n")
file.close()
