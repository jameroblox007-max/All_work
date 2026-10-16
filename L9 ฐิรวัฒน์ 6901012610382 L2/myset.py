class mySet:
    def __init__(self):
        self.items = []

    def show(self):
        print("Set:", self.items)

    def add(self, x):
        if x not in self.items:
            self.items.append(x)

    def remove(self, x):
        if x in self.items:
            self.items.remove(x)


class myBag:
    def __init__(self):
        self.items = []

    def show(self):
        print("Bag:", self.items)

    def add(self, x):
        self.items.append(x)

    def remove(self, x):
        if x in self.items:
            self.items.remove(x)


class myQueue:
    def __init__(self):
        self.items = []

    def show(self):
        print("Queue:", self.items)

    def add(self, x):
        self.items.append(x)

    def remove(self):
        if self.items:
            return self.items.pop(0)

s = mySet()
s.add(1); s.add(1); s.add(2)
s.show()          

b = myBag()
b.add(1); b.add(1); b.add("a")
b.show()          

q = myQueue()
q.add(1); q.add(2); q.add(3)
q.remove()
q.show()        