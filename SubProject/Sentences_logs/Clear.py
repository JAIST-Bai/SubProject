def Replace(file, old_str, new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


Replace(r'log1.txt', 'BEAUTIFUL', 'beautiful')
Replace(r'log1.txt', 'HOT', 'hot')
Replace(r'log1.txt', 'LIKE', 'like')
Replace(r'log1.txt', 'SUBJECT_I', 'i')
Replace(r'log1.txt', 'SUMMER', 'summer')
Replace(r'log1.txt', 'SWIM', 'swim')
Replace(r'log1.txt', 'WINTER', 'winter')

Replace(r'log2.txt', 'BEAUTIFUL', 'beautiful')
Replace(r'log2.txt', 'HOT', 'hot')
Replace(r'log2.txt', 'LIKE', 'like')
Replace(r'log2.txt', 'SUBJECT_I', 'i')
Replace(r'log2.txt', 'SUMMER', 'summer')
Replace(r'log2.txt', 'SWIM', 'swim')
Replace(r'log2.txt', 'WINTER', 'winter')

Replace(r'log3.txt', 'BEAUTIFUL', 'beautiful')
Replace(r'log3.txt', 'HOT', 'hot')
Replace(r'log3.txt', 'LIKE', 'like')
Replace(r'log3.txt', 'SUBJECT_I', 'i')
Replace(r'log3.txt', 'SUMMER', 'summer')
Replace(r'log3.txt', 'SWIM', 'swim')
Replace(r'log3.txt', 'WINTER', 'winter')

Replace(r'log4.txt', 'BEAUTIFUL', 'beautiful')
Replace(r'log4.txt', 'HOT', 'hot')
Replace(r'log4.txt', 'LIKE', 'like')
Replace(r'log4.txt', 'SUBJECT_I', 'i')
Replace(r'log4.txt', 'SUMMER', 'summer')
Replace(r'log4.txt', 'SWIM', 'swim')
Replace(r'log4.txt', 'WINTER', 'winter')


def Clear_st_1():
    rule = {'i': 0, 'like': 1, 'summer': 2, 'winter': 3}
    Words = open('log1.txt').read()
    Strip_Words = Words.strip().replace('\n', ',').replace('\r', ',')
    Clear_Words = list(set(list(Strip_Words.split(','))))
    New_List = sorted(Clear_Words, key=lambda x: rule[x])
    for i in New_List:
        if i == 'summer':
            New_List.insert(3, '<mask>')
            continue
        else:
            pass
    New_List.append('.')
    Mask_str_1 = ' '.join(New_List)
    print(Mask_str_1)


def Clear_st_2():
    rule = {'summer': 0, 'hot': 1}
    Words = open('log2.txt').read()
    Strip_Words = Words.strip().replace('\n', ',').replace('\r', ',')
    Clear_Words = list(set(list(Strip_Words.split(','))))
    while True:
        if 'like' in Clear_Words:
            Clear_Words.remove('like')
            continue
        else:
            break
    New_List = sorted(Clear_Words, key=lambda x: rule[x])
    for i in New_List:
        if i == 'summer':
            New_List.insert(1, '<mask>')
            continue
        else:
            pass
    New_List.append('.')
    Mask_str_2 = ' '.join(New_List)
    print(Mask_str_2)


def Clear_st_3():
    rule = {'winter': 0, 'beautiful': 1}
    Words = open('log3.txt').read()
    Strip_Words = Words.strip().replace('\n', ',').replace('\r', ',')
    Clear_Words = list(set(list(Strip_Words.split(','))))
    while True:
        if 'swim' in Clear_Words:
            Clear_Words.remove('swim')
        if 'hot' in Clear_Words:
            Clear_Words.remove('hot')
            continue
        else:
            break
    New_List = sorted(Clear_Words, key=lambda x: rule[x])
    for i in New_List:
        if i == 'winter':
            New_List.insert(1, '<mask>')
            continue
        else:
            pass
    New_List.append('.')
    Mask_str_3 = ' '.join(New_List)
    print(Mask_str_3)


def Clear_st_4():
    rule = {'i': 0, 'like': 1, 'swim': 2, 'summer': 3}
    Words = open('log4.txt').read()
    Strip_Words = Words.strip().replace('\n', ',').replace('\r', ',')
    Clear_Words = list(set(list(Strip_Words.split(','))))
    while True:
        if 'winter' in Clear_Words:
            Clear_Words.remove('winter')
            continue
        else:
            break
    New_List = sorted(Clear_Words, key=lambda x: rule[x])
    for i in New_List:
        if i == 'like':
            New_List.insert(2, '<mask>')
            continue
        else:
            pass
    New_List_copy = New_List.copy()
    for n in New_List_copy:
        if n == 'swim':
            New_List_copy.insert(4, '<mask>')
            continue
        else:
            pass
    New_List_copy.append('.')
    Mask_str_4 = ' '.join(New_List_copy)
    print(Mask_str_4)


if __name__ == "__main__":
    Clear_st_1()
    Clear_st_2()
    Clear_st_3()
    Clear_st_4()
