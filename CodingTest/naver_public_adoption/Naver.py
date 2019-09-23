#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:50:13 2019

@author: changsicjung
"""
'''
메일 시스템 만들기
'''
'''
def solution(record):
    
    temp = []
    per = []
    
    for i in record:
        if len(i.split(" ")) == 2:
            mail = i.split(" ")[1]
            temp.append(mail)
        else:
            if i == 'DELETE' and len(temp) != 0:
                temp.pop()
            else:
                per += temp
                temp = []
    
    
    return per

solution(["RECEIVE abcd@naver.com", "RECEIVE zzkn@naver.com", "DELETE", "RECEIVE qwerty@naver.com", "SAVE", "SAVE", "DELETE", "RECEIVE QwerTY@naver.com", "SAVE"])
'''


'''
연속되는 자연수들의 곱으로 만들어 지고 크기 순으로 나열된 수열
'''
'''
def solution(n):
    
    nums_two = []
    
    for i in range(1, n+1):
        nums_two.append(i * (i + 1))
    
    return nums[n - 1]
'''

'''
다익스트라 알고리즘 인 듯
'''
def solution(cook_times, order, k):
    
    node = dict()
    for idx, time in enumerate(cook_times):
        node[idx + 1] = [0, time, 0] # 이전 노드가 있는지 여부 / 요리시간 (ㅇ) / 다음 노드 번호.
        
    for i in order:
        node[i[0]][2] = i[2] # 다음 노드 번호 (ㅇ)
        node[i[2]][0] = 1 # 다음 노드에서 이전 노드가 있는지 
        
    for i in range(1, k):
        if node[i][0] == 0:
            current = i
            time = 0
            while node[current][2] != 0 and node[current][2] == k:
                current = node[i][2]
                time += node[i][1]
        else:
            continue
    
    return

solution([5, 30, 15, 30, 35, 20, 4], [[2, 4], [2, 5], [3, 4], [3, 5], [1, 6], [4, 6], [5, 6], [6, 7]], 6)