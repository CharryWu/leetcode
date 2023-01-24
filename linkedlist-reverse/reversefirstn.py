successor = None
def reverseFirstN(head, n):
    nonlocal successor
    if n == 1:
        successor = head.next
        return head
    newhead = reverseFirstN(head.next, n-1)
    head.next.next = head
    head.next = successor
    return newhead