with open('dataset_3363_3.txt') as in_f, open('answer.txt', 'w') as out_f:
    s = sorted(in_f.read().replace('\n', ' ').lower().split())
    freq = max(set(s.count(i) for i in s))
    for i in s:
        if s.count(i) == freq:
           ans = [str(i), str(freq)]
           out_f.writelines(' '.join(ans))
           break

