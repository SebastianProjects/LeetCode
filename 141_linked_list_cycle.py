class Solution(object):
    def hasCycle(self, head):
        fastPointer = head
        slowPointer = head
        while fastPointer != None and fastPointer.next != None:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer == slowPointer:
                return True
        return False