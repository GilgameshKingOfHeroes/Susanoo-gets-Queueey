class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        # something
        ouroboros_chain = Ouroboros(value)
        ouroboros_chain.next = self.head
        self.head = ouroboros_chain
    def pop(self):
        # return something
        chain = self.head
        if chain is None:
            return None
        self.head = chain.next
        return chain.value

class Ouroboros:
    def __init__(self, value):
        self.next = None
        self.value = value

def main():
    stack = Stack()
    stack.push(2)
    stack.push(4)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

main()