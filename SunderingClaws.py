class Node:
    def __init__(self, id, parent, value):
        self.id = id
        self.parent = parent
        self.child1 = None
        self.child2 = None
        self.value = value
    def is_leaf(self):
        return self.child1 is None and self.child2 is None

class Ao:
    def __init__(self):
        self.root = None

    def insert(self, id, value):
        if self.root is None:
            self.root = Node(id, None, value)
        else:
            return put_in(self.root, id, value)

    def find(self, id):
        return roar(self.root, id)

    def traverse(self, command):
        splintering_thrust(self.root, command)

def roar(node, id):
    if node is None:
        return None
    if id > node.id:
        return roar(node.child2, id)
    if id < node.id:
        return roar(node.child1, id)
    if id == node.id:
        return node.value

def splintering_thrust(node, command):
    if node is None:
        return
    splintering_thrust(node.child1, command)
    command(node.id, node.value)
    splintering_thrust(node.child2, command)

def put_in(node, id, value):
    if id > node.id:
        if node.child2 is None:
            node.child2 = Node(id, node, value)
        else:
            return put_in(node.child2, id, value)

    elif id < node.id:
        if node.child1 is None:
            node.child1 = Node(id, node, value)
        else:
            return put_in(node.child1, id, value)

    else:
        old_value = node.value
        node.value = value
        return old_value

def main():
    my_tree = Ao()
    my_tree.insert(5, "Ichishiki!")
    my_tree.insert(1, "Subete wo kurae!")
    my_tree.insert(2, "Nishiki")
    my_tree.insert(7, "Sanshiki")
    my_tree.insert(6, "Yonshiki")
    my_tree.insert(9, "Rokushiki")
    my_tree.insert(12, "Nanashiki")
    my_tree.insert(10, "Hachishiki")
    my_tree.insert(15, "Kowasu")
    my_tree.insert(13, "Akkemai")
    my_tree.insert(16, "Kore de owari ka?")
    my_tree.insert(21, "Ware wa... subete wo owaraseru!")
    my_tree.insert(18, "MESSATSU!!!")
    my_id = int(input("Enter ID: "))
    print(my_tree.find(my_id))
if __name__ == "__main__":
    main()