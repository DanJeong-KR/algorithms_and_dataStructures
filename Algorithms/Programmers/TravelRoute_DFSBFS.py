#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:17:15 2019

@author: changsicjung
"""
'''
여행경로

문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.

항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
입출력 예
tickets	return
[[ICN, JFK], [HND, IAD], [JFK, HND]]	 /  [ICN, JFK, HND, IAD]
[[ICN, SFO], [ICN, ATL], [SFO, ATL], [ATL, ICN], [ATL,SFO]]	/ [ICN, ATL, ICN, SFO, ATL, SFO]
입출력 예 설명
예제 #1

[ICN, JFK, HND, IAD] 순으로 방문할 수 있습니다.

예제 #2

[ICN, SFO, ATL, ICN, ATL, SFO] 순으로 방문할 수도 있지만 [ICN, ATL, ICN, SFO, ATL, SFO] 가 알파벳 순으로 앞섭니다.
'''


'''
배경지식
* 그래프
    * 정점, 간선
    * directed 그래프, undirected 그래프
* 스택
* 큐

* 깊이우선 탐색
* 너비우선 탐색

해결
* 한 붓 그리기 (문제에서 보장되어 있음)
* 시작 정점은 언제나 ICN
* 모든 정점 방문이 아니고, 모든 간선을 거쳐야 (언젠가 한 번 가야하는데, 그 순서를 결정하는 것)
* 한 정점에서 택할 수 있는 간선이 두 개 이상인 경우는 알파벳 순서

설계
* 재귀적인 성질을 가진 한붓 그리기 문제
* 재귀적인 성질을 가진 '그래프의 깊이 우선 탐색'을 응용하여 해결할 것
'''
test = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]

test.sort(key=lambda x: x[0] == 'ICN', reverse=True)

temp = []

for i in test:
    if i[0] == 'ICN':
        temp.append(i)
    else:
        break
if temp


    
    

def solution(tickets):
    answer = []
    return answer