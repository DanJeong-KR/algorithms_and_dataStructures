//
//  Marathon.swift
//  Algorithms_Swift
//
//  Created by Sicc on 22/09/2019.
//  Copyright © 2019 chang sic jung. All rights reserved.
//

/// 문제 url : https://programmers.co.kr/learn/courses/30/lessons/42883

import Foundation

func solution(_ number:String, _ k:Int) -> String {
  
  var k = k
  var collected = Array<String>()
  
  for (idx, num) in number.enumerated() {
    while !collected.isEmpty && String(num) > collected.last! && k > 0 {
      collected.removeLast()
      k -= 1
    }
    
    if k == 0 {
      collected += number.map { String($0) }[idx...]
      break
    }
    collected.append(String(num))
  }
  
  let answer = k > 0 ? Array(collected[...(collected.count - k - 1)]) : collected
  
  return answer.joined()
}
