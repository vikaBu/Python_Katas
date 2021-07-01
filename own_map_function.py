
# creating my own map function without using map() in built functionality- kata from codewars

def mappy(function, list_of_numbers):
    new_list =[function(x) for x in list_of_numbers]
    return new_list

    mappy(sum, [[1, 2, 3],[4, 5],[6, 7, 8]])
    mappy(int, ['34', '23'])
    mappy(str, [1, 2, 3])
    mappy(ord, "Hello")
    mappy(chr, [87, 111, 114, 108, 100])


