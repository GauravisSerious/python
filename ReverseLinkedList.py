class Reverse(object):
    def __init__(self,head):
        prev= None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
