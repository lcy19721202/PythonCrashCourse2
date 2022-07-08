## !/opt/local/bin/python
# -*- coding: utf-8 -*-

import numpy  # numpy是用于科学计算的Python扩展库

print(__name__)
print("矩阵乘法演示")

x = numpy.ones(3)  # ones()函数用于生成全1矩阵
m = numpy.eye(3)  # eye()函数用于生成单位矩阵
print("初始矩阵：\n", "\nx\n", x, "\nm\n", m)
m = m * 3
m[0, 2] = 5  # 设置矩阵指定位置上元素的值
m[2, 0] = 3
print("m*3:\n", m)
y = x @ m  # 矩阵相乘
print("x @ y\n", y)
