#Data structure implementation example
#Stack implementation

class Stack:
    def __init__(self, size):
        self.li = [None] * size
        self.cap = size
        self.top = -1
 
#To append a element to the stack
    def push(self, element):
        if self.isFull():
            print("Stack is full.")
            return None
        else:
            print(f"{element} is inserted.")
            self.top += 1
            self.li[-1] = element
 
#To pop the top element
    def pop(self):
        if self.isEmpty():
            print("Stack is empty.")
            return None
        else:
            print("Element is removed.")
            top = self.li[-1]
            self.top -= 1
            return top
 
#To see the top element
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.li[-1]
 
#To see the size of the stack
    def size(self):
        return self.top + 1
 
#To see if the stack is empty
    def isEmpty(self):
        return self.size() == 0
 
#To see if the stack is full
    def isFull(self):
        return self.size() == self.cap

stackExample = Stack(4) #The size of the "stackExample" is 4.

#Adding elements to the stack
stackExample.push("a")
stackExample.push("b")
stackExample.push("c")

#Checking if it is full or not
print(stackExample.isFull())

#Adding one more element to the stack
stackExample.push("d")

#Checking the top element of the stack
stackExample.peek()

#Checking if it is full or not again
print(stackExample.isFull())

#Popping a element from the stack
stackExample.pop()

#Checking if it is empty or not
print(stackExample.isEmpty())

#Checking the top element of the stack
stackExample.peek()

#Popping all the elements from the stack
stackExample.pop()
stackExample.pop()
stackExample.pop()

#Checking the stack if it is empty or not again
print(stackExample.isEmpty())

















