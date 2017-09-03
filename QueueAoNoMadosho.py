from StackMe import Ouroboros

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def reaper_enqueue(self, value):
        add_chain = Ouroboros(value)
        if self.head is None:
            self.head = add_chain
        if self.tail is not None:
            add_chain.next = self.tail
        self.tail = add_chain



    def nightmare_dequeue(self):
        pull_chain = self.head
        if pull_chain is None:
            return None
        self.head = pull_chain.next
        if self.head is None:
            self.tail = None
        return pull_chain.value




def main():
    



main()