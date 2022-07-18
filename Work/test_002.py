##!/opt/local/bin/python
# -*- coding: utf-8 -*-

import numpy  # numpy是用于科学计算的Python扩展库

#-- 寻求帮助:
L = dir(list)
print(L)    # 简单的列出对象obj所包含的方法名称，返回一个字符串列表
help(str.rfind) # 查询obj.func的具体介绍和用法

#-- 测试类型的三种方法，推荐第三种
if type(L) == type([]):
    print("L is list")
if type(L) == list:
    print("L is list")
if isinstance(L, list):
    print("L is list")  




print("\n【矩阵乘法演示】\n")
x = numpy.ones(3)  # ones()函数用于生成全1矩阵
m = numpy.eye(3)  # eye()函数用于生成单位矩阵
print("初始矩阵：\n", "\nx\n", x, "\nm\n", m)
m = m * 3
m[0, 2] = 5  # 设置矩阵指定位置上元素的值
m[2, 0] = 3
print("m*3:\n", m)
y = x @ m  # 矩阵相乘
print("x @ y\n", y)

print(__name__)