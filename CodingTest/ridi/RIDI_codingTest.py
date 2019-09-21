#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:46:01 2019

@author: changsicjung
"""

'''
def solution(location, s, e):
    
    location = sorted(location)
    answer = []
    
    mini = [min(s[0], e[0]), min(s[1], e[1])]
    maxi = [max(s[0], e[0]), max(s[1], e[1])]
    
    for point in location: # i 는 [x, y]
        if point[0] < mini[0] or point[1] < mini[1] or point[1] > maxi[1]: # x 좌표 먼저 검사
            continue
        elif point[0] > maxi[0]:
            break
        else:
            answer.append(point)
            
    
    return len(answer)


'''
'''
def solution(n):
    
    door = [1] * n
    
    for i in range(2, n + 1): # n - 1 번 반복  / 첫 번째 문 여는 행위 없이
        # i 는 배수 2, 3, 4 ... n
        for k in range(i - 1, n, i): # 이 부분은 인덱스
            if door[k] == 0:
                door[k] = 1
            else:
                door[k] = 0
    
    
    return len([i for i in door if i == 1])
'''

'''
# 약수의 개수 구하기
def num_of_cd(n):
    cds = []
    for i in range(2, n+1):
        if n % i == 0:
            cds.append(i)
    return len(cds)

def solution(n):
    answer = 1 # 첫 번쨰 문은 무조건 열려있다.
    for i in range(2, n + 1):
        if num_of_cd(i) % 2 == 0: # 약수의 개수가 짝수면
            answer += 1
    return answer
        
    
'''

'''
import datetime

def solution(p,n):
    
    time_split = p.split(' ')
    unit = time_split[0]
    real_time = time_split[1]
    
    _time = real_time.split(':') # 시간 문자열 리스트
    if unit == 'PM':
        if _time[0] != '12':
            hour = int(_time[0]) + 12
            _time[0] = str(hour)
            real_time = ':'.join(_time)
        else:
            _time[0] = '00'
        
    
    
    
    time = datetime.datetime.strptime(real_time, '%H:%M:%S')
    time += datetime.timedelta(seconds=n)
    
    return str(time).split(' ')[1]



solution('AM 11:27:35', 16000)

'''
pascal = dict()
    
for n in range(4):
    pascal[n, 0] = 1
    pascal[n, n] = 1
        
    for k in range(1, n):
        pascal[n, k] = pascal[n - 1, k - 1] + pascal[n - 1, k]
        
    

def solution(r, c):
    
    #파스칼 삼각형 구현
    
    maxi = max(r, c)
    
    pascal = dict()
    
    for n in range(maxi):
        pascal[n, 0] = 1
        pascal[0, n] = 1
        
        for k in range(1, n):
            pascal[n, k] = pascal[n - 1, k - 1] + pascal[n - 1, k]
            
            print(pascal[n, k])
    return pascal[r-1, c-1]




