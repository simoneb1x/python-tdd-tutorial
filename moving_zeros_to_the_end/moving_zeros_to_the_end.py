def move_zeros(array):
    return [number for number in array if number] + [0]*array.count(0)