//
//  main.swift
//  naver_test
//
//  Created by Sicc on 16/09/2019.
//  Copyright © 2019 chang sic jung. All rights reserved.
//

import Foundation

//public func solution(_ A : inout [Int]) -> Int {
//  // write your code in Swift 4.2.1 (Linux)
//
//  var newList = [Int]()
//
//  var idx: Int = 0
//  while A[idx] != -1 {
//    newList.append(A[idx])
//    idx = A[idx]
//  }
//  newList.append(A[idx])
//
//  return newList.count
//
//}


public func solution(_ S : inout String) -> String {
  // write your code in Swift 4.2.1 (Linux)

  let ignoreStrs = ["-" , "/", " "]

  var result = S
  ignoreStrs.forEach {
    let temp = result.split(separator: Character($0))
    result = temp.joined()
  }

  // 3개씩 담기
  var newArr: [String] = []
  var brace = ""
  for (idx, s) in result.enumerated() {
    brace += String(s)
    if idx % 3 == 2 {
      newArr.append(brace)
      brace = "" // 초기화
    }
  }
  newArr.append(brace)

  // 마지막 두 칸이 나눠지는 경우 에외 처리, 숫자 두자리 이상 주어지므로 첫째칸 신경 안씀
  if result.count % 3 == 1 {
    let lastIdx = newArr.count - 1
    let firstChar = String(newArr[lastIdx - 1].popLast()!)
    newArr[lastIdx] = firstChar + newArr[lastIdx]
  }

  result = newArr.joined(separator: "-")

  // 마지막 - 올 수 있는 경우예외 처리
  if result.last! == "-" {
    result.removeLast()
  }
  return result
}


//public func solution(_ S : inout String) -> Int {
//
//  var result: [String] = []
//
//  let firTest = S.split(separator: "?")
//  print("firstTest : \(firTest)")
//
//  var secTest: [String] = []
//
//  for i in firTest {
//    if i.contains(".") {
//      (i.split(separator: ".")).forEach { secTest.append(String($0)) }
//    } else {
//      secTest.append(String(i))
//    }
//  }
//
//  for i in secTest {
//    if i.contains("!") {
//      (i.split(separator: "!")).forEach { result.append(String($0)) }
//    }else {
//      result.append(String(i))
//    }
//  }
//
//  let wordCountArr = result.map {
//    $0.split(separator: " ").count
//  }
//  return wordCountArr.sorted().last!
//}


