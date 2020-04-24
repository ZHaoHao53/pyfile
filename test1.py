#print('hello\nworld')
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            print(index)
        index = index + 1

print(find('banana','a'))