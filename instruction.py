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
        
        #Populated Member vaiables
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