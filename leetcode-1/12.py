# coding=utf-8


# 65-90 97-122 30-39

def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        c1 = parse(s[left])  # isalnum
        if c1 is None:
            left += 1
            continue
        c2 = parse(s[right])
        if c2 is None:
            right -= 1
            continue
        if c1 != c2:
            return False
        left += 1
        right -= 1
    return True


def parse(char):
    uc = ord(char)
    if 65 <= uc <= 90 or 48 <= uc <= 57:
        return char
    elif 97 <= uc <= 122:
        return chr(uc - 32)


s = 'asdasd'
x = [x for x in s]
print(''.join(x))
