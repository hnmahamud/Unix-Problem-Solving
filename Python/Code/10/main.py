import string

# Open the file in read mode
text = open("test.txt", "r")

# Search word from file
# Convert lowercase to avoid case mismatch
search = input('Enter a word: ')
search = search.lower()

# Initialize variables
lineNum = 1
wordPos = 0
wordNum = 0
finalPos = 0

# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        wordPos = (wordPos + len(word)) + 1
        if search == word:
            wordNum = wordNum + 1
            finalPos = (wordPos - (len(word))) - 1
            print('Line-{0}, Position-{1} '.format(lineNum, finalPos))

    lineNum = lineNum + 1

print('The word is found {0} times'.format(wordNum))