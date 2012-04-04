#coding=utf8
'''
'''

import sys, os

dicts = open(os.path.join(os.path.dirname(__file__), 'words.txt'), 'r').read()
dicts = dicts.split('\n')
dicts = [(v.split('[')[0], None) for v in dicts if v.find('[')>0]
dicts = dict(dicts)

_start = dict()
for w in dicts.keys():
    for i in range(len(w)):
        key = i+1
        if not key in _start:
            _start[key] = dict()
        _start[key][w[:key]] = None

def _enumwords(chars, word='', words=[]):
    "enumerate all posible words"
    length = len(chars)
    if word:
        if len(word) not in _start or word not in _start[len(word)]:
            print word
            return
    for i in range(length):
        c = chars[i]
        w = word+c
        words.append( w )
        if length == 1:
            return 
        else:
            _enumwords(''.join([chars[j] for j in range(length) if j!=i]), w, words)
    return words

def enumwords(chars):
    return _enumwords(chars.strip(), '', [])

def feed(chars):
    allwords = set(enumwords(chars))
    words = []
    for w in allwords:
        if w in dicts:
            words.append(w)
    return words

if __name__ == '__main__':
    while True:
        try:
            chars = raw_input('>> Give me chars:\n>> ')
            words = feed(chars)
            if not words:
                print '>>', ''
            else:
                print '>>', 'Possible words:'
                for w in words:
                    print '>>', '\t', w
        except KeyboardInterrupt:
            exit()
