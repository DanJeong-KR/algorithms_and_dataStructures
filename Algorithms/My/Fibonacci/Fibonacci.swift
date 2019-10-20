//
//  Fibonacci.swift
//  DataStructures
//
//  Created by Sicc on 20/10/2019.
//  Copyright © 2019 chang sic jung. All rights reserved.
//

import Foundation

// 반복문 O(N)
public func fibonacci_for(n: Int) -> Int {
  if n == 0 || n == 1 {
    return n
  }
  
  var result = 0
  var a = 0
  var b = 1
  
  for _ in 2...n {
    result = a + b
    a = b
    b = result
  }
  
  return result
}

// 재귀
// 종료조건 만들어야.
// O(2^N)
public func fibonacci_recur(n: Int) -> Int {
  // 종료조건
  if n == 0 || n == 1 {
    return n
  }
  return fibonacci_recur(n: n - 1) + fibonacci_recur(n: n - 2)
}


// 메모제이션
// 공간복잡도를 희생해서 시간복잡도를 높여보자.
// 공간의 max 는 100
// O(N)
var memo = Array(repeating: -1, count: 100)

public func fibonacci_memo(n: Int) -> Int {
  
  if n == 0 || n == 1 {
    memo[n] = n
  }
  
  if memo[n] != -1 { // memo에 값이 있으면.
    return memo[n]
  } else { // 값이 없으면
    memo[n] = fibonacci_memo(n: n - 1) + fibonacci_memo(n: n - 2)
    return memo[n]
  }
  
}
