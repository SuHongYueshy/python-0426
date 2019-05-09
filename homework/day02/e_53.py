# 请根据 BMI 公式，根据用户输入计算 BMI 指数，并输出测试结果

H = float(input(f'请输入您的身高：'))
W = float(input(f'请输入您的体重：'))
bmi = W / H ** 2
if bmi <= 18:
    print("过轻")
elif 18.5 <= bmi < 25:
    print("正常")
elif 25 <= bmi < 28:
    print("过重")
elif 28 <= bmi < 32:
    print("肥胖")
elif bmi > 32:
    print("严重肥胖")
