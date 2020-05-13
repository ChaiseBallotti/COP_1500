#identify words
    #-spaces
    #-punctuation
    #end of string

def parse_words(line : str):
    """given a string in line prints each word"""

    line = line.lower()
    index = 0
    begin_index = 0
    words = []

    while index < len(line):

        #looking for start of word
        while index < len(line) and line[index] == ' ':
            index += 1
        begin_index = index

        #looking fo rthe en of next word
        while index < len(line) and line[index] != ' ':
            index += 1
        end_index = index

        if begin_index < len(line):
            #print(line[begin_index:end_index])
            words.append(line[begin_index:end_index])

    return words

def word_to_piglatin(word):
    """returns a string that represents the pig latin translation"""
    return word[1:] + word[0] + 'ay'

def line_to_piglatin(english_line):
    line = ""
    for word in english_words:
        line = line + " " + word_to_piglatin(word)

    return line.strip()

english_words = parse_words("The little brown fox jumped over the picket fence ")

#line = ""
#for word in english_words:
#    line = line + " " + to_piglat(word)
#line = line.strip()
print(line_to_piglatin("The little brown fox jumped over the picket fence "))

#for i in range(len(english_words)):
#    print(english_words[i])





