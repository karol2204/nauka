import time

def function_performance(func, arg, how_many_times = 1):
    sum = 0
    
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

def if_is_element(what_value):
    if what_value in listContainer:
        return True
    else:
        return False

print(function_performance(if_is_element, 45, how_many_times = 1000000))
