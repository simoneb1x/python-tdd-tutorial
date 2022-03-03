def pig_it(text):
    # first array where I split the words based on whitespaces
    text_splitted = text.split()

    # array that will be returned as output
    output = []
    
    for word in text_splitted:
        word_splitted = list(word)
        word_splitted.append(word_splitted[0] + "ay")
        word_splitted.pop(0)
        output.append(''.join(word_splitted))

    output = ' '.join(output)

    return output