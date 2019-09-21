#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 19:53:40 2019

@author: changsicjung
"""


# 파스칼 삼각형 구현
# dict 이용
# x, y 좌표계 이용
# n 에 따라 n-1 의 길이를 가진 이등변 삼각형 모양을 가짐
# n 에 다라 접근 가능한 dic의 범위가 정해진다. (n이 4라면 3,0 2,1 1,2 0,3 이 제한.)
def pascal(x, y):
    if min(x, y) == 0:
        return 1
    
    mini = min(x, y)
    n = mini + max(x, y)
    
    p = dict()
    
    for i in range(n + 1):
        p[(i,0)] = 1
        p[(0,i)] = 1
        
        for k in range(1, i):
            p[(i - k, k)] = p[(i - k, k - 1)] + p[(i - k - 1, k)]
            
    return p[(x, y)]
    

