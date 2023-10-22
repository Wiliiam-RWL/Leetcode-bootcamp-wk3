# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def allDone(self, lists: List[Optional[ListNode]]):
        for h in lists:
            if h is not None:
                return False
        return True

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode()
        res_head = res
        heads = []
        for h in lists:
            heads.append(h)
        while self.allDone(heads) == False:
            min_head = None
            min_index = 0
            for i in range(len(heads)):
                if heads[i] is not None and (min_head is None or heads[i].val < min_head.val):
                    min_head = heads[i]
                    min_index = i
            res_head.next = ListNode(min_head.val, None)
            res_head = res_head.next
            heads[min_index] = heads[min_index].next
        return res.next