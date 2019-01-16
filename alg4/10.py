# coding=utf-8

class KMPplus:
    """
    alg4 p496
    KPM算法在一般情况下并不会带来明显性能提升
    该算法代码简单，但我还没理解其实现原理
    """

    def __init__(self, pat):
        self._pat = pat
        self._patlen = len(pat)
        self._next = [-1 for i in range(self._patlen)]
        j = 0
        for i in range(1, self._patlen):
            if pat[i] != pat[j]:
                self._next[i] = j
            else:
                self._next[i] = self._next[j]
            while j >= 0 and pat[i] != pat[j]:
                j = self._next[j]
            j += 1

    def search(self, text):
        patlen = self._patlen
        textlen = len(text)
        i = 0
        j = 0
        while i < textlen and j < patlen:
            while j >= 0 and text[i] != self._pat[j]:
                j = self._next[j]
            i += 1
            j += 1
        if j == patlen:
            return i - patlen
        return -1


if __name__ == '__main__':
    def index_of(text, pat):
        return KMPplus(pat).search(text)


    t = 'this is a text for KMP'

    print(index_of(t, 'KMP'))
