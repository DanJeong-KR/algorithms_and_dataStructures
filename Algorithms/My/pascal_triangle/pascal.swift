//
//  pascal.swift
//  Algorithms_Swift
//
//  Created by Sicc on 22/09/2019.
//  Copyright © 2019 chang sic jung. All rights reserved.
//

import Foundation

func pascal(x: Int, y: Int) -> Int {
  if min(x, y) == 0 {
    return 1
  }
  
  let n = min(x, y) + max(x, y)
  
  var p = Dictionary<Two<Int, Int>, Int>()
  
  for i in 0..<(n+1) {
    p[Two(values: (i, 0))] = 1
    p[Two(values: (0, i))] = 1
    
    guard i >= 2 else {
      continue
    }
    for k in 1..<i {
      p[Two(values: (i - k, k))] = p[Two(values: (i - k, k - 1))]! + p[Two(values: (i - k - 1, k))]!
    }
  }
  
  return p[Two(values: (x, y))]!
}

struct Two<X: Hashable, Y: Hashable>: Hashable {
  // Hashable 채택을 위해선 Equtable을 만족해야함.
  static func == (lhs: Two<X, Y>, rhs: Two<X, Y>) -> Bool {
    return lhs.values == rhs.values
  }
  
  // Hash Value 만들기
  let values: (X, Y)
  
  func hash(into hasher: inout Hasher) {
    let (a, b) = values
    hasher.combine(a.hashValue &* 31 &+ b.hashValue)
  }
}




