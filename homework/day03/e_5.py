# 对一个 tuple 进行各种切片操作
L = range(1,101)
print (L[-10:] ) #取出最后10个数
print (L[-50:-1:2]) #在倒数50到倒数第1个数中每2个数取一个即隔一个取一个数
print (L[4::5][-10:] ) #取出最后10个5的倍数