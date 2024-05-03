# -*- coding = utf-8 -*-
# @Time: 2024/5/3 10:32
# @Author: JaDM
# @File: BL20240503.py
# @Software: PyCharm
# @Url: https://www.bilibili.com/video/BV12E411A7ZQ/?p=9&spm_id_from=pageDriver&vd_source=a2baf25ae75bc2f30de0f8ce15b304f3

"""
# 1.
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
print("------  商品列表  ------")
"""
"""
for i in range(len(products)):
    print(i,products[i][0],products[i][1],end="\t")
    print()
"""
"""
j = 0
for i in products:
    print(j,i[0],i[1],end="\t")
    j +=1
    print()
"""
# 2. 根据上面的products写一个循环，不断询问客户想买什么，
#    用户选择一个商品编号，就把对应的商品添加到购物车里，
#    最终用户输入q退出时，打印购买的商品列表
"""
products = [["iphone",6888],["MacPro",14800],["小米6",2499],["Coffee",31],["Book",60],["Nike",699]]
number = input("请输入您想购买的商品编号，输入\"q\"退出:")
wantbuy = []
while number != "q":
    if number == "q" or number.isdigit():
        while number != "q":
            number = int(number)
            if number in range(len(products)):
                wantbuy.append(number)
                number = input("请继续输入您想购买的商品编号，输入\"q\"退出:")
            else:
                print("该商品不存在，请重新输入!")
                number = input("请重新输入您想购买的商品编号，输入\"q\"退出:")
        else:
            print("------  您想购买的商品列表为：  ------")
            j = 0
            for i in wantbuy:
                print(i,products[i][0],products[i][1],end="\t")
                j += products[i][1]
                print()
            print(f"您总计选择{len(wantbuy)}件商品，共{j}元")
    else:
        print("请输入商品编号(数字)或\"q\"!")
        number = input("请重新输入您想购买的商品编号，输入\"q\"退出:")
"""
"""
练习2：
https://www.bilibili.com/video/BV12E411A7ZQ?p=12&spm_id_from=pageDriver&vd_source=a2baf25ae75bc2f30de0f8ce15b304f3
1.写一个打印一条横线的函数。
2.写一个函数，可以通过输入的参数，打印出自定义行数的横线。
3.写一个函数求三个数的和
4.写一个函数求三个函数的平均值（提示：调用上面的函数）
"""
"""
def printline():
    print("------------------")
printline()

def linenums():
    n = input("请输入要打印的行数：")
    if n.isdigit():
        for i in range(n):
            printline()
    else:
        print("请输入整数！")
linenums()
"""
"""
def sum3(a,b,c):
    return a+b+c
result = sum3(1,2,3)
print(result)

def avg3(i,j,k):
    return sum3(i,j,k)/3
result2 = avg3(4,5,6)
print(result2)
"""
"""
作业：
1.应用文件操作的相关知识，通过Python新建一个文件gushi.txt，选择一首古诗写入文件中
2.另外写一个函数，读取指定文件gushi.txt，将内容复制到copy.txt中，并在控制台输出”复制完毕“
3.提示：分别定义两个函数，完成读文件和写文件的操作
       尽可能完善代码，添加异常处理
"""
f = open("gushi.txt", "w", encoding="utf-8")             #with open("gushi.txt","w",encoding="utf-8") as f:
poem = """          《忆秦娥・娄山关》
西风烈，长空雁叫霜晨月。霜晨月，马蹄声碎，喇叭声咽。
雄关漫道真如铁，而今迈步从头越。从头越，苍山如海，残阳如血。
"""
f.write(poem)
f.close()

def readdir(file):
    try:
        f = open(file, "r", encoding="utf-8")
        content = f.readlines()
        return content
    except Exception as error:
        print(f"出错了，错误是：{error}")
    finally:
        f.close()

def copydir():
    try:
        with open("copy.txt", "w", encoding="utf-8") as f:
            content = readdir("gushi.txt")
            for i in content:
                f.write(i)
    except Exception as error:
        print(f"出错了，错误是：{error}")
    finally:
        print("复制完毕")
copydir()