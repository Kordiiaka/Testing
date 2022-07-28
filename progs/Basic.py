row1 = '295743861'
row2 = '431865927'
row3 = '876192543'
row4 = '387459216'
row5 = '612387495'
row6 = '549216738'
row7 = '763524189'
row8 = '928671354'
row9 = '154938673'

digits = '123456789'

def col():
    a = list(row1)
    b = list(row2)
    c = list(row3)
    d = list(row4)
    e = list(row5)
    f = list(row6)
    g = list(row7)
    h = list(row8)
    i = list(row9)
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    e.sort()
    f.sort()
    g.sort()
    h.sort()
    i.sort()

    for elem in range(9):
        if a[elem] == b[elem] == c[elem] == d[elem] == e[elem] == \
        f[elem] == g[elem] == h[elem] == i[elem]:
            continue
        else:
            return "No"
    return "Yes"


def my_f():
    for ch in range(len(digits)):
        a = row1.find(digits[ch])
        b = row2.find(digits[ch])
        c = row3.find(digits[ch])
        d = row4.find(digits[ch])
        e = row5.find(digits[ch])
        f = row6.find(digits[ch])
        g = row7.find(digits[ch])
        h = row8.find(digits[ch])
        i = row9.find(digits[ch])

        if a == -1 or b == -1 or c == -1 or d == -1 or e == -1 or \
                f == -1 or g == -1 or h == -1 or i == -1:
            print("No")
            break

    if a != -1 and b != -1 and c != -1 and d != -1 and e != -1 and \
            f != -1 and g != -1 and h != -1 and i != -1:
        print(col())


def subs():
    a = list(row1)
    b = list(row2)
    c = list(row3)
    d = list(row4)
    e = list(row5)
    f = list(row6)
    g = list(row7)
    h = list(row8)
    i = list(row9)

    subs1 = a[0] + a[1] + a[2] + b[0] + b[1] + b[2] + c[0] + c[1] + c[2]
    subs2 = a[3] + a[4] + a[5] + b[3] + b[4] + b[5] + c[3] + c[4] + c[5]
    subs3 = a[6] + a[7] + a[8] + b[6] + b[7] + b[8] + c[6] + c[7] + c[8]
    subs4 = d[0] + d[1] + d[2] + e[0] + e[1] + e[2] + f[0] + f[1] + f[2]
    subs5 = d[3] + d[4] + d[5] + e[3] + e[4] + e[5] + f[3] + f[4] + f[5]
    subs6 = d[6] + d[7] + d[8] + e[6] + e[7] + e[8] + f[6] + f[7] + f[8]
    subs7 = g[0] + g[1] + g[2] + h[0] + h[1] + h[2] + i[0] + i[1] + i[2]
    subs8 = g[3] + g[4] + g[5] + h[3] + h[4] + h[5] + i[3] + i[4] + i[5]
    subs9 = g[6] + g[7] + g[8] + h[6] + h[7] + h[8] + i[6] + i[7] + i[8]

    for ch in range(len(digits)):
        check1 = subs1.find(digits[ch])
        check2 = subs2.find(digits[ch])
        check3 = subs3.find(digits[ch])
        check4 = subs4.find(digits[ch])
        check5 = subs5.find(digits[ch])
        check6 = subs6.find(digits[ch])
        check7 = subs7.find(digits[ch])
        check8 = subs8.find(digits[ch])
        check9 = subs9.find(digits[ch])

        if check1 == -1 or check2 == -1 or check3 == -1 or check4 == -1 or check5 == -1 or \
                check6 == -1 or check7 == -1 or check8 == -1 or check9 == -1:
            print("No")
            break

    if check1 != -1 and check2 != -1 and check3 != -1 and check4 != -1 and check5 != -1 and \
            check6 != -1 and check7 != -1 and check8 != -1 and check9 != -1:
        my_f()


subs()
