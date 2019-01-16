# coding=utf-8


class BoyerMoore:
    """
    p502
    KMP算法保证了最坏情况下线性级别的运行时间。但是一般实际运用中比暴力算法的性能优势并不明显
    因为实际运行中，几乎不会在重复性很高的文本中查找重复性很高的模式。
    并且需要构建一个R*M的辅助空间，R为字符表大小，M为模式长度。
    BoyerMoore算法在一般情况下，处理不匹配查找只需要~N/M次字符比较
    """

    def __init__(self, pat):
        self._pat = pat
        self._patlen = len(pat)
        # 用来保存字符在pat中从左到右最后一次出现位置的索引
        # 原始算法中将其初始化为一个字符表大小的数组，对于ASCII码来说这样是比较合适的
        # 如果处理的是Unicode这样大型的码表，一般来说pat中出现的字符数量不会太多，远远不及码表大小，所以我初始化一个散列表
        self._right = dict()
        for i in range(self._patlen):
            self._right[pat[i]] = i

    def search(self, text):
        tlen = len(text)
        # 下一次跳跃的长度
        i = 0
        while i <= tlen - self._patlen:
            skip = 0
            # pat从右往左匹配
            for j in range(self._patlen - 1, -1, -1):
                # 如果当前位置不匹配
                if self._pat[j] != text[i + j]:
                    # 取到text中当前位置字符在模式中最后出现的位置
                    index = self._right.get(text[i + j])
                    # 将text中当前位置字符和模式中最后出现位置对齐
                    if index is not None:
                        skip = j - index
                    else:
                        # text当前位置的字符不在模式中，不可能匹配成功，直接跳过这个位置
                        skip = j + 1
                    # 如果要发生回退，就前进一步
                    if skip < 1:
                        skip = 1
                    break
            # 完成了for循环，匹配成功
            if skip == 0:
                return i
            i += skip
        return -1


def search(text, pat):
    return BoyerMoore(pat).search(text)


# ================== test ===============
if __name__ == '__main__':
    t = 'hello word'
    p = 'lo w'
    print(search(t, p))
