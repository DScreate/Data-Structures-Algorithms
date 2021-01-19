from timeit import default_timer as timer

def findFactorialRecursive(number):
    if number <= 2:
        return number
    return number * findFactorialRecursive(number - 1)

def findFactorialIterative(number):
    num = 0
    for x in range(0, number):
        num *= x

    return num


test = 255
start = timer()
print(findFactorialRecursive(test))
elapsed_time = timer() - start # in seconds
print('recursive took ', elapsed_time)

start = timer()
print(findFactorialRecursive(test))
elapsed_time = timer() - start # in seconds
print('iterative took ', elapsed_time)
