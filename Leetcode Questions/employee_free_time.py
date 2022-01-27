def find_employee_free_time(schedule):
    if not schedule:
        return []

    result = []
    end = schedule[0][1]

    for i in range(1, len(schedule)):
        curr = schedule[i]
        if end < curr[0]:
            result.append([end, curr[0]])
        end = max(end, curr[1])
    
    return result

print(find_employee_free_time([[1,3], [5,6],[2,3], [6,8]] ) )