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
    JZ = 15  # r0 为真跳转
    JNZ = 16  # r0 为假跳转
    CALL = 17
    RET = 18
    PUSH = 19
    ESC = 20
    PRINT = 21


PC, ESP, EBP, R1, R2, R3, R4, R5 = {0, 1, 2, 3, 4, 5, 6, 7}


class Vm(object):
    def __init__(self):
        self.code = [None] * 9900  # 代码区从 100 开始 到 9999
        self.data = [None] * 10000  # 数据区从 10000 到 19999
        self.call_frame = [None] * 10000  # 调用栈帧 从 20000 29999

        self.register = [None] * 8
        self.register[PC] = 100

        self.code[9899] = Code(Instruction.RET)
        self.call_frame[0] = 0
        self.call_frame[1] = 9899

    def exc(self):
        while True:
            code = self.code[self.register[PC] - 100]
            print("指令：%s" % code)
            if code.op is Instruction.MOV:
                self.register[code.data[1]] = self.data[code.data[0] - 10000].value
            elif code.op is Instruction.ADD:
                self.register[code.data[0]] = self.register[code.data[0]] + self.register[code.data[1]]
            elif code.op is Instruction.SUB:
                pass
            elif code.op is Instruction.MUL:
                pass
            elif code.op is Instruction.DIV:
                pass
            elif code.op is Instruction.MOD:
                pass
            elif code.op is Instruction.OR:
                pass
            elif code.op is Instruction.XOR:
                pass
            elif code.op is Instruction.AND:
                pass
            elif code.op is Instruction.EQ:
                pass
            elif code.op is Instruction.NE:
                pass
            elif code.op is Instruction.LT:
                pass
            elif code.op is Instruction.GT:
                pass
            elif code.op is Instruction.LE:
                pass
            elif code.op is Instruction.GE:
                pass
            elif code.op is Instruction.JZ:
                pass
            elif code.op is Instruction.JNZ:
                pass
            elif code.op is Instruction.CALL:
                pass
            elif code.op is Instruction.RET:
                pass
            elif code.op is Instruction.PUSH:
                pass
            elif code.op is Instruction.PRINT:
                print("程序打印：%s" % self.register[R1])
            elif code.op is Instruction.ESC:
                print("程序退出！")
                return
            else:
                print("指令错误")
            self.register[PC] = self.register[PC] + 1


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
