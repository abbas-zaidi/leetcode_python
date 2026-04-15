# Given a reference of type ListNode which is the head of a singly linked list, 
# write a function to determine if the linked list is a palindrome.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """Singly Linked List implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    # ---------- Insertion Operations ----------
    
    def append(self, data):
        """Add node at the end of the list"""
        new_node = ListNode(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def display(self):
        """Print the linked list"""
        if self.head is None:
            print("Empty List")
            return
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.value))
            current = current.next
        
        print(" -> ".join(elements))

def isPalindrome(head:ListNode):
    
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    print("slow value = ",slow.value)
    print("fast value = ",fast.value if fast else "None")
    
    cur = slow
    prev= None

    while cur:
        next_ = cur.next
        cur.next = prev
        prev = cur
        cur = next_
    
    left = head 
    right = prev

    while right:
        if left.value != right.value:
            return False
        else:
            left = left.next
            right = right.next
    return True

def _display(head:ListNode):
    """Print the linked list"""
    if head is None:
        print("Empty List")
        return
    
    elements = []
    current = head
    while current:
        elements.append(str(current.value))
        current = current.next
    
    print(" -> ".join(elements))


# Create a new linked list
ll = LinkedList()
print("\n1. Created empty list:")
ll.display()


# Append elements
print("\n2. Appending 10, 20, 30:")
ll.append(10)
ll.append(20)
# ll.append(30)
ll.append(20)
ll.append(10)
ll.display()
print(isPalindrome(ll.head))


  