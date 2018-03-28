# Definition for singly-linked list.
import json
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        bac = res
        flag1 = False
        flag2 = False
        flag3 = False
        while l1 != None and l2 != None:
            flag3=False
            if l1.next == None:
                flag1 = True
            if l2.next == None:
                flag2 = True
            sum = l1.val + l2.val
            ben = sum % 10
            jin = int(sum / 10)
            ss = res.val + ben
            ben = ss % 10
            jin = int(ss / 10) + jin
            res.val = ben
            if l1.next == None or l2.next == None:
                if jin == 0:
                    if flag1 and flag2:
                        break
                    res.next = ListNode(jin)
                    break
            flag3 = True
            res.next = ListNode(jin)
            l1 = l1.next
            l2 = l2.next
            res = res.next
        if flag1 and flag2:
            return bac
        elif flag1:
            # l2 haiyou
            if not flag3:
                l2 = l2.next
                # res=res.next
                # res.next = ListNode(0)
                res = res.next
            while l2 != None:
                sum = l2.val + res.val
                ben = sum % 10
                jin = int(sum / 10)
                res.val = ben
                if l2.next == None:
                    if jin == 0:
                        break
                    else:
                        res.next = ListNode(jin)
                        break
                res.next = ListNode(jin)
                res = res.next
                l2 = l2.next
            return bac
        else:
            # l1 haiyou
            if not flag3:
                l1 = l1.next
                # res=res.next
                # res.next = ListNode(0)
                res = res.next
            while l1 != None:
                sum = l1.val + res.val
                ben = sum % 10
                jin = int(sum / 10)
                res.val = ben
                if l1.next == None:
                    if jin == 0:
                        break
                    else:
                        res.next = ListNode(jin)
                        break
                res.next = ListNode(jin)
                res = res.next
                l1 = l1.next
            return bac

l1=ListNode(1)
l1.next=ListNode(8)
l1.next.next=ListNode(3)
l2=ListNode(7)
l2.next=ListNode(1)
res=Solution.addTwoNumbers(None,l1,l2)
print(res.val)
print(res.next.val)
print(res.next.next.val)
