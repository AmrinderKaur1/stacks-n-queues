# queue implementation using list

class Queue(object):
    def __init__(self):
        self.li = []

    def push(self, item):
        self.li.append(item)
        
    def delete(self):
        return self.li.pop(0)
    
    def peek(self):
        if len(self.li):
            return self.li[0]
        return None
    
    def isEmpty(self):
        return len(self.li) > 0
    
q1 = Queue()

print(q1.peek()) # returns None

q1.push(11)
print(q1.peek()) # returns 11

q1.push(21)
print(q1.peek()) # returns 11 

q1.push(31) 
print(q1.peek()) # returns 11

# stack is 11->21->31

# # delete everything one by one
print(q1.delete()) # returns 11
print(q1.peek()) # returns 21

print(q1.delete()) # returns 21
print(q1.peek()) # returns 31

print(q1.delete()) # returns 31
print(q1.peek()) # returns None


--------------------------------------
# USING LINKED LIST.

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue(object):
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        
    def push(self, val):
        # we add elements at the end in queue  
        if self.tail:
            # tail exists
            self.tail.next = val
            self.tail = self.tail.next
        else:
            self.head = self.tail = val
    
    def delete(self):
        # delete the head of the data structure
        # Null checks
        if self.isEmpty():
            return None
        
        data = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return data
        
    def peek(self):
        if self.head:
            return self.head.value
        return None
                
    def isEmpty(self):
        if not self.head:
            return True
        return False
    
e1 = Node(11)
e2 = Node(21)
e3 = Node(31)
e4 = Node(41)

q1 = Queue(e1)

q1.push(e1)
print(q1.peek()) # -> 11

q1.push(e2) # 11->21
print(q1.delete()) # -> 11
print(q1.peek()) # -> 21

q1.push(e3) # 21 -> 31
print(q1.peek()) # -> 21
print(q1.delete()) # -> 21

q1.push(e4) # 31 -> 41
print(q1.peek()) # -> 31
# queue resultant is: 31 -> 41
