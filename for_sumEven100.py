# _*_ coding: utf-8 _*_
import random

### 使用分支结构，实现1~100之间偶数求和
s_even = 0
for i in range(101):
    if i%2 == 0:
        s_even += i
print(s_even)

### 不使用分支结构，实现1~100之间偶数求和
s2_even = 0
for i in range(0,101,2):
    s2_even += i
print(s2_even)

### 猜数字游戏：计算出1~100之间的一个随机数由人来猜
### 根据人猜的数字分别给出提示大一点/小一点/猜对了

li = [i for i in range(101)]
a = random.choice(li)
print(a)
i = int(input("请输入一个1~100内的整数，并按Enter键结束输入："))
while(True):
    if i < a:
        i = int(input(f"猜小了，请重新输入一个{i}~100内的整数，并按Enter键结束输入："))
    elif i > a:
        i = int(input(f"猜大了，请重新输入一个1~{i}内的整数，并按Enter键结束输入："))
    else:
        print("恭喜您，猜对了！")
        break


