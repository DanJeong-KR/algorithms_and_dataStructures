#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:29:15 2019

@author: changsicjung
"""

import functools

def comparator(a, b):
    t1 = a + b
    t2 = b + a
    
    if int(t1) > int(t2):
        return 1
    elif int(t1) < int(t2):
        return -1
    else:
        return 0

def solution(numbers):
    _numbers = [str(n) for n in numbers]
    
    result = sorted(_numbers, key=functools.cmp_to_key(comparator), reverse=True)
    
    
    return str(int(''.join(result)))

