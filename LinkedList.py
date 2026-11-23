# Node class
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Delete by value
    def delete(self, key):

        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None

        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Element Not Found")
            return

        prev.next = temp.next

    # Display
    def display(self):

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program

ll = LinkedList()

ll.insert_begin(20)
ll.insert_begin(10)
ll.insert_end(30)
ll.insert_end(40)

print("Linked List:")
ll.display()

ll.delete(30)

print("After Deletion:")
ll.display()
