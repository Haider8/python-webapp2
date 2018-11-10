# make_rot.py

from __future__ import print_function

#ascii of m is 109
#ascii of a is 97
#ascii of z is 122
#ascii of M is 77
#ascii of A is 65
#ascii of Z is 90
def rot_func(text):
    i = 0
    rot_text = [None] * len(text)
    while i < len(text):
        s = text[i]
        asci = ord(s)
        if asci >= 97 and asci <= 122:
            if asci <= 109:
                asci = asci + 13
                #print(chr(asci), end="")
            elif asci > 109:
                asci = asci - 13
                #print(chr(asci), end="")

        elif asci >= 65 and asci <= 90:
            if asci <= 77:
                asci = asci + 13
                #print(chr(asci), end="")
            elif asci > 77:
                asci = asci - 13
                #print(chr(asci), end="")
        else:
            rot_text[i] = text[i]
            #print(s, end="")
        rot_text[i] = chr(asci)

        i += 1    

    str1 = ''.join(str(e) for e in rot_text)   
    return str1

#print(rot_func("Hello what;S Up"))

    

                   