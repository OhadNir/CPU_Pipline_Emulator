# co_project
Computer Organization Group Project

Meeting 1 Notes:

Build non-forwarding first!

Classes:

Instruction - R type, I type. With appropriate fields ?. List of 16 strings initalized to ".". Update each cycle index when updating pipeline

Members: Op, Rd, Rs, Rt


List for instructions in I-Type ?

Control - Track forwarding, 

PipeReg - IF/ID, ID/EX, EX/MEM, MEM/WB. Booleans for input and output being open, variables for RD, RS, RT.

Global dictionary for register data. All registers are available

For running actual operations, run the operation once the instruction hits WB stage and store back in dictionary

Global cyclecount tracker used for looping and history tracking, start at 0

Global max cyclecount=16

Global pipeline list that holds the instructions that are being printed with global integer that tracks max instruction index

main: Increment cyclecount -> Update pipeline -> Print pipeline -> Run operation in WB -> Print register data

ALU function:

Parameter is instruction object

Hardcode decoding funciton

First reg writeback, second reg first operand, third reg last operand


Insert nop's while running


Workload before Break:

Jesse - ALU

Xavier - Instruction class and file parsing

Ayannah - Learning Python and implement PipeReg

Ohad - Set up globals and skeleton/pseudocode main
