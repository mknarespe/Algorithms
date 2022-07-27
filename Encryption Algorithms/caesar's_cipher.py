def decryption(s: str, n: int = 0) -> str:
    res = ''
    for char in s:
        if char != ' ':
            char = chr(ord(char)+n)
        res = res+char
    return res


if __name__ == '__main__':
    s ="a b c d e f g h i j k l m n o p q r s t u v w x y z"
    n = 2
    encryption = decryption(s, n)
    print(encryption)
