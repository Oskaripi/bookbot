global location
location = 'books/frankenstein.txt'
global book
book = open(location, 'r')
global readBook
readBook = book.read()


def checkWordCount():
    splitBook = readBook.split()
    count = len(splitBook)
    print(count)

def countChar():
    diction = {}
    lowerBook = readBook.lower()
    for c in lowerBook:
        if c in diction:
            diction[c] += 1
        else:
            diction[c] = 1
    print(diction)

def report():
    splitBook = readBook.split()
    count = len(splitBook)
    diction = {}
    lowerBook = readBook.lower()
    for c in lowerBook:
        if c in diction:
            if c.isalpha():
                diction[c] += 1
        else:
            if c.isalpha():
                diction[c] = 1
    
    print("--- Begin Report of " + location + " ---")
    print(str(count) + " words found in the document\n")

    sortDict = sorted(diction.items(), key=lambda x: x[1], reverse=True)

    for item, key in sortDict:
        print("The " + item + " character was found " + str(key) + " times")

    print("\n--- End Report ---")

#checkWordCount()
#countChar()
report()