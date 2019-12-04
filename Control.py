'''
Create the Control class:
Deal with hazards
Forwarding
Branch handling
'''

class Control(object):
    def __init__(self, ForwardStatus):
        self.DataHazardFlag=False
        self.ControlHazardFlag=False
        self.forwardFlag=ForwardStatus
        self.forwardA=False
        self.forwardB=False
        self.BranchDestination=None

    def checkDataHazards(self):
        IFID=0
        IDEX=1
        EXMEM=2
        MEMWB=3
        EXHazard=False
        if pipeline_registers[EXMEM].input.RD==pipeline_registers[IDEX].input.RS:
            self.DataHazardFlag=True
            self.ForwardA=10
            EXHazard=True
        if pipeline_registers[EXMEM].input.RD==pipeline_registers[IDEX].input.RT:
            self.DataHazardFlag=True
            self.ForwardB=10
            EXHazard=True
        if (not EXHazard) and (pipeline_registers[MEMWB].input.RD==pipeline_registers[IDEX].input.RS):
            self.DataHazardFlag=True
            self.ForwardA=01
        if (not EXHazard) and (pipeline_registers[MEMWB].input.RD==pipeline_registers[IDEX].input.RT):
            self.DataHazrdFlag=True
            self.ForwardB=01

    def BranchValue():
        instr=pipeline_registers[MEMWB].ouput
        if instr.operation=="beq" && instr.RS==instr.RT:
            return labelDictionary[isntr.RD]
        if instr.operation=="bne" && instr.RS!=instr.RT:
            return labelDictionary[instr.RD]
        return -1

    def CheckBranch():
        instr=pipeline_registers[MEMWB].output
        cases=["beq", "bne"]
        if instr.operation in cases:
            return self.BranchValue():
        return -1
