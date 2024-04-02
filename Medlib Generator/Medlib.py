def readstory():
    with open('story.txt','r') as f:
        story = f.read()

        words = set()
        targets = "["
        targete = "]"
        start_of_word = -1
        for i, char in enumerate(story):
            if char == targets:
                start_of_word = i
            
            if targete == char and start_of_word != -1:
                word = story[start_of_word:i+1]
                words.add(word)

        return words


def getwords(words):
    wordlist = {}
    for word in words:
        wordlist[word] = input("Enter a word for " + word + ": ")
    return wordlist


def main():
    with open('story.txt','r') as f:
        story = f.read()

    word = readstory()
    wordlist = getwords(word)

    for old_word, new_word in wordlist.items():
        story = story.replace(old_word, new_word)

    print(story)


main()
