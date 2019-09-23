//
//  HyperConnect.swift
//  Algorithms_Swift
//
//  Created by Sicc on 23/09/2019.
//  Copyright © 2019 chang sic jung. All rights reserved.
//

import Foundation

/*
func solution(_ win_lose:[Int]) -> Int{
  var maxWin = 0
  var currentWin = 0
  for (idx, value) in win_lose.enumerated() {
    if value == 0 || idx == win_lose.count - 1 {
      maxWin = currentWin > maxWin ? currentWin : maxWin
      currentWin = 0
    } else {
      currentWin += 1
    }
  }
  return maxWin
}
*/

/// 리팩토링

func solution(_ n:Int) -> String
{
  var n = n
  var flag = false
  if n < 0 {
    n = abs(n)
    flag = true
  }
  
  if n == 1 || n == 0 || n == -1 { return String(n) }
  
  var result = 0
  var a = 0
  var b = 1
  
  for _ in 2...n {
    result = a + b
    // 여기부터 다음 반복의 값이 변하는 부분.
    a = b
    b = result
  }
  
  if flag && n % 2 == 0 {
    return String(-result)
  }else {
    return String(result)
  }
}



// 예외 처리 체크
// 리팩토링
/*
func solution(_ board:[[Int]]) -> Int{
  
  // 행과 열의 크기가 다르다면 수정해야함.
  var record = Array(repeating: 0, count: board[0].count)
  
  var maxLength: Int = 0
  for i in board {
    for (idx, value) in i.enumerated() {
      switch value {
      case 0:
        record[idx] = 0 // 0 으로 초기화
      case 1:
        record[idx] += 1
      default:
        break
      }
    }
    
    let goalLength: Int = maxLength + 1
    var current = 0
    for i in record {
      if i >= goalLength {
        current += 1
      }else {
        current = 0
      }
      if current == goalLength {
        maxLength += 1
        break
      }
    }
  }
  
  
  return maxLength == 0 ? 0 : Int(maxLength * maxLength)
}

 
*/

