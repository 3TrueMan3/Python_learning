def camel_case(string):
    list = string.split()
    cap_list = []
    for i in range(len(list)):
        cap_list.append(list[i].capitalize())
    answer = ''.join(cap_list)
    return print(answer)
camel_case('test case')