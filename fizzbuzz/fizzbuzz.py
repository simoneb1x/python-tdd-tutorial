# Main script for FizzBuzz

def FizzBuzz(value):
    output = []

    for number in range(1, value+1):
        if number % 15 == 0:
            output.append("FizzBuzz")
        elif number % 3 == 0:
            output.append("Fizz")
        elif number % 5 == 0:
            output.append("Buzz")
        else:
            output.append(number)
    
    return output