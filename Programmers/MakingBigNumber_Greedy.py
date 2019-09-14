#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 14:44:44 2019

@author: changsicjung
"""

'''
큰 수 만들기

어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다. 1 <= len(number) and len(number) <= 1000000
k는 1 이상 number의 자릿수 미만인 자연수입니다.  1 <= k and k < len(number)
k 가 자연수 이기 때문에 number 는 10 이상이다.
'''


'''
* (1)주어진 숫자로부터 하나씩 꺼내어 모은다,
    * (2)이미 모아둔 것 중 지금 등장한 것보다 작은 것들은 빼낸다.
    * (3)이미 모아둔 것들은 뒤에서 부터 우선순위로 살펴보아야 한다. (뒤에 수가 먼저 빠진다.)
    * (4) 중간에 다 찾았으면 나머지 탐색 안하고 뒤에 남아있는 것들 한번에 붙이기
* (5)아직 뺄 수 k 를 채우지 못한 경우 k 수만큼 뒤에 수를 뺸다.
* (6)모은 숫자들을 모두 붙인 뒤 반환한다.
'''

'''
* 무식 : 모든 경우의 수를 찾는 것.
* 우리 : O(N) (탐욕법이 통하기 때문에)
    * 앞 자리의 수를 결정할 때 큰 걸 앞에놓고 뒤는 처다보지 않아도, 앞에도 작은 게 나왔으면 앞에 나온게 k 개가 채워질 때까지 지워나가는 것이 마지막에 solution에 영향을 주지 않음
    * 모든 걸 다 돌아보지 않아도 됨.
'''

# 내 꺼.
def solution(number, k):
    
    result = []
    for idx, value in enumerate(number):
        result.append(value)
        if k != 0:
            for idx_result, value_result in enumerate(result[:-1].__reversed__()): # 우선순위 높은 아이 있는지  검사.
                if value > value_result: # 우선순위가 높은 아이를 찾았다면
                    result.remove(value_result) # result 에서 우선순위 낮은 애 없애기
                    k -= 1
                    if k == 0:
                        break
    else:# 반복이 끝났는데 k가 남아있다면
        if k != 0:
            for i in range(k):
                result.pop(-1)
            
    return ''.join(result)
            
            
## 강의 해답
def solution2(number, k):
    #(1)
    collected = []
    for i, num in enumerate(number):
        #(2)
        while len(collected) > 0 and collected[-1] < num and k > 0: # 문자열 대소관계는 사전관계 -> 한 문자 '1' 은 '2' 와 비교 됨
            collected.pop() #(3)
            k -= 1
        #(4)
        if k == 0:
            collected += list(number[i:])
            break # 가장 바깥의 for 루프 빠져나감.
        collected.append(num)
            
    #(5)
    collected = collected[:-k] if k > 0 else collected
    
    #(6)
    answer = ''.join(collected)
    return answer
        
        
            