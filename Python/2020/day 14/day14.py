def part_1():
    with open('data.in', 'r') as f:
        memory = {} #address : value
        for line in f:
            # X: excvlusive of X
            # :X inclusive of X 
            if line[:4] == 'mask':
                bitmask = line[7:].strip()
            else:
                # for the memory locations
                address = line[line.index('[')+1:line.index(']')]
                decimal_value = int(line[line.index('=')+1:].strip())
                # convert value to 36 bit binary
                binary_val = '{:036b}'.format(decimal_value)
                # now apply the mask to the value
                masked_value = ''.join([bitmask[i] if bitmask[i] != 'X' else binary_val[i] for i in range(36)])
                # add the masked value to the memory
                memory[address] = masked_value
        #sum the values in the memmory
        memory_sum = sum([int(memory[key], 2) for key in memory])
        return memory_sum


def part_2():
    with open('data.in', 'r') as f:
        memory = {}
        for line in f:
            if line[:4] == 'mask':
                bitmask = line[7:].strip() 
            else:
                decimal_address = int(line[line.index('[')+1:line.index(']')])
                decimal_value = int(line[line.index('=')+1:].strip())
                binary_address = '{:036b}'.format(decimal_address)          
                masked_address = ''.join([binary_address[i] if bitmask[i] == '0' else bitmask[i] for i in range(36)]) 
                # address is masked but still has X's in. 'first stage' of masking complete
                # now work with floating bits to create correct addresses
                count = bitmask.count('X')
                # there are count amount of X's that need switching.
                # the f.b will have arrangements of 0 -> (2**count)-1 as you count up in binary
                # so with a count of 3. there will be 0 up to 7 in binary for the X's
                # giving 8 (2**count) arrangements
                #create all possible arrangements of the X's as 1's and 0's
                possible_floating_bit_arrangements = [[k for k in j] for j in [str(bin(i)[2:]).zfill(count) for i in range(2**count)]]
                # now get all possible mask values
                for arrangement in possible_floating_bit_arrangements:
                    # get new mask without X's
                    # by replacing X's with numbers
                    address = [arrangement.pop() if masked_address[i] == 'X' else masked_address[i] for i in range(36)]
                    # now add value to memory at correct location
                    memory[''.join(address)] = decimal_value
    memory_sum = sum([int(memory[key]) for key in memory])
    return memory_sum

print(part_1())
print(part_2())
