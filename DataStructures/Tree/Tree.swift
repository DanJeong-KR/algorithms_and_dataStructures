//
//  tree.swift
//  DataStructures
//
//  Created by Sicc on 06/10/2019.
//  Copyright © 2019 chang sic jung. All rights reserved.
//

import Foundation

public class TreeNode<T> {
  public var value: T
  public var children: [TreeNode] = []
  
  public init(_ value: T) {
    self.value = value
  }
  
  public func add(_ child: TreeNode) {
    children.append(child)
  }
  
  // 배열로 한번에 자식노드 추가하기
  public func add(_ childs: [TreeNode]) {
    children += childs
  }
  
  // 깊이 우선 탐색
  public func forEachDepthFirst(visit: ((TreeNode) -> Void)? = nil) {
    if let visit = visit {
      visit(self) // 매개변수에 자기자신의 인스턴스를 넣음으로써 이 함수를 사용할 때 $0로 내가 원하는 작업을 수행할 수 있게
    }else {
      print(value)
    }
    children.forEach {
      $0.forEachDepthFirst(visit: visit)
    }
  }
  
  // 레벨 순서 탐색
  // FIFO 이용. (성능을 위해서는 Queue 이용해야)
  public func forEachLevelOrder(visit: ((TreeNode) -> Void)? = nil) {
    if let visit = visit {
      visit(self) // 매개변수에 자기자신의 인스턴스를 넣음으로써 이 함수를 사용할 때 $0로 내가 원하는 작업을 수행할 수 있게
    }else {
      print(value)
    }
    
    var queue: [TreeNode] = []
    children.forEach { queue.append($0) }
    
    while !queue.isEmpty {
      let node = queue.removeFirst()
      if let visit = visit {
        visit(node)
      } else {
        print(node.value)
      }
      node.children.forEach { queue.append($0) }
    }
  }
}

// 특정 값인 노드 탐색하기
// 레벨 순서 탐색 방법 활용할 것.
extension TreeNode where T: Equatable {
  public func search(_ value: T) -> TreeNode? {

    var result: TreeNode?

    forEachLevelOrder { (node) in
      if node.value == value {
        result = node
      }
    }
    return result
  }
}
