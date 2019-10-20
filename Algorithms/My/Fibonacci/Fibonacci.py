#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 23:59:16 2019

@author: changsicjung
"""


# 반복문
def fibonacci_for(n):
    if n == 0 or n == 1:
        return n
    result = 0
    a = 0
    b = 1
    
    for i in range(2, n + 1):
        result = a + b
        a = b
        b = result
    return result

# 재귀호출
def fibonacci_recur(n):
    if n == 0 or n == 1:
        return n
    
    return fibonacci_recur(n - 1) + fibonacci_recur(n - 2)



# 메모제이션을 적용한 재귀. 
memo = [-1] * 100
def fibonacci_memo(n):
    if n == 0 or n == 1:
        memo[n] = n
        
    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
        return memo[n]