class Priority:
    def __init__(self):
        self.head = None

    def push(self, key, value):
        pri_link = Link(key, value)
        if self.head is None:
            self.head = pri_link
        elif self.head.key > pri_link.key:
            pri_link.next = self.head
            self.head = pri_link
        else:
            rec_push(self.head, pri_link)

    def pop(self):
        chain = self.head
        if chain is None:
            return None
        self.head = chain.next
        return chain.value


class Link:
    def __init__(self, key, value):
        self.next = None
        self.value = value
        self.key = key

def rec_push(link_before, link_to_add):
    next = link_before.next
    if next is None:
        link_before.next = link_to_add
    elif next.key > link_to_add.key:
        link_before.next = link_to_add
        link_to_add.next = next
    else:
        rec_push(next, link_to_add)

def Main():
    link = Priority()
    link.push(2, "Gun")
    link.push(1, "Bullets")
    link.push(5, "Katana")
    print(link.pop())
    print(link.pop())
    print(link.pop())

Main()