//
//  main.swift
//  Algorithms_Swift
//
//  Created by Sicc on 21/09/2019.
//  Copyright © 2019 chang sic jung. All rights reserved.
//

import Foundation
func solution(_ n:Int, _ a:Int, _ b:Int) -> Int
{
  
  if a.haha == b.haha {
    return 1
  }
  var result = 1
  var a = a
  var b = b
  while true {
    a = a.haha
    b = b.haha
    result += 1
    if abs(a - b) == 1 && a.haha == b.haha {
      return result
    }
  }
}

extension Int {
  var haha: Int {
    return Int((self + 1) / 2)
  }
}

solution(8, 4, 7)
