# coding=utf-8


class RabinKarp:
    """
    p 505
    将字符串转换为一个R进制的数，R为字符表大小。
    设n为模式字符串的长度，Ti为文本中索引为i的字符对应的码点值,Xi为文本i到i+n-1(i从0开始，所以-1)对应的R进制数：
    Xi = Ti*R^(n-1) + T(i+1)*R^(n-2) + ... + T(i+n-1)*R^0
    X(i+1) = (Xi - Ti*R^(n-1))*R + T(i+n)*R^0
    每一步都求余，与计算完毕再求余结果是一样的。
    """

    def __init__(self, pat):
        self._pat = pat
        # 字符表大小，假定字符在Unicode第一平面内
        self._R = 0xd800
        self._patlen = len(pat)
        # 选择一个足够大的质数，避免碰撞
        self._Q = 999999937
        # 模式字符串的指纹
        self._pathash = self._hash(pat)
        # R^(_patlen-1)%Q
        self._RM = 1
        for i in range(1, self._patlen):
            self._RM = (self._R * self._RM) % self._Q

    def _hash(self, key, start=0, lenght=0):
        h = 0
        lenght = lenght or len(key)
        # 每一步都求余，与计算完毕再求余结果是一样的。每一步都求余可以保证不溢出
        for i in range(start, start + lenght):
            h = ((h * self._R) + ord(key[i])) % self._Q
        return h

    def _check(self, text, start):
        for i in range(self._patlen):
            if text[start + i] != self._pat[i]:
                return False
        return True

    def search(self, text):
        n = len(text)
        if n < self._patlen:
            return -1
        texthash = self._hash(text, lenght=self._patlen)
        if texthash == self._pathash and self._check(text, 0):
            return 0
        for i in range(0, n - self._patlen):
            # 加上Q是为了保证结果为正数，因为是对Q求余，所以加上Q并不会影响结果
            # 这两句代码是 X(i+1) = (Xi - Ti*R^(n-1))*R + T(i+n)*R^0 的实现， 并且将 X(i+1)求余
            texthash = ((texthash + self._Q) - (self._RM * ord(text[i]))) % self._Q
            texthash = (texthash * self._R + ord(text[i + self._patlen])) % self._Q
            # 散列有可能发生碰撞，所以需要检查是否真得匹配
            if texthash == self._pathash and self._check(text, i + 1):
                return i + 1
        return -1


if __name__ == '__main__':
    def index_of(text, pat):
        return RabinKarp(pat).search(text)


    t = "特朗普在过去20年间分别支持过共和党和民主党各主要总统竞选者。2015年6月，\
    特朗普以共和党竞选者身份正式参加2016年美国总统选举。此前，特朗普没有担任过公共职务。特朗普结过3次婚，育有5个子女。 \
    [1]  2016年11月9日，唐纳德·特朗普已获得了276张选举人票，超过270张选举人票的获胜标准，当选美国第45任总统。 [2]  2017年1月20日，特朗普正式成为美国第45任总统。"

    print(index_of(t, '45任总统。'))
