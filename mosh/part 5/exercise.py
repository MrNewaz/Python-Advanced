from pprint import pprint

sentence = 'This is a common interview Question'

char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1


char_sorted = sorted(char_frequency.items(),
                     key=lambda kv: kv[1], reverse=True)


pprint(char_sorted, width=1)
print("Answer", char_sorted[0])
