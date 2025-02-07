class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detect_and_remove_cycle(head):
    slow = fast = head

    # Step 1: Detect cycle using Floyd's algorithm
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        # No cycle detected
        return False

    # Step 2: Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Step 3: Remove the cycle
    cycle_start = slow
    current = cycle_start
    while current.next != cycle_start:
        current = current.next
    current.next = None  # Remove the cycle

    return True

# Example usage:
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next  # Creates a cycle

if detect_and_remove_cycle(head):
    print("Cycle was detected and removed.")
else:
    print("No cycle found.")

