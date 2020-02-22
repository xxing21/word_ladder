#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    from collections import deque
    from copy import deepcopy

    f = open('words5.dict')
    dictionary = f.read().split("\n")

    s = []
    s.append(start_word)
    q = deque()
    q.append(s)

    while len(q) > 0:
        top = q.pop()[0]
        for word in dictionary:
            if _adjacent(top, word) is True:
                if word == end_word:
                    s.append(word)
                    return s
                copy = deepcopy(s)
                copy.append(word)
                q.append(copy)
                dictonary.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''

    if len(ladder) == 0:
        return False
    else:
        for i in range(len(ladder)-1):
            if _adjacent(ladder[i], ladder[i+1]) is False:
                return False
        return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    diff = 0
    if len(word1) != len(word2):
        return False
    else:
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                diff = diff + 1
        if diff == 1:
            return True
        else:
            return False
