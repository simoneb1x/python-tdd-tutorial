def middle_permutation(string):
    
    sorted_string = sorted(string)
    if len(sorted_string) % 2 == 0:
        return sorted_string.pop(len(sorted_string) // 2 - 1) + ''.join(sorted_string[::-1])
    else:
        return sorted_string.pop(len(sorted_string) // 2) + middle_permutation(sorted_string)