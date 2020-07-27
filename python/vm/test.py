from vm import *

d1 = Data('int', 'a1', 5)
d2 = Data('int', 'a2', 6)


c1 = Code(Instruction.MOV, 10000, R1)
c2 = Code(Instruction.MOV, 10001, R2)
c3 = Code(Instruction.ADD, R1, R2)
c4 = Code(Instruction.PRINT)
c5 = Code(Instruction.ESC)


vm = Vm()
vm.data[0] = d1
vm.data[1] = d2

vm.code[0] = c1
vm.code[1] = c2
vm.code[2] = c3
vm.code[3] = c4
vm.code[4] = c5

vm.exc()
