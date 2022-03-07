def form(time, seconds_converted):
    if time == 0:
        return ""
    if time == 1:
        return "1 "+ seconds_converted
    return str(time) + " " + seconds_converted + "s"

def readable(array):
    array = list(filter(None, array))
    result = ""
    if len(array) == 1:
        return array[0]
    for i in range(len(array)-1):
        result = result + ", " + array[i]
    result = result + " and " + array[len(array)-1]
    return result[2:]

def format_duration(seconds):
    if seconds == 0:
        return "now"

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    d, h = divmod(h, 24)
    y, d = divmod(d, 365)

    return readable([form(y,"year"),form(d,"day"),form(h,"hour"),form(m,"minute"),form(s,"second")])
