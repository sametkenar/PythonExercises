def capitalize_sentences(string):
    def upper_initial(string):
        return string[0].upper() + string[1:] if string else string
    
    def split_by_and_capitalize(string, delimiter):
        sentences = [sentence.lstrip() for sentence in string.split(delimiter)]
        return (delimiter + '').join(
            [upper_initial(sentence) for sentence in sentences])
    
    delimiters = [',', '?', '!']

    for delimiter in delimiters:
        string = split_by_and_capitalize(string, delimiter)

    return string.rstrip() # discard trailing whitespace

print(capitalize_sentences('lorem. ipsum? dolor sit amet, consectetur! adipiscing elit.'))
print(capitalize_sentences('string methods are really useful in Python! you need to know them to succeed in CENG240.'))

