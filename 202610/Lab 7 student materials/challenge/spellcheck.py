def file_to_string(filename):
    """ Return the entire contents of the file called filename
    as a string. Precondition: the given file exists. """
    with open(filename , 'r') as f:
        contents = f.read()
        
    return contents

def load_words():
    """ Return a list of all words """
    with open("en_US.dic") as f:
        words = f.readlines()
    
    return [w.strip().split('/')[0] for w in words]

def normalize_word(word):
    ignore = ["'", '"', ',', '.', ';', '?', ')', '(']
    ignore.extend('0123456789')
    word = word.strip()
    for s in ignore:
        word = word.replace(s, "")
    return word.lower()

wordlist = load_words()

document = file_to_string("sample_document.txt")


for word in document.split():
    wn = normalize_word(word)
    if wn == "" or wn in wordlist or word in wordlist:
        pass#print(word, end=" ")
    else:
        print("[SP ", wn, "]", word, "[/SP]", sep="", end="\n")