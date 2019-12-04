# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 13:28:40 2019

@author: Xerox
Basic class for storing standardized instruction data
"""

#I'm not sure that we need this, so I'll prob just delete later
R_Types = ["add, and, or, slt"]

#"add $t0,$s2,$s3"

#Convert $zero to '0' when found
class Instruction(object):
    
    def __init__(self, instr_string):
        self.cycle_state = [] #Size of max cycles
        
        #Populated Member variables
        self.full_instr = instr_string
        
        split_instr = instr_string.split(" ")
        self.operation = split_instr[0]
        
        split_regs = split_instr[1].split(",")
        self.RD = split_regs[0]
        self.RS = split_regs[1]
        
        if(len(split_regs == 3)):
            self.RT = split_regs[2]
        else:
            self.RT = ""
        
        self.type = None

    def update(self, cycle):  # cycle is an int
        to_add = ""

        if self.full_instr == "nop":  # very rudimentary, will fix later. maybe we should implement a counter?
            temp = self.cycle_state[cycle_1]
            if temp == "ID" or temp == "EX" or temp == "MEM":
                to_add = "*"
        else:
            if cycle == 0 or self.cycle_state[cycle - 1] == ".":  # will cycles be passed in starting from 0 or 1?
                to_add = "IF"
            elif self.cycle_state[cycle - 1] == "IF":
                to_add = "ID"
            elif self.cycle_state[cycle - 1] == "ID":
                to_add = "EX"
            elif self.cycle_state[cycle - 1] == "EX":
                to_add = "MEM"
            elif self.cycle_state[cycle - 1] == "MEM":
                to_add = "WB"

        self.cycle_state[cycle] = to_add

    def make_nop(self):  # for when we push nops, the plan is to copy the instruction its based on and then nop it
        self.full_instr = "nop"
