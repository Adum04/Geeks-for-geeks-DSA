class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def insertatend(self, head, x):
        node = Node(x)
        if head is None:  # if head is none
            head = node  # then head is node
            return head
        else:
            temp = head  # if head is given then we have to traverse the list
            while temp.next is not None:
                temp = temp.next  # traverse the list
            temp.next = node  # when list is traversed then add node at the end
        return head  # return the head
