# parenthesis have top priority
# * and + have equal priority

#make recursive func?


def get_data():
    with open('data.in', 'r') as f:
        data = [l.strip() for l in f]
        return data


def find_parens(s):
    toret = {}
    pstack = []
    for i, c in enumerate(s):
        if c == '(':
            pstack.append(i)
        elif c == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret[pstack.pop()] = i

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))
    return toret


def solve(ex, p1): #recursive
    #expression = [str(i) for i in expression]
    if '(' in ex or ')' in ex:
        #print(ex)
        #find the outer most pair of parentheses
        brackets = find_parens(ex)
        obi = list(brackets.keys())[0]
        cbi = list(brackets.values())[0]
        sub_ex = ex[obi+1:cbi] #excludes brackers
        sub_val = solve(sub_ex, p1) #recursion
        le = [i for i in ex]
        #le[obi:cbi+1]#indices include brackets
        #new_ex = old ex up to brackets + sub val + old ex after brackers
        new_ex = []
        new_ex.extend(le[:obi])
        new_ex.append(str(sub_val))
        new_ex.extend(le[cbi+1:])
        new_ex  = ''.join(new_ex)
        #print(new_ex)
        ex = solve(new_ex, p1)
        #print(ex)     
    return solve_expression_p1(ex) if p1 else solve_expression_p2(ex)
        #parentheses be evaluated first, and replaces with their value        


def solve_expression_p1(ex):
    #solve an expression L -> R if it has not parentheses
    #print(f'SOLVING {ex}')
    try:
        int(ex)
    except ValueError:
        le = ex.split(' ')
        total = int(le.pop(0))
        while len(le) > 0 :
            oper = str(le.pop(0))
            num = int(le.pop(0))
            if oper == "+":
                total += num
            else:
                total *= num
        return total

    else:
        return int(ex)


def part_1():
    results = [solve(line, True) for line in get_data()]
    return sum(results)


def solve_expression_p2(ex): #if doesnt work, skip first part and just make a func to remove all brackets
    #solve an expression L -> R if it has not parentheses
    # ADDITION TAKES PRECEDENCE OF MULTIPLICATION
    #so add brackets around the addition and let python solve normally
    #print(f'SOLVING {ex}')
    try:#return if already solved
        int(ex)
    except ValueError: #else solve
        # add brackets around addition
        le = ex.split(' ')
        #get indices of multiplication
        le = '(' + ex.replace('*', ')*(') + ')'
        #print(le)
        return eval(le)
    else:
        return int(ex)


def part_2():
    results = [solve(line, False) for line in get_data()]
    return sum(results)


print(part_1())
print(part_2())
