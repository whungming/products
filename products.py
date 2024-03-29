import os # operating system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products
            
#讓使用者輸入
def user_input(products):
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
        print(products)
        return products
#print(products)
#print(products[0][0])
#print(products[1][1])

#印出所有購買記錄
def print_products(products):
    for p in products:
            #print(p)     #show every list of name and price
            #print(p[0])  #show every list of name
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w') as f: #with is good for "close" in programming. 
                                         #'w' means write 
        f.write('商品,價格\n')                                
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):#檢查檔案在不在
        print('yeah! 找到檔案了')
        products = read_file(filename)
    else:
        print('找不到檔案....')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)
main()