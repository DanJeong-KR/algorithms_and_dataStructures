#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 17:19:09 2019

@author: changsicjung
"""

from collections import Counter

def perfectSubstring(s, k):
    
    
    result = 0
    
    if k > len(s):
        return result
        
    iterNum = len(s) // k # 반복할 횟수
    print('iterNum is : ',iterNum)
    
    for i in range(1,iterNum + 1): # i 는 1,2,3,4,5
        for idx, value in enumerate(s[:len(s) - (int(k * i) - 1)]):
            
            counter = Counter(s[idx:idx + int(k*i)])
            for i in counter.values():
                if i == k:
                    continue
                else:
                    break
            else:
                result += 1
    return result
            
    
    
def braces(values):
    
    
    
    braces = {'{' : '}', '[' : ']', '(' : ')'}
    
    result = []
    
    for value in values:
        
        stack = [] # 닫혀있는지 검사할 스택
        # 오픈인지 검사
        for brace in value:
            
            if brace in braces.keys(): #열려있는
                stack.append(brace) 
    
            elif brace in braces.values(): #닫혀있는
                if len(stack) == 0 or braces[stack[-1]] != brace: 
                    result.append('NO') # 빈 스택인데 닫힘 나오면
                    break
                else:
                    stack.pop(-1)
                    
        else:
            if len(stack) == 0:
                result.append('YES')
            else:
                result.append('NO')
        
    return result
        
        
        
braces(['{}[]()', '{[}]'])