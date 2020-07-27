from enum import Enum


class Instruction(Enum):
    MOV = 0
    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    MOD = 5
    OR = 6
    XOR = 7
    AND = 8
    EQ = 9
    NE = 10
    LT = 11
    GT = 12
    LE = 13
    GE = 14
    JZ = 15   # r0 为真跳转
    JNZ = 16  # r0 为假跳转
    CALL = 17
    RET = 18
    PUSH = 19
    ESC = 20


class Vm(object):
    def __init__(self):
        self.code = [None] * 9900  # 代码区从 100 开始 到 9999
        self.data = [None] * 10000  # 数据区从 10000 到 19999
        self.call_frame = [None] * 10000  # 调用栈帧 从 20000 29999
        self.pc = 100  # 地址为 0
        self.esp = 2  # 地址为 1
        self.ebp = 0   # 地址为 2
        self.r0 = 0
        self.r1 = 0
        self.r2 = 0
        self.r3 = 0

        self.code[9899] = Code(Instruction.RET)
        self.call_frame[0] = 0
        self.call_frame[1] = 9899

    def exc(self):
        while self.pc < 9999:
            print("指令：%s" % self.code[self.pc - 100])
            if self.code[self.pc - 100].op is Instruction.MOV:
                pass
            elif self.code[self.pc - 100].op is Instruction.ADD:
                pass
            elif self.code[self.pc - 100].op is Instruction.SUB:
                pass
            elif self.code[self.pc - 100].op is Instruction.MUL:
                pass
            elif self.code[self.pc - 100].op is Instruction.DIV:
                pass
            elif self.code[self.pc - 100].op is Instruction.MOD:
                pass
            elif self.code[self.pc - 100].op is Instruction.OR:
                pass
            elif self.code[self.pc - 100].op is Instruction.XOR:
                pass
            elif self.code[self.pc - 100].op is Instruction.AND:
                pass
            elif self.code[self.pc - 100].op is Instruction.EQ:
                pass
            elif self.code[self.pc - 100].op is Instruction.NE:
                pass
            elif self.code[self.pc - 100].op is Instruction.LT:
                pass
            elif self.code[self.pc - 100].op is Instruction.GT:
                pass
            elif self.code[self.pc - 100].op is Instruction.LE:
                pass
            elif self.code[self.pc - 100].op is Instruction.GE:
                pass
            elif self.code[self.pc - 100].op is Instruction.JZ:
                pass
            elif self.code[self.pc - 100].op is Instruction.JNZ:
                pass
            elif self.code[self.pc - 100].op is Instruction.CALL:
                pass
            elif self.code[self.pc - 100].op is Instruction.RET:
                pass
            elif self.code[self.pc - 100].op is Instruction.PUSH:
                pass
            elif self.code[self.pc - 100].op is Instruction.ESC:
                pass
            else:
                print("指令错误")
            self.pc = self.pc + 1


class Code(object):
    def __init__(self, op, *data):
        self.op = op
        self.data = []
        for tmp in data:
            self.data.append(tmp)

    def __str__(self):
        return 'code({op},{data})'.format(
            op=self.op,
            data=self.data
        )

    def __repr__(self):
        return self.__str__()


class Data(object):
    def __init__(self, type, name, value):
        self.type = type
        self.name = name
        self.value = value

    def __str__(self):
        return 'Data({type},{name},{value})'.format(
            type=self.type,
            name=self.name,
            value=self.value
        )

    def __repr__(self):
        return self.__str__()


dd = Data('int', 'lv', 5)
print(dd)

c1 = Code(Instruction.GE)
c2 = Code(Instruction.MOV, 1, 2)

vm = Vm()
vm.code[0] = c1
vm.code[1] = c2

vm.exc()

