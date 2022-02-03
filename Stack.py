# stack implementation using list

class Stack(object):
    def __init__(self):
        self.li = []

    def push(self, item):
        self.li.append(item)
        
    def delete(self):
        return self.li.pop()
    
    def peek(self):
        if len(self.li):
            return self.li[-1]
        return None
    
    def isEmpty(self):
        return len(self.li) > 0
    
s1 = Stack()

print(s1.peek()) # returns None

s1.push(11)
print(s1.peek()) # returns 11

s1.push(21)
print(s1.peek()) # returns 21

s1.push(31) 
print(s1.peek()) # returns 31

# delete everything one by one
print(s1.delete()) # returns 31
print(s1.peek()) # returns 21

print(s1.delete()) # returns 21
print(s1.peek()) # returns 11

print(s1.delete()) # returns 11
print(s1.peek()) # returns None

--------------------------------------------------
# stack implementation using linked list

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack(object):
    def __init__(self, head=None):
        self.head = head
        
    def push(self, val):
        # in stack, we add new elements to the top
        current = self.head
        self.head, self.head.next = val, current
    
    def delete(self):
        # returns the data of head and updates the head to next value
        # Null checks :
        if self.isEmpty():
            return None
        data = self.head.value
        self.head = self.head.next
        return data
        
    def peek(self):
        return self.head.value
                
    def isEmpty(self):
        if not self.head:
            return True
        return False
            
    
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)

s1 = Stack(e1)
s1.push(e1)
print(s1.peek()) # returns 1

s1.push(e2)
print(s1.peek()) # returns 2

print(s1.delete()) # returns 2 -> as the head node gets deleted
print(s1.peek()) # returns 1 -> as 1 is the head node now

s1.push(e3)
print(s1.peek()) # returns 3
