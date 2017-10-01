from queue import PriorityQueue

q = PriorityQueue()

q.put((10, "Mu 12"))
q.put((5, "Nu 13"))
q.put((8, "Lambda 11"))
q.put((3, "Assassin's Katana"))
q.put((9, "Assassin's Arashi"))
q.put((2, "Hunter's Darklance"))
q.put((4, "Hunter's Darkclaw"))
q.put((6, "Warlock's Disruptor"))
q.put((7, "Alien Psi Amp"))
q.put((1, "Avatar"))

while not q.empty():
    next = q.get()
    print(next)