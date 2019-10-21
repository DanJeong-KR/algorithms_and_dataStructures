//
//  BinaryTree.swift
//  DataStructures
//
//  Created by Sicc on 21/10/2019.
//  Copyright © 2019 chang sic jung. All rights reserved.
//



import Foundation

public class BinaryNode<T> {
  public var value: T
  public var leftChild: BinaryNode?
  public var rightChild: BinaryNode?
  
  public init(_ value: T) {
    self.value = value
  }
  
  public func traverseInOrder(visit: ((T) -> Void)? = nil) {
    leftChild?.traverseInOrder(visit: visit)
    if let visit = visit {
      visit(value)
    }else{
      print(value)
    }
    rightChild?.traverseInOrder(visit: visit)
  }
  
  public func traversePreOrder(visit: ((T) -> Void)? = nil) {
    if let visit = visit {
      visit(value)
    }else{
      print(value)
    }
    leftChild?.traversePreOrder(visit: visit)
    rightChild?.traversePreOrder(visit: visit)
  }
  
  public func traversePostOrder(visit: ((T) -> Void)? = nil) {
    leftChild?.traversePreOrder(visit: visit)
    rightChild?.traversePreOrder(visit: visit)
    if let visit = visit {
      visit(value)
    }else{
      print(value)
    }
  }
}

extension BinaryNode: CustomStringConvertible {
  
  public var description: String {
    return diagram(for: self)
  }
  
  private func diagram(for node: BinaryNode?,
                       _ top: String = "",
                       _ root: String = "",
                       _ bottom: String = "") -> String {
    guard let node = node else {
      return root + "nil\n"
    }
    if node.leftChild == nil && node.rightChild == nil {
      return root + "\(node.value)\n"
    }
    return diagram(for: node.rightChild,
                   top + " ", top + "┌──", top + "│ ")
      + root + "\(node.value)\n"
      + diagram(for: node.leftChild,
                bottom + "│ ", bottom + "└──", bottom + " ")
  }
}
