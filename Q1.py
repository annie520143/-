
def reverse_string(s):
    rs = ''
    for i in range(len(s)-1, -1, -1):
        rs = rs+s[i]

    return rs

def reverse_sentence(s):

    out = ''
    tmp = ''
    for ss in s:
        
        if ss == ' ':
            out = out + reverse_string(tmp)
            out = out + ' '
            tmp = ''

        else :
            tmp = tmp + ss

    out = out + reverse_string(tmp)

    print(out)


if __name__ == '__main__':
    s = input()
    reverse_sentence(s)