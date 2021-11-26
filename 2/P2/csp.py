global n
n = int(input())
variables = [{x:True for x in range(n)} for i in range(n)]  # set of variable for csp problem
global pos, neg
tempdiagonal = [x for x in range(1, n)]
tempdiagonal.reverse()
neg = [x for x in range(1, n + 1)] + tempdiagonal           # number of squares in \ diagonals
pos = neg.copy()                                            # number of squares in / diagonals
unassigned = {x:True for x in range(n)}                     # set of unassigned variable

def get_neg_index(x, y):            
    return n - y + x - 1                                    # get index of neg diagonal for a square of chessboard (column x, row y)
def get_pos_index(x, y):
    return 2 * n - x - y - 2                                # get index of pos diagonal for a square of chessboard (column x, row y)



def remove_incosistent_values(unassigned_varibale_values, unassigned_variable_index, assigned_variable_index, assigned_variable_value):
    pruned = []
    if assigned_variable_value in unassigned_varibale_values:
        unassigned_varibale_values.pop(assigned_variable_value)
        pruned.append([unassigned_variable_index, assigned_variable_value])


    if assigned_variable_value - (assigned_variable_index - unassigned_variable_index) in unassigned_varibale_values:
        unassigned_varibale_values.pop(assigned_variable_value - (assigned_variable_index - unassigned_variable_index))
        pruned.append([unassigned_variable_index, assigned_variable_value - (assigned_variable_index - unassigned_variable_index)])

    if assigned_variable_value + (assigned_variable_index - unassigned_variable_index) in unassigned_varibale_values:
        unassigned_varibale_values.pop(assigned_variable_value + (assigned_variable_index - unassigned_variable_index))
        pruned.append([unassigned_variable_index, assigned_variable_value + (assigned_variable_index - unassigned_variable_index)])

    return pruned


"""
doing forward_cheking for unassigned variables
"""
def forward_checking(variables, assigned_index, assigned_value ,unassigned):
    pruned = []
    for index in unassigned:
        pruned += remove_incosistent_values(variables[index], index, assigned_index, assigned_value)
    return pruned


def NQueens(variables, step, unassigned):

    if step == n:
        return True, variables

    """
    finding variable with minimum valid, remaning domain value
    """
    variable, minimum = 0, n + 1
    for i in unassigned:
        if len(variables[i]) == 0:
            return False, variables
        
        if len(variables[i]) < minimum:
            minimum = len(variables[i])
            variable = i
    unassigned.pop(variable)
    temp = {x:True for x in variables[variable]}


    """
    finding best remaning value each time (sorting by threated squares)
    """
    sorted_values = (list(variables[variable].keys()))
    sorted_values.sort(key= lambda x: pos[get_pos_index(x, variable)] + neg[get_neg_index(x, variable)], reverse=True)


    for value in sorted_values:
        variables[variable] = {value:True}
        pruned = forward_checking(variables, variable, value, unassigned)
        find, soln = NQueens(variables, step + 1, unassigned)
        if find:
            return True, soln
        for pair in pruned:
            variables[pair[0]][pair[1]] = True  # restore pruned varibales
    variables[variable] = temp                  # restore chessboard
    unassigned[variable] = True
    return False, variables



find, soln = NQueens(variables, 0, unassigned)


"""
printing formed solution
"""
for variable in soln:
    queen_place = (list(variable.keys()))[0]
    print("_ " * queen_place + "o " + (n - 1 - queen_place) * "_ ")
