"""This module supplies a single function reverse_words that reverses
a string word by word.

>>> reverse_words('four score and seven years')
'years seven and score four'

You must call reverse_words with a single argument, a string:
>>> reverse_words(1)
Traceback (most recent call last):
    ...
AttributeError: 'int' object has no attribute 'split'
"""


def reverse_words(astring):
    words = astring.split()
    words.reverse()
    return ' '.join(words)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
