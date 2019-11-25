global RegData
RegData={"$s0":10, "$s1":15, "$s2":20}

class Instruction:
    def __init__(self, opin, r1,r2,r3):
        self.op=opin
        self.rd=r1
        self.rs=r2
        self.rt=r3

def ALU(instr):
    if type(instr) is not Instruction:
        raise Exception ("The variable being passed into the ALU is not an instruction!")

    if instr.op=="add" or instr.op=="addi":
        RegData[instr.rd]=int(RegData[instr.rs])+int(RegData[instr.rt])
    elif instr.op=="and" or instr.op=="andi":
        RegData[instr.rd]=int(RegData[instr.rs])&int(RegData[instr.rt])
    elif instr.op=="or" or instr.op=="ori":
        RegData[instr.rd]=int(RegData[instr.rs])|int(RegData[instr.rt])
    elif instr.op=="slt" or instr.op=="slti":
        RegData[instr.rd]=int(int(RegData[instr.rs])<int(RegData[instr.rt]))
    elif instr.op=="beq":
        RegData[instr.rd]=int(int(RegData[instr.rs])==int(RegData[instr.rt]))
    elif instr.op=="bne":
        RegData[instr.rd]=int(int(RegData[instr.rs])!=int(RegData[isntr.rt]))

    else:
        raise Exception ("The operation is not supported by the ALU")


ALU(Instruction("sub", "$s0", "$s1", "$s2"))
print(RegData["$s0"])
