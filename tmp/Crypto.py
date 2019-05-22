cr_dict = dict(zip([str(i) for i in input()], [str(j) for j in input()]))
cr_dict_inv = dict(zip([str(i) for i in cr_dict.values()], [str(j) for j in cr_dict.keys()]))
print(''.join(cr_dict[i] for i in str(input())), sep='')
print(''.join(cr_dict_inv[i] for i in str(input())), sep='')

