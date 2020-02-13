import sys

punctuationToRemove = ["'", "\"", ".", "\"", ",", "-"]

# This is a function which gets the argument with the specified name or returns
# an empty string if it can't find that argument.
def getArgument(name):
    for argument in sys.argv:
        if argument.startswith("-" + name):
            return argument[argument.index("=") + 1:]
    return ""

def removePunctuation(word):
    for punctuation in punctuationToRemove:
        if word.startswith(punctuation):
            word = word[1:]
        if word.endswith(punctuation):
            word = word[:-1]
    return word

# This gets the file name or exits the program if it is not specified.
filename = getArgument("file")
if filename is "":
    print ("No file name specified, specify the filename uing -file=filename argument")
    sys.exit()

minWordLength = getArgument("length")
if minWordLength is "":
    minWordLength = 0

numberToShow = getArgument("top")
if numberToShow is "":
    numberToShow = 10

wordCounts = {}

# Opens the  file which has been specified for reading.
inputFile = open(filename, "r")
# Reads a single line of that file
line = inputFile.readline()
# Loop over each of the lines
while (line):
    # Seperate each of the words in the line into a list
    words = line.split()
    # Loop over each word in the line.
    for word in words:
        word = removePunctuation(word)
        if (len(word) > minWordLength):
            if word in wordCounts:
                wordCounts[word] += 1
            else:
                wordCounts[word] = 1
        
    line = inputFile.readline()


while len(wordCounts) > 0 and numberToShow > 0:
    highestValue = 0
    for word in wordCounts:
        if (wordCounts[word] > highestValue):
            highestValue = wordCounts[word]
            highestWord = word
    if (highestValue is 1):
        timeString = " time"
    else:
         timeString = " times"   
    print (highestWord + " appears " + str(highestValue) + timeString)
    wordCounts.pop(highestWord)
    numberToShow -= 1
