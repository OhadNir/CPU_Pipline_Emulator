# co_project
Computer Organization Group Project

Meeting 1 Notes:

Build non-forwarding first!

Classes:

Instruction - R type, I type. With appropriate fields ?. List of 16 strings initalized to ".". Update each cycle index when updating pipeline. Update function that takes string of current stage.

Members: Op, Rd, Rs, Rt


List for instructions in I-Type ?

Control - Track forwarding,

PipeReg - IF/ID, ID/EX, EX/MEM, MEM/WB. Instruction objects for input and output; NULL if open. String variables for input and output (e.g. "IF", "ID", "EX", etc.)

For update: Make sure output matches input for next is NULL. Look at the instruction you're trying to move and check if its next stage is open. If we're at the last instruction, we don't need to worry about IF/ID input being NULL. Once moved, set previous spots to NULL

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

Ayanna - Learning Python and implement PipeReg

Ohad - Set up globals and skeleton/pseudocode main



Phase 2 Workload (by Wednesday):

Xavier - File parsing and output printing

Ohad - Fill main (update pipeline - Including Control operations pseudocode; update registers)

Ayanna - NOP push (look at instruction that needs to delay, call insert. Instruction update function, PipeReg name variables

Jesse - Control class (hazard checks and handling, Forwarding, function to execute operation in EX, Branch handling)



Phase 3 Workload (by ): FIX UPDATE TO ACCOUNT FOR PIPELINE POSITION

Xavier - First round of debugging. Add functions to main.

Ohad - Finish main forwarding logic.

Ayanna - TBD.

Jesse - First round of debugging. 
