from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words = {'rose': 'rose', 'tulip': 'tulip', 'lotus': 'lotus', 'daffodil': 'daffodil'}

word = ''
found = False

while vowels and consonants:

    if found:
        break

    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in words:
        words[word] = words[word].replace(vowel, '')
        words[word] = words[word].replace(consonant, '')

        if not words[word]:
            print(f'Word found: {word}')
            break
    else:
        continue

    break

else:
    print(f'Cannot find any word!')
if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
