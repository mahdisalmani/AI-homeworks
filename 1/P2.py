global table
global fringe
global closed
global m
global n

(pac_x, pac_y) = [int(x) for x in input().split()]
(food_x, food_y) = [int(x) for x in input().split()]
(m, n) = [int(x) for x in input().split()]
table = [[x for x in input()] for x in range(m)]

def heuristic_calculator(food_x, food_y, pos_x, pos_y):
    return abs(food_x - pos_x) + abs(food_y - pos_y)  #manhattan distance

fringe = [{'position': (pac_x, pac_y), 
            'f': heuristic_calculator(food_x, food_y, pac_x, pac_y),
            'father': (-1, -1), 
            'cost': 0}]
closed = {}


def sorted_insert(pos_x, pos_y, f_func, g_func, father_x, father_y):
    index = 0
    if pos_x == food_x and pos_y == food_y:
        f_func -= 1
        g_func -= 1
    item = {'position': (pos_x, pos_y), 'f': f_func, 'father': (father_x, father_y), 'cost': g_func}
    while index < len(fringe):
        if fringe[index]['f'] < f_func:
            index += 1
            continue
        break
    fringe.insert(index, item)   

def problem_solving_agent():
    while fringe:
        item = fringe.pop(0)
        (x, y) = item['position']
        if x == food_x and y == food_y:
            closed[(x, y)] = item['father']
            return
        if x < m - 1 and not table[x + 1][y] == '%' and not closed.get((x + 1, y), False):
            sorted_insert(x + 1, y, 
            item['cost'] + 1 + heuristic_calculator(food_x, food_y, x + 1, y), 
            item['cost'] + 1, x, y)
        if y < n - 1 and not table[x][y + 1] == '%' and not closed.get((x, y + 1), False):
            sorted_insert(x, y + 1, 
            item['cost'] + 1 + heuristic_calculator(food_x, food_y, x, y + 1), 
            item['cost'] + 1, x, y)
        if y > 0 and not table[x][y - 1] == '%' and not closed.get((x, y - 1), False):
            sorted_insert(x, y - 1, 
            item['cost'] + 1 + heuristic_calculator(food_x, food_y, x, y - 1), 
            item['cost'] + 1, x, y)
        if x > 0 and not table[x - 1][y] == '%' and not closed.get((x - 1, y), False):
            sorted_insert(x - 1, y, 
            item['cost'] + 1 + heuristic_calculator(food_x, food_y, x - 1, y), 
            item['cost'] + 1, x, y)

        closed[(x, y)] = item['father']

problem_solving_agent()

def print_path(x, y):
    if x == pac_x and y == pac_y:
        print(str(x) + " " + str(y))
        return
    print_path(closed[(x, y)][0], closed[(x, y)][1])
    print(str(x) + " " + str(y))

print_path(food_x, food_y)
