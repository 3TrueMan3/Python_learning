import re

# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)

# [] -- можно указать множество подходящих символов
# . ^ $ * + ? { } [ ] \ | ( ) -- метасимволы
# ^ -- исключить из поиска, НЕ
# \d ~ [0-9] -- цифры
# \D ~ [^0-9]
# \s ~ [ \t\n\r\f\v] -- пробельные символы
# \S ~ [^\t\n\r\f\v]
# \w ~ [a-zA-z0-9_] -- буквы + цифры + _
# \W ~ [^a-zA-z0-9_]
# . -- все метасимволы


pattern = r'a[\w.-]c'
string = 'acc'
match_object = re.match(pattern, string)
print(match_object)

string = 'abc, a.c, aac, a_c, a-c, aBc, azc'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, 'abc', string)
print(fixed_typos)
print()

pattern = r'ab{1}a'
# * после символа указывает на любое, включая 0, количество вхождения символа
# если 0 вхождений не нужно, то используется метасимвол +
# если интересует 0 или 1 включение, то используется метасимвол ?
# если интересует конкретное кол-во вхождений, то используется {}, где внутри скобок вставляется необходимое значение

string = 'aa, aba, abba, abbba, abbbba'
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
print()

