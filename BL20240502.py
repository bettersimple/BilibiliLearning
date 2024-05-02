# -*- coding = utf-8 -*-
# @Time: 2024/5/2 12:13
# @Author: JaDM
# @File: BilibiliLearning20240502.py
# @Software: PyCharm
# @Url: https://www.bilibili.com/video/BV12E411A7ZQ/?p=6&vd_source=a2baf25ae75bc2f30de0f8ce15b304f3
"""
#九九乘法表
#1. for循环
for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %d"%(i,j,i * j),end = "\t")
    print()
"""
#2. while循环
"""
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{i} * {j} = {i * j}",end = "\t")
        j += 1
    i += 1
    print()
"""
