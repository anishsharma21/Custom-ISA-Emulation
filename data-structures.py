class Empty(Exception):
  pass

class ArrayStack:
  def __init__(self, capacity: int=1) -> None:
    self.values = [None] * capacity
    self.size = 0
    self.head = 0
    
  def is_empty(self):
    return self.size == 0

  def peek(self):
    if self.is_empty():
      raise Empty("ArrayStack is empty")
    return self.values[self.head]
    
arrstack: ArrayStack = ArrayStack(4)
print(arrstack.is_empty());

class ArrayQueue:
  pass

class Node:
  __slots__ = ("value", "next")
  
  def __init__(self, value: int=0, next=None) -> None:
    self.value = value
    self.next = next

class LinkedList:
  pass

class LinkedStack:
  pass

class LinkedQueue:
  pass

class HashTable:
  pass

class Set:
  pass

class Map:
  pass

class Deque:
  pass