class GrammarError(Exception):
    def __init__(self, found, suggestion):
        self.found = found
        self.suggestion = suggestion


class InvalidWordError(GrammarError):
    pass


class MisspelledWordError(GrammarError):
    pass


invalid_words = {
    'irregardless': 'regardless',
    "ain't": "isn't",
}
mispelled_words = {
    'tacco': 'taco'
}


def check_grammar(s):
    exceptions = []
    for word in s.lower().split():
        if (suggestion := invalid_words.get(word)) is not None:
            exceptions.append(InvalidWordError(word, suggestion))
        elif (suggestion := mispelled_words.get(word)) is not None:
            exceptions.append(MisspelledWordError(word, suggestion))
    if exceptions:
        raise ExceptionGroup('Found grammar errors', exceptions)

text = "Irregardless a hot dog ain't a tacco"
try:
    check_grammar(text)
except* InvalidWordError as iwe:
    print('\n'.join(f'{e.found!r} is not a word, use {e.suggestion!r}' for e in iwe.exceptions))
except* MisspelledWordError as mwe:
    print('\n'.join(f'{e.found!r}, perhaps you meant {e.suggestion!r}' for e in mwe.exceptions))
else:
    print('No errors!')
