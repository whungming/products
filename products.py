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