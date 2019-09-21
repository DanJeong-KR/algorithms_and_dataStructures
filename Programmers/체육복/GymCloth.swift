//
//  GymCloth.swift
//  Algorithms_Swift
//
//  Created by Sicc on 22/09/2019.
//  Copyright © 2019 chang sic jung. All rights reserved.
//

import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
  
  var uniform = Array(repeating: 1, count: n + 2)
  
  reserve.forEach { uniform[$0] += 1 }
  lost.forEach { uniform[$0] -= 1 }
  
  for i in 1...n {
    if uniform[i] == 2 {
      if uniform[i - 1] == 0 {
        uniform[i - 1] = 1
        uniform[i] = 1
      }else if uniform[i + 1] == 0 {
        uniform[i + 1] = 1
        uniform[i] = 1
      } else {
        continue
      }
    }
  }
  let lastIdx = uniform.count - 1
  
  return uniform[1..<lastIdx].filter { $0 > 0 }.count
}
