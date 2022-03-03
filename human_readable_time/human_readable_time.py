def make_readable(seconds):

    if seconds > 359999:
        raise ValueError('Invalid number.')
    
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)