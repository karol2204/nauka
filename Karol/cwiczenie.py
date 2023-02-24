import time

def function_performance(func, *arg, how_many_times):
    sum = 0
    print(arg)
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum

setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]


def if_contain_in(what_value, container):
    if what_value in container:
        return True
    else:
        return False

print(function_performance(if_contain_in, 632, setContainer, how_many_times = 30000000))
print(function_performance(if_contain_in, 632, listContainer, how_many_times = 30000000))
