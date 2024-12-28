"""

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        """


class Solution:
    def getcount(self, head):
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count


# Input: LinkedList : 1->2->3->4->5

# Output: 5
# Explanation: Count of nodes in the linked list is 5, which is its length.
