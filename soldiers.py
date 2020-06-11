def find_solution(solution_list,no_of_soldiers, column): 
    ''' find the soldiers position ''' 
    if column >= no_of_soldiers: 
        return True
    for row in range(no_of_soldiers): 

        if is_valid_position(solution_list,row , column,no_of_soldiers): 

            solution_list[row][column] = 1

            if find_solution(solution_list,no_of_soldiers, column + 1) == True: 
                return True

            solution_list[row][column] = 0
    return False


def is_valid_position(solution_list, row, column,no_of_soldiers): 
    ''' Check given position is valid '''
    for column_index in range(column): 
        if solution_list[row][column_index] == 1: 
            return False

    for row_index, column_index in zip(range(row, -1, -1), range(column, -1, -1)): 
        if solution_list[row_index][column_index] == 1: 
            return False
    for row_index, column_index in zip(range(row, no_of_soldiers, 1),range(column, -1, -1)): 
        if solution_list[row_index][column_index] == 1: 
            return False
    return True


def place_soldiers(): 
    ''' Create solution list and find the position'''
    no_of_soldiers = int(input("Enter the number of soldiers :"))
    solution_list = [ [0 for column in range(no_of_soldiers)] for row in range(no_of_soldiers)]
    
    if find_solution(solution_list,no_of_soldiers, 0) == False: 
        return "No valid solution!!!"

    return solution_list
solution = place_soldiers() 
print(solution)