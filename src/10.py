import fileinput


class Bot:
    def __init__(self, n):
        self.n = n
        self.values = []

    def append(self, number):
        self.values.append(number)
        assert(len(self.values) <= 2)

    def low(self):
        return min(self.values)

    def high(self):
        return max(self.values)

    def has_two(self):
        if(sorted(self.values) == [17, 61]):
            print(self.n)
        return len(self.values) == 2

    def clear(self):
        self.values = []

    def __repr__(self):
        return str((self.n, sorted(self.values)))


def parse(words):
    word = words[0]
    if word =='value':
        return (int(words[1]),int(words[5]))
    return (int(words[1]), (words[5], int(words[6])), (words[10], int(words[11])))


def solve(instructions):
    insts = instructions
    bots = {}
    outs = {}
    while insts:
        next_insts = []
        for inst in insts:
            apply(inst, bots, outs, next_insts)
        insts = next_insts
    print(outs[0][0]*outs[1][0]*outs[2][0])


def apply(inst, bots, outs, next_insts):
    if 2 == len(inst):
        n = inst[1]
        dst = bots.setdefault(n, Bot(n))
        if not dst.has_two():
            dst.append(inst[0])
        else:
            next_insts.append(inst)
    elif 3 == len(inst):
        n = inst[0]
        src = bots.setdefault(n, Bot(n))
        if src.has_two():
            low_dst_inst = inst[1]
            if low_dst_inst[0] == 'bot':
                n_low = low_dst_inst[1]
                low_dst = bots.setdefault(n_low, Bot(n_low))
            else:
                low_dst = outs.setdefault(low_dst_inst[1], [])
            low_dst.append(src.low())

            high_dst_inst = inst[2]
            n_high = high_dst_inst[1]
            if high_dst_inst[0] == 'bot':
                high_dst = bots.setdefault(n_high, Bot(n_high))
            else:
                high_dst = outs.setdefault(n_high, [])
            high_dst.append(src.high())

            src.clear()
        else:
            next_insts.append(inst)


instructions = [parse(line.strip().split()) for line in fileinput.input()]
solve(instructions)
