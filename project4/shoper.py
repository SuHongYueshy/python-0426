import os

ps = '''
1 >>>>>> 修改商品
2 >>>>>> 添加商品
按q为退出程序
'''

# 打开两个文件，f文件为原来存取商品文件,f_new文件为修改后的商品文件
f = open('commodit', 'r', encoding='utf-8')
f_new = open('commodit_update', 'w+', encoding='utf-8')
file_list = f.readlines()

# 打印商品信息
while True:
    productslist = []
    # 从商品文件中读取出来的数据存放到productslist列表里
    for line in file_list:
        productname = line.strip().split()
        productname, oldprice = line.strip("\n").split()
        productslist.append([productname, int(oldprice)])
    choose = input("%s请选择：" % ps)
    if choose == '1':
        for index, item in enumerate(productslist):
            print(index, item)
        productindex = input("请输入要修改价格的商品序号:")
        if productindex.isdigit():
            productindex = int(productindex)
        while True:
            print('要修改商品信息:', productslist[productindex])
            price = input("请输入要修改的价格:")
            if price.isdigit():
                price = int(price)
                productslist[productindex][1] = price
                break
            else:
                print("请正确的输入价格！")
                continue

        # 已经修改好的商品列表循环写入f_new文件夹

        for products in productslist:
            insert_data = "%s %s" % (products[0], products[1])
            f_new.write(insert_data + '\n')
        print("商品价格已经修改！")
        # 替换原来的文件
        f_new = open('commodit_update', 'r', encoding='utf-8')
        data = f_new.readlines()
        f = open('commodit', 'w+', encoding='utf-8')
        for line in data:
            f.write(line)
        f.close()
        f_new.close()
        # 删除替换文件
        os.remove('commodit_update')
    elif choose == '2':
        # 添加商品
        f = open('commodit', 'a+', encoding='utf-8')
        pricename = input("请输入商品名:")
        while True:
            price = input("请输入商品价格:")
            if price.isdigit():
                f.writelines('%s %s\n' % (pricename, price))
                break
            else:
                print('输入错误请重新输入!')
                continue
        f.close()
        continue
    elif choose == 'q':
        break
    else:
        print("输入错误请重新输入")
        continue