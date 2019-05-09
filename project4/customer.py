productslist = []
f = open('commodit', 'r', encoding='utf-8')
for line in f:
    productname, price = line.strip('\n').split()
    productslist.append((productname, int(price)))

print(productslist)
shopping_list = []

salary = input("请输入你的现金:")
if salary.isdigit():
    salary = int(salary)
    while True:
        # for item in productslist:
        #  print(productslist.index(item),item)
        for index, item in enumerate(productslist):
            print(index, item)
        # 判断用户要输入
        user_choice = input("请选择要买什啥>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(productslist) and user_choice >= 0:
                p_item = productslist[user_choice]
                if p_item[1] <= salary:  # 买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("加入 %s 购物车你的余额是\033[31;1m%s\033[0mRMB" % (p_item, salary))
                else:
                    print("\033[32;1m 你的余额只剩[%s]RMB啦，还买个毛线\033[0m " % salary)
            else:
                print("\033[41;1m您输入的商品不存在，请重新输入!\033[0m")
        elif user_choice == 'q':
            print("----shopping_list----")
            for p in shopping_list:
                print(p)
            print("你的余额:\033[31;1m%s\033[0mRMB" % salary)
            # 简单的余额记录
            f = open('salary', 'w+', encoding='utf-8')
            f.writelines(str(salary))
            f.close
            exit()
        else:
            print("错误选项")