from utils import read_file

data = read_file(8)


class Interpreter:
    def __init__(self, instructions):
        self.pc = 0
        self.accumulator = 0
        self.instructions = instructions
        self.executed = set()

    def nop(self, _):
        self.pc += 1

    def acc(self, val):
        self.accumulator += val
        self.pc += 1

    def jmp(self, val):
        self.pc += val

    def execute(self, inst, val):
        self.executed.add(self.pc)
        getattr(self, inst)(val)

    def run(self):
        while True:
            if self.pc in self.executed:
                return 'busted', self.accumulator
            try:
                inst, val = self.instructions[self.pc].split(' ')
                self.execute(inst, int(val))
            except IndexError:
                return 'fixed', self.accumulator


def p1():
    i = Interpreter(data)
    return i.run()[1]


print('p1', p1())


def p2():
    jmps = [i for i, val in enumerate(data) if val.startswith('jmp')]
    for index in jmps:
        new_dataset = data.copy()
        new_dataset[index] = str.replace(new_dataset[index], 'jmp', 'nop')
        i = Interpreter(new_dataset)
        flag, acc = i.run()
        if flag == 'fixed':
            return acc


print('p2', p2())
