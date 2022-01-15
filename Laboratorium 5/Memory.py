

class Memory:

    def __init__(self, name): # memory name
        self.memory = {}

    def has_key(self, name):
        return name in self.memory.keys()

    def get(self, name):
        return self.memory.get(name, None)

    def put(self, name, value):
        self.memory.update({name: value})

class MemoryStack:
                                                                             
    def __init__(self, memory=None):
        if memory is None:
            self.stack = [Memory("bla bla")]
        else:# initialize memory stack with memory <memory>
            self.stack = [memory]

    def get(self, name):             # gets from memory stack current value of variable <name>
        for m in self.stack:
            res = m.get(name)
            if res is not None:
                return res

    def insert(self, name, value): # inserts into memory stack variable <name> with value <value>
        self.stack[0].put(name, value)

    def set(self, name, value): # sets variable <name> to value <value>
        self.insert(name, value)

    def push(self, memory): # pushes memory <memory> onto the stack
        pass

    def pop(self):          # pops the top memory from the stack
        pass

