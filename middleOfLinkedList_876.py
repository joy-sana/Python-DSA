# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        temp = head
        count = 0
        while(temp):
            temp = temp.next
            count+=1

        if count == 1:
            return head        
        if (count ^ 1) == (count + 1):
            index = (count//2) + 1
        else:
            index = ((count + 1)//2)

        temp = head
        count = 1
        while(temp):
            temp = temp.next
            count+=1        
            if count == index:
                return temp

