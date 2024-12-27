class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def construct(self, arr):
        node = Node(arr[0])  # create head node
        temp = node
        for i in arr[1:]:  # loops starts from 1st index of given array
            new_node = Node(i)  # create new node which includes the value from arr
            temp.next = new_node  # connect the new node to previous node
            temp = temp.next  # move to new node
        return node  # return head node
