//
//  MaximumNumber.swift
//  Algorithms_Swift
//
//  Created by Sicc on 22/09/2019.
//  Copyright © 2019 chang sic jung. All rights reserved.
//

import Foundation

func solution(_ numbers:[Int]) -> String {
  
  let answer = numbers.sorted(by: comparator).map { String($0) }.reduce("") { $0 + $1 }
  
  return answer.first == "0" ? "0" : answer
}

func comparator(a: Int, b: Int) -> Bool {
  let _a = Int(String(a) + String(b))!
  let _b = Int(String(b) + String(a))!
  
  if _a >= _b {
    return true
  } else {
    return false
  }
}
