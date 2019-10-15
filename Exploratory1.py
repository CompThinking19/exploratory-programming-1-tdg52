# defined function
# tested validity of the function
# called it three times
def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 5]
    return result
double([7, 8, 9])
[35, 40, 45]
double([5, 10, 15])
[25, 50, 75]
double([3, 6, 9])
[15, 30, 45]
