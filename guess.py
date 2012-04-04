#coding=utf8
'''
'''

import sys, os

dicts = open(os.path.join(os.path.dirname(__file__), 'words.txt'), 'r').read()
dicts = dicts.split('\n')
dicts = [(v.split('[')[0], None) for v in dicts if v.find('[')>0]
dicts = dict(dicts)

_2start = dict()
_3start = dict()
_4start = dict()
for w in dicts.keys():
    l = len(w)
    if l >= 2:
        _2start[w[:2]] = None
    if l >= 3:
        _3start[w[:3]] = None
    if l >= 4:
        _4start[w[:3]] = None
print len(_2start), len(_3start), len(_4start)

def _enumwords(chars, word='', words=[]):
    "enumerate all posible words"
    length = len(chars)
    if len(word) == 2 and word not in _2start:
        print word
        return 
    elif len(word) == 3 and word not in _3start:
        print word
        return
    elif len(word) == 4 and word not in _4start:
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
