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

    y = seconds // (3600*24*365)
    d = (seconds % (3600*24*365))//(3600*24)
    h = (seconds % (3600*24)) // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60

    return readable([form(y,"year"),form(d,"day"),form(h,"hour"),form(m,"minute"),form(s,"second")])
