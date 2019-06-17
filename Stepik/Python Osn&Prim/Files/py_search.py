import os.path
os.chdir('task/main')
for current_dir, dirs, files in os.walk('.'):
    for i in range(len(files)):
        if files[i][-3:] == '.py':
            with open('task/answer_search_py.txt', 'a') as ans:
                ans.write(current_dir + '\n')