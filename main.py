from FuncCode import ALU
from instruction import Instruction
global register_data, pipeline_registers, pipeline_history, all_instructions, cycle_count, max_cycle_count, next_instruction_index
register_data = {
        "$s0": 0,
        "$s1": 0,
        "$s2": 0,
        "$s3": 0,
        "$s4": 0,
        "$s5": 0,
        "$s6": 0,
        "$s7": 0,
        "$t0": 0,
        "$t1": 0,
        "$t2": 0,
        "$t3": 0,
        "$t4": 0,
        "$t5": 0,
        "$t6": 0,
        "$t7": 0,
        "$t8": 0,
        "$t9": 0
    } 
branch_labels = dict()
pipeline_registers = list()
pipeline_history = list()
all_instructions = list()

cycle_count = 0
max_cycle_count = 16
next_instruction_index = -1

def read_file():
    #reads input file
    return "inst"

def make_pipeline(filename):
    next_index = 1
    
    file = open(filename, 'r', encoding = "utf-8")
    for line in file:
        #HIT A LABEL (All labels end in ':')
        if line.strip()[-1] == ':': 
            branch_labels[line.strip()] = next_index
            continue
        
        all_instructions.append(Instruction(line.strip()))
        next_index += 1
    
    file.close()
    return

def make_pipereg():
    return

#I'm assuming this is the function to print the entire pipeline
def print_register():
    print("CPU Cycles ===>\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16")
    for instr in all_instructions:
        print(instr)
    
    print("")
    i = 0
    for reg in register_data.keys():
        if i == len(register_data.keys()) - 1:
            print(reg + " = " + str(register_data[reg]))
        elif i < 3:
            print(reg + " = " + str(register_data[reg]) + "\t", sep = "", end = "")
        else:
            print(reg + " = " + str(register_data[reg]), sep = "")

    print("-" * 82)
    return
    
if __name__ == '__main__':

    isForwarding = False
    print("START OF SIMULATION (" + "no" if isForwarding else "" + "forwarding)" )
    print("-" * 82)
    
    for cycle_count in range(len(max_cycle_count)):
        temp = control.CheckBranch()
        if temp != -1: 
            next_instruction_index = temp
        else:
            ALU(pipeline_registers[-1].output_instruction) #output_instruction is the current instruction in the wb pipreg object. Varable can chance based on chosen object varable.
            next_instruction_index+=1
            
        control.checkDataHazards()


        for index in reversed(range(len(pipeline_registers))):
            if pipeline_registers[index].input_instruction:
                pipeline_registers[index].output_instruction = pipeline_registers[index].input_instruction 
                pipeline_registers[index].input_instruction = None
                if index != len(pipeline_registers)-1:
                    pipeline_registers[index + 1].input_instruction = pipeline_registers[index].output_instruction

        if next_instruction_index != -1:
            pipeline_history.append(all_instructions[next_instruction_index])
            pipeline_registers[0].input_instruction = pipeline_history[-1]

        #update all registers after they moved to their new pipeline register



                
    '''
    
        update pipeline
        {
            pass mem/wb output to alu func
            check for hazerds from control
            move input and outputs for pipereg objects list
                if in input then move to output and set input to NULL
                if its input output set output to NULL
                call update instructions on instructions as they are moved.
        }
        print_pipeline()
        update registers 
        {
            done in ALU step
        }
        print_registers()
    

    '''