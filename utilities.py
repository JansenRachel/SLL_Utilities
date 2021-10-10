class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def printVals(self):
        runner = self.head
        while runner != None:
            print(runner.data)
            runner = runner.next
        return self

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

#   Add a method contains(value) to your SLL class, which is given a value as a parameter.  Return a boolean (true/false); true, if the list possesses a node that contains the provided value.
    def contains(self, value):
        runner = self.head
        while runner != None:
            if runner.data == value:
                return True
            runner = runner.next
        return False

#   Create a new SLL method length() that returns number of nodes in that list.
    def lenght(self):
        runner = self.head
        length = 0
        while (runner):
            length += 1
            runner = runner.next
        return length

#   Create display() that returns a string containing all list values. Build what you wish console.log(myList) did!
    def display(self, temp):
        if temp:
            self.display(temp.next)
            print(temp.data, end = ' ')
        else:
            return

#   Create a standalone function that locates the minimum value in a linked list, and moves that node to the front of the list. Return the new list, with all nodes still present, and all (except for the new head node) in their original order
    def moveMin(self):
        # current = self.head
        # min = self.head.data
        # while self.head != None:
        #     if min > self.head.data:
        #         min = self.head.data
        #     current = self.head.next
        

#    Create a standalone function that locates the maximum value in a linked list, and moves that node to the back of the list. Return the new list, with all nodes still present, and all in their original order except for the node you moved to the end of the singly linked list.
    def moveMax(self):
        return




sll =SLL()
sll.append(2)
sll.append(4)
sll.append(6)
sll.append(8)
sll.append(10)
sll.append(12)

sll.printVals()


if sll.contains(6):
    print("Yes")
else:
    print("No")

if sll.contains(5):
    print("Yes")
else:
    print("No")

print("length of list is", sll.lenght())
sll.display(sll.head)

# sll.moveMin()


