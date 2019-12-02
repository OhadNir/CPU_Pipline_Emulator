def ALU(instr):
    if type(instr) is not Instruction:
        raise Exception ("The variable being passed into the ALU is not an instruction!")

    first=0
    second=0
    if instr.RS=="$zero":
        first=0
    elif instr.RS not in RegData:
        first=int(instr.RS)
    else:
        first=int(RegData[instr.RS])
    if instr.RT=="$zero":
        second=0
    elif instr.RT not in RegData:
        second=int(instr.RT)
    else:
        second=int(RegData[instr.RT])
    if instr.operation=="add" or instr.operation=="addi":
        RegData[instr.RD]=first+second
    elif instr.operation=="and" or instr.operation=="andi":
        RegData[instr.RD]=first&second
    elif instr.operation=="or" or instr.operation=="ori":
        RegData[instr.RD]=first|second
    elif instr.operation=="slt" or instr.operation=="slti":
        RegData[instr.RD]=int(first<second)
    elif instr.operation=="beq":
        RegData[instr.RD]=int(first==second)
    elif instr.operation=="bne":
        RegData[instr.RD]=int(first!=second)

    else:
        raise Exception ("The operation is not supported by the ALU")

if __name__=="__main__":
    global RegData
    RegData={"$s0":10, "$s1":15, "$s2":20}

    class Instruction:
        def __init__(self, opin, r1,r2,r3):
            self.operation=opin
            self.RD=r1
            self.RS=r2
            self.RT=r3


    ALU(Instruction("addi", "$s0", "$s1", "$s2"))
    print(RegData["$s0"])
