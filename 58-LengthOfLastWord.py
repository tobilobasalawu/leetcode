def lengthOfLastWord(self, s: str) -> int:
    words = s.split(' ')
    newWord = []

    for i in words:
        if i == '':
            continue
        else:
            newWord.append(i)

    lastWord = newWord[-1]

    return len(lastWord) 