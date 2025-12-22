class Mycontainer:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def remove(self, item):
        if item in self.data:
            self.data.remove(item)
        else:
            print("Item not found")

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]


c = Mycontainer()

c.add(2)
c.add(4)
c.add(5)

print(len(c)) #c.__len__()
print(c[1]) #c.__getitem__(1)

c.remove(20)
print(c.data)
