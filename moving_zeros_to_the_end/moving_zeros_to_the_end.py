def move_zeros(array):
    for number in array:
        if number == 0:
            array.remove(number)
            array.append(number)
    
    return array