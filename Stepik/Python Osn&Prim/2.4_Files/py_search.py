import os.path
os.chdir('task')
answer_set = set()
for current_dir, dirs, files in os.walk('.'):
    for i in range(len(files)):
        if files[i][-3:] == '.py':
            answer_set.add(str(current_dir))
with open("answer_search_py.txt", 'w') as ans:
    ans.write('\n'.join(str(i) for i in sorted(answer_set)))