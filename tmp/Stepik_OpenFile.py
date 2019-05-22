with open('dataset_3363_2.txt') as in_f, open('answer.txt', 'w') as out_f:
    s = in_f.readline()
    tmp_digit = '0'
    tmp_alpha = 0
    for i in range(len(s)):
        if s[i].isalpha():
            out_f.write(str(s[tmp_alpha]) * int(tmp_digit))
            tmp_alpha = i
            tmp_digit = ''
        elif s[i].isdigit():
            tmp_digit += str(s[i])
    out_f.write(str(s[tmp_alpha]) * int(tmp_digit))
