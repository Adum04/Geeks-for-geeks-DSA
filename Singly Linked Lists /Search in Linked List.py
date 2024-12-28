""" Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
"""


class Solution:
    def searchKey(self, n, head, key):
        temp = head
        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
        return False
