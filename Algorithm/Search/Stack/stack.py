

class Stack:
    
    def __init__(self, size):
        self.size = size
        self.top = -1 
        self.items = [None] *size

    def is_empty(self) :
        return True if (self.top == -1 ) else False

    def is_full(self) :
        return True if (self.size == self.top+1) else False
    
    def push(self, data) :
        if self.is_full() :
            raise Exception('가득참!')
        else :
            self.top += 1 
            self.items[self.top] = data

    def pop(self) :
        if self.is_empty() :
            raise Exception('stack is empty')
        else : 
            value = self.items[self.top]
            self.items[self.top] = None 
            self.top -= 1 
            return value

    def peek(self) :
        if self.is_empty() :
            raise Exception('stack is empty')
        else : 
            value = self.items[self.top]
            return value

    
        
my_stack = Stack(5)

my_stack.push(1)
my_stack.push(2)

my_stack.pop()
my_stack.push(2)
my_stack.push(3)

print(my_stack)