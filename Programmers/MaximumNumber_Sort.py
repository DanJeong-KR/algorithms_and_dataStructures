#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:44:49 2019

@author: changsicjung
"""
'''
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

numbers의 길이는 1 이상 100,000 이하입니다. 
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

입출력 예
[6, 10, 2]	'6210'
[3, 30, 34, 5, 9]	'9534330'
[3, 303, 323, 365, 395, 86, 96]  '9686395365'
[54, 55, 52, 5, 50, 56, 5796, 5231]  5796 56 55 54 5231 52
'''

'''
* 0 이면 첫 자리에 올 수 없고
* 가장 큰 수가 앞에 와야 하고

(1) 문자에 인덱스로 접근하기 위해 문자열로 바꾸기

(2) 크게 만드는 수 의 기준만 찾기

수의 길이가 같으면 비교만 하면 되는데 
3 / 32 / 33 / 34 비교해보기.    ->   34 33 3 32
34 / 342 / 343 / 344 -> 34 344 343

(3)
리스트에 0 만 있다면 ? 
0000 -> 0 으로 바꾸어 줘야해
 
'''

## 강의 풀이
def solution(numbers):
    
    #(1)
    numbers = [str(i) for i in numbers]
    
    # (2)
    numbers.sort(key=lambda x : (x*4)[:4], reverse=True)
    
    #(3)
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    
    
    
    return answer


## 인기풀이 1

def solution2(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers))) # '000' 을 0 으로 바꾸기 위해 int

## 인기풀이 2
    
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0 (key function으로 만드려면 이렇게 해야함)
    if int(t1) > int(t2):
        return 1
    elif int(t1) < int(t2):
        return -1
    else:
        return 0

def solution3(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer





