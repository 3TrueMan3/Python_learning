import os
import os.path
import shutil


print(os.getcwd())
print(os.listdir())
print(os.path.exists('files.py'))

shutil.copy('test1.txt', '.idea/test1_copy.txt')
for current_dir, dirs, files in os.walk('.'):
    print(current_dir, dirs, files)

