"""def o0O():
    print('Input an English word to be translated into a Haforli word: ')
    inputWord = raw_input().strip().split(' ')[0]
    reversedWord = inputWord[::-1]
    Ooo = ''
    o0oOoO00o = len(reversedWord) - 1 if ooOO00oOo(reversedWord) else len(reversedWord)
    print o0oOoO00o
    for i in range(0, o0oOoO00o, 2):
        Ooo += reversedWord[i + 1] + reversedWord[i]

    if ooOO00oOo(reversedWord):
        Ooo += reversedWord[-1]
    print Ooo
    output = ''
    for s in Ooo:
        if not s.isalpha():
            output += s + s
        elif s.isupper():
            output += s + random.choice(string.ascii_uppercase)
        else:
            output += s + random.choice(string.ascii_lowercase)


    print('Your translated word: {0}'.format(output))
"""
def decrypt(enc):
    enc = enc[::-1]
    tmp = ""
    out = ""
    for i in range(1, len(enc), 2):
        tmp += enc[i]
    for i in range(0, len(tmp), 2):
        try:
            out += tmp[i+1] + tmp[i]
        except:
            out += tmp[i]
    return out
print decrypt("da}}rilwwe00yt____mfotfysf__11ty11mg__lphyer__tyrt33__algv33uc44nrgely44ys____mvozfpsw__11tv11mf{{letsfmmgcutbic")