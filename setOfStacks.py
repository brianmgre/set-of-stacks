
class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [[]]
        self.length = 0

    def push(self, item):
        if self.stacks[self.length] < self.capacity:
            self.add()
            self.stacks[self.length].append(item)
        else:
            self.stacks.append([])
            self.add()
            self.stacks[self.length].append(item)

    def add(self):
        self.length += 1

    def subtract(self):
        self.length -= 1


stacks = SetOfStacks(3)

stacks.push(10)
stacks.push(9)
stacks.push(8)
stacks.push(7)

print(stacks.length)
print(stacks.popAt(0))
print(stacks.pop())
print(stacks.pop())
print(stacks.length)
