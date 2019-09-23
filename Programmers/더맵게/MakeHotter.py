#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 23:46:48 2019

@author: changsicjung
"""


'''
더 맵게
문제 url : https://programmers.co.kr/learn/courses/9877/lessons/55750 
'''

'''
실패 
1 . 스코빌 지수가 모두 0일 때
2. 모두 섞었지만 k 를 넘지 않을 때
'''
import heapq as h

def solution(scoville, K):
    
    # 리스트를 힙으로 만들구
    h.heapify(scoville)
    
    # scoville 이 모두 0 인지 체크
    for i in scoville:
        if i != 0:
            break
    else:
        return -1
    
    # 음식 섞는 과정
    count = 0
    while scoville[0] < K and len(scoville) >= 2:
        firstHot = h.heappop(scoville)
        secondHot = h.heappop(scoville)
        new = firstHot + secondHot * 2
        h.heappush(scoville, new)
        count += 1
        
    if scoville[0] < K:
        return -1
    
    return count