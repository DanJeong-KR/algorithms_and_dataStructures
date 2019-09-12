#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:38:52 2019

@author: changsicjung
"""


# 단 한명의 선수를 제외하고는 모든 선수가 마라톤을 완주했음
# 마라톤에 참여한 선수들의 이름 participant
# 완주한 선수들의 이름 completion
# return : 완주하지 못한 선수의 이름

# 1 <= len(participant) <= 100,000
# len(completion) = len(participant) - 1
# 참가자 이름은 1개 ~ 20개 사이의 알파멧 소문자
# 참가자 중에 동명이인이 있을 수 있다.

## solution
# (1) 완주자에 있는 이름이 참여자에 있으면 하나씩 지워나자. -> 시간복잡도 탈락
# (2) zip을 활용해보자. -> 시간 복잡도 통과.


def solution(participant, completion):
    
    if not (len(participant) >= 1 and len(participant) <= 100000):
        print('참여자의 수가 조건에 맞지 않습니다.')
        return 'error'
    elif len(completion) != len(participant) - 1:
        print('참여자와 완주자의 수가 조건에 맞지 않습니다. 완주자 수는 참여자 수 - 1')
        return 'error'
    
    # (1)
    """
    for i in completion: 
        if i in participant:
            participant.remove(i) 
    """
    
    # (2)
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    else:
        return participant[-1]
        

# 인기 풀이
        
def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
