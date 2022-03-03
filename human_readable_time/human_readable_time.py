def make_readable(seconds):

    if seconds > 359999:
        raise ValueError('Invalid number of seconds: {}'.format(seconds))
    
    s = seconds % 60
    seconds //= 60

    m = seconds % 60
    seconds //= 60

    h = seconds

    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)