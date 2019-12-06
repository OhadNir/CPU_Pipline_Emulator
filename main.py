from FuncCode import ALU
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
pipeline_registers = list()
pipeline_history = list()
all_instructions = list()

cycle_count = 0
max_cycle_count = 16
next_instruction_index = -1

def read_file():
    #reads input file
    return "inst"

def make_pipeline():
    #reads input file
    input_file = read_file()
    for instruction in input_file:
        #convert insuction strings into instruction class objects.
        #then
        all_instructions.append(instruction)

    return

def make_pipereg():
    return

def print_pipeline():
    return

def print_register():
    return
    
if __name__ == '__main__':

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