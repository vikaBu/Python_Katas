def map1(function, list_of_lists):
    list_of_lists = [[1, 2, 3],
                     [4, 5],
                     [6, 7, 8]]
    return [sum(x) for x in list_of_lists]

def map2(function, map_list_of_string):
    map_list_of_strings= ['34', '23']
    return [int(number) for number in map_list_of_strings]

def map3(function, map_numbers_to_strings):
    map_numbers_to_strings = [1, 2, 3]
    return [str(x) for x in map_numbers_to_strings]

def map4(function, map_to_order):
    map_to_order = [72, 101, 108, 108, 111]
    return [int(i) for i in map_to_order]

def map5(function, map_to_order):
    map_to_order = "Hello"
    for char in range(0, len(map_to_order)):
        return ord(map_to_order[char])

def map6(function, map_to_numbers):
    map_to_numbers = [87, 111, 114, 108, 100]
    return [chr(n) for n in map_to_numbers]



