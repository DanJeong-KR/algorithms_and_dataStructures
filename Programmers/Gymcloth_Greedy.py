#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:48:24 2019

@author: changsicjung
"""

'''
체육복

점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 
이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

입출력 예
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
입출력 예 설명
예제 #1
1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

예제 #2
3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.
'''

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
            
    # (3)
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


## 강의 풀이
    
# 방법 1 (n 이 작을 때)
def solution3(n, lost, reserve):
    uniform = [1] * (n + 2) # 체육복 모두 1로 초기화 하고 인덱스 맨 앞에, 맨 뒤에 여분의 하나씩 더 해서 리스트의 접근 쉽게 할 것.
    
    for i in reserve: # 빌려줄 수 있는 학생들
        uniform[i] += 1
    
    for i in lost: # 도난 당한 학생들 
        uniform[i] -= 1
        
    for i in range(1,n + 1): # 빌려주는 동작
        if uniform[i - 1] == 0 and uniform[i] == 2: # 왼쪽 학생 먼저 빌려줄지 확인하고
            uniform[i - 1:i + 1] = [1, 1]
        elif uniform[i] == 2 and uniform[i + 1] == 0: # 오른쪽 학생 빌려주질 확인
            uniform[i:i + 2] = [1, 1]
    
    return len([x for x in uniform[1:-1] if x > 0])
    

# 방법 2 (n 이 클 때) 집합 사용
def solution4(n, lost, reserve):
    s = set(lost) & set(reserve) # &는 교집합 / 여분도 있고 도난도 당한 애들 
    l = set(lost) - s # 실제로 체육복을 빌려야 하는 학생들
    r = set(reserve) - s # 실제로 빌려줄 수 있는 학생들
    
    for x in sorted(r): 
        if x - 1 in l:
            l.remove(x - 1)
        elif x + 1 in l:
            l.remove(x + 1)
    return n - len(l)
    
    



    
    
    