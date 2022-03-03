import string

def pig_it(text):
    # first list where I split the words based on whitespaces
    text_splitted = text.split()

    # array that will be returned as output
    output = []
    
    # looping the list:
    # if word == punctuation, just simply append it
    # else, transform the word and append it
    for word in text_splitted:
        if word in string.punctuation:
            output.append(word)
        else:
            word_splitted = list(word)
            word_splitted.append(word_splitted[0] + "ay")
            word_splitted.pop(0)
            output.append(''.join(word_splitted))

    # we join all words in a single string
    output = ' '.join(output)

    return output