products = []
while True:
    name = input('please enter products: ')
    if name == 'q':
    	break
    price = input('please enter price: ')
                      #p = []
                      #p = [name, price]
                      #p.append(name)
                      #p.append(price)
                      #products.append(p)
    products.append([name, price])
print(products)
print(products[0][0])
print(products[1][1])

for p in products:
	print(p)#show every list of name and price
	print(p[0])#show every list of name
	print(p[0], '的價格是', p[1])