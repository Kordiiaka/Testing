row1 = '295743861'
row2 = '431865927'
row3 = '876192543'
row4 = '387459216'
row5 = '612387495'
row6 = '549216738'
row7 = '763524189'
row8 = '928671354'
row9 = '154938672'

digits = '123456789'
rows_lst = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
print(rows_lst)

def col():
    data = []
    for i in range(len(rows_lst)):
        col = []
        for j in range(len(rows_lst)):
            col.append(rows_lst[j][i])
        data.append(''.join(sorted(col)))
    print(data)
    if not compare_data(data):
        return 'No_from_cols'
    return 'Yes'

def my_f():
    if compare_data(rows_lst):
        return col()
    return 'No_from_my_f'

def subs():
    data = []
    for i in range(0, len(rows_lst),3):
        counter = 0
        for j in [3,6,9]:
            data.append(rows_lst[i][counter:j] + rows_lst[i+1][counter:j] + rows_lst[i+2][counter:j])
            counter +=3
    print(data)

    if compare_data(data):
        return my_f()
    return 'No_from_subs'


def compare_data(data):
    for numbers in data:
        if ''.join(sorted(numbers)) != digits:
            return False
    return True

print(subs())



