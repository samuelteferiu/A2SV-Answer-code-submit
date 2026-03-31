# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curent=temp=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                curent.next=list1
                list1,curent=list1.next,list1
            else:
                curent.next=list2
                list2,curent=list2.next,list2
        if list1 or list2:
            curent.next =list1 if list1 else list2

        return temp.next
        