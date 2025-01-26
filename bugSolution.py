def function_with_uncommon_error_solution(a, b):
    if a == 0 and b == 0:
        return 0  # Or raise an appropriate exception
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error_solution(10, 0)
result2 = function_with_uncommon_error_solution(0,0)
result3 = function_with_uncommon_error_solution(5,2)