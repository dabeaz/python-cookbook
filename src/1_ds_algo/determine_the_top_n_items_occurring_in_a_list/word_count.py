# example.py
#
# Determine the most common words in a list

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print("top_three", top_three)
# outputs [('eyes', 8), ('the', 5), ('look', 4)]

# Example of merging in more words

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes', 'look', 'look']
word_counts.update(morewords)
print("after merging in more words, top_three: ", word_counts.most_common(3))
