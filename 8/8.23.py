word = input().lower()
while word.count(word[0]) != len(word):
    word = word.replace(word[0], "")
print(word)
