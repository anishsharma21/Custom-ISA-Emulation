class LinkedList:
  class Node:
    __slots__ = 'value, next'
    def __init__(self, value: int, next=None) -> None:
      self.value = value
      self.next = next
  
  def __init__(self, head: Node=None) -> None:
    self.head = head
  