global register_data, cycle_count, max_cycle_count, pipeline
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
pipeline = list()
cycle_count = 0
max_cycle_count = 16
max_instruction_index = 0

def read_file():
    #reads input file
    return "inst"

def make_pipeline():
    #reads input file
    input_file = read_file()
    for instruction in input_file:
        #convert insuction strings into instruction class objects.
        #then
        pipeline.append(instruction)

    return

def print_pipeline():
    return

def print_register():
    return
    
if __name__ == '__main__':

    '''
    
    for cycle_count in range(len(max_cycle_count)):
        update pipeline
        print_pipeline()
        update registers 
        print_registers()
        max_instruction_index++
    

    '''