
class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [[]]
        self.index = 0
        self.length = len(self.stacks)

    def __len__(self):
        return self.index + 1

    # adds an item to the stack
    def push(self, item):
        if len(self.stacks[self.index]) < self.capacity:
            print(len(self.stacks[self.index]))
            self.stacks[self.index].append(item)

        else:
            self.stacks.append([])
            self.add()
            self.stacks[self.index].append(item)

    # removes last item in stack
    def pop(self):
        if self.stacks[self.index] == 0:
            self.subtract()
        return self.stacks[self.index].pop()

    # removes item at an index
    def popAt(self, at_index):
        if self.stacks[at_index] == 0:
            self.subtract()
        if at_index > self.index:
            return 'that stack does not exist'
        else:
            return self.stacks[at_index].pop()

    def add(self):
        self.index += 1

    def subtract(self):
        self.index -= 1


stacks = SetOfStacks(2)


stacks.push(10)
stacks.push(9)
stacks.push(8)
stacks.push(7)
stacks.push(13)
stacks.push(27)


print(len(stacks))
print(stacks.popAt(0))
print(stacks.pop())
print(len(stacks))
print(f' stacks on stacks{stacks.stacks}')
