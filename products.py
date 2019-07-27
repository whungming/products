products = []
while True:
    name = input('please enter products: ')
    if name == 'q':
    	break
    price = input('please enter price: ')
    price = int(price)
                      #p = []
                      #p = [name, price]
                      #p.append(name)
                      #p.append(price)
                      #products.append(p)
    products.append([name, price])
#print(products)
#print(products[0][0])
#print(products[1][1])

for p in products:
	#print(p)     #show every list of name and price
	#print(p[0])  #show every list of name
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f: #with is good for "close" in programming. 
                                     #'w' means write 
                                      #'r' means read
                                      #if 亂碼 use encoding = 'utf-8'
    f.write('商品,價格\n')                                
    for p in products:
    	f.write(p[0] + ',' + str(p[1]) + '\n')