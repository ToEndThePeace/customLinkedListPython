
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return repr(self.value)

    def get_value(self):
        return self.value

    def set_next(self, nextNode):
        self.next = nextNode

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        pass
    
    def __str__(self):
        text = "====================>\n";
        text += "= List:\n"
        if self.is_empty():
            text += "= EMPTY\n"
        else:
            current = self.head
            while current is not None and current is not self.tail:
                text += f"= {current}\n"
                current = current.get_next()
            text += f"= {self.tail}\n"
        text += "======<\n";
        return text

    def is_empty(self):
        return True if self.head == None and self.tail == None else False

    def push(self, *values):
        """
        alter the tail node.next to point to new node
        change the list's tail prop to be the new node
        """
        for value in values:
            newNode = Node(value)
            if self.is_empty():
                self.head = newNode
                self.tail = newNode
                return
            self.tail.set_next(newNode)
            self.tail = newNode
        pass
    
    def pop(self):
        """
        iterate over the elements until you find the element whose .get_next() returns self.tail
        change that element to be the tail element
        """
        current = self.head
        while current is not None and current.get_next() is not self.tail:
            current = current.get_next()
        self.tail = current
        current.set_next(None)
        return current
    
    def shift(self):
        """
        the .get_next() of the head element is your new head
        """
        if self.is_empty():
            return
        self.head = self.head.get_next()

x = LinkedList()
x.push(5)
x.push(6)
x.push(7)
x.push(8)
print(x)
x.push("abcde")
print(x)
x.pop()
x.pop()
print(x)
x.shift()
print(x)
x.push(12)
x.push(13, 14, 15)
print(x)
x.push("a", 2, 3, "why tho")
print(x)