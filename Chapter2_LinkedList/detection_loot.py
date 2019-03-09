from LinkedList import LinkedList


def Solve(ll):
    fast = slow = ll.head
    while fast in fast.next:
        fast = fast.next.next
        slow=slow.next
        if(fast is slow):
            break
    slow=ll.head
    while(slow is not fast):
        fast=fast.next
        slow=slow.next

    return fast

