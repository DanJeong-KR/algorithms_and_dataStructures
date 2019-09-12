#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:48:24 2019

@author: changsicjung
"""

# 체육복 빌려주는 상황
# 체육복은 양 옆의 학생에게만 빌려줄 수 있음
# 전체 학생수 2 <= n <= 30
# 도난당한 학생의 번호 배열 lost, 1 <= lost.count <= n
# 여벌 가진 학생 번호 배욜 reverse, 1 <= reserve.count <= n
# 여벌 가진 학생이 도난 당했을 때는 빌려줄 수 없음
# return : 체육 수업을 들을 수 있는 학생의 최대값

# (3) n - len(lost) 가 answer 가 될 것
# (1) lost 에 있는 아이가 reserve에 있다면 일반 학생으로 바꾸기 (배열에서 지우기)
# (2) lost 에 있는 아이를 기준으로 작은 학생 껏 부터 빌림을 시도해서 빌리면 배열에서 지우기.

def solution(n, lost, reserve):
    if n < 2 or n > 30 or len(reserve) < 1 or len(reserve) > n or len(lost) < 1 or len(lost) > n :
        return -1
    
    # (1)
    for i in lost[:]: 
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            
    # (2)
    for i in lost[:]:
        if i - 1 in reserve:
            lost.remove(i)
            reserve.remove(i - 1)
        elif i + 1 in reserve:
            lost.remove(i)
            reserve.remove(i + 1)
            
    # (3)4
    answer = n - len(lost)
    
    print("lost is : ",lost," reserve is : ", reserve, " answer is : ", answer)
    return answer


solution(5, [2,4], [1,3,5])
solution(5, [2,4], [3])
solution(3, [3], [1])



# 인기 풀이

def solution2(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)