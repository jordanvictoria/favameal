


# The function should return the sum of all the multiples of 3 and/or 5 less than (but not equal to) the number passed in

#You'll need to create an iterable (something that can be looped over ie. List) of the numbers below the parameter. 
# Look up the range function and modulo operator


# LIST COMPREHENSION

def sum_of_multiples(num):
    multiples = [i for i in range(1, num) if i % 3 == 0 or i % 5 == 0]
    return sum(multiples)


# def sum_of_multiples(num):
#     list_of_nums = []
#     for i in range(num):
#         if i % 3 == 0 or i % 5 == 0:
#             list_of_nums.append(i)
#     return sum(list_of_nums)
            


def test_sum_of_multiples_solution():
    assert sum_of_multiples(10) == 23
    assert sum_of_multiples(20) == 78
    assert sum_of_multiples(0) == 0
    assert sum_of_multiples(1) == 0
    assert sum_of_multiples(200) == 9168
    assert sum_of_multiples(64) == 933





