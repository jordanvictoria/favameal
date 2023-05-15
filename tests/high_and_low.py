def highest_and_lowest(string_o_numbers):
    
    numbers = string_o_numbers.split()

    
    new_numbers = []
    for num in numbers:
        new_num = int(num)
        new_numbers.append(new_num)
    
    highest = max(new_numbers)
    lowest = min(new_numbers)
    
    return {"highest": highest, "lowest": lowest}


# def highest_and_lowest(string_o_numbers):
#     numbers = [int(x) for x in string_o_numbers.split()]
#     highest = numbers[0]
#     lowest = numbers[0]
#     for num in numbers:
#         if num > highest:
#             highest = num
#         elif num < lowest:
#             lowest = num
#     return {"highest": highest, "lowest": lowest}




def test_highest_and_lowest_solution():
    assert highest_and_lowest('5 4 3 9 7 23') == { 'highest': 23, 'lowest': 3 }
    assert highest_and_lowest('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6') == { 'highest': 542, 'lowest': -214 }
    assert highest_and_lowest('1 -1') == { 'highest': 1, 'lowest': -1 }
    assert highest_and_lowest('42') == { 'highest': 42, 'lowest': 42 }
    assert highest_and_lowest('2189 3105 476 2849 1619 1816 1785 1037 3266 187 446 3032 1743 2940 535 1677 2176 968 176 2078 2404 2867') == { 'highest': 3266, 'lowest': 176 }