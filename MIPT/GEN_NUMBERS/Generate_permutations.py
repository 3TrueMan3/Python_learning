def find(number, A):
    """ищет number в А и возвращает True, если такой есть, иначе false """
    for x in A:
        if number == x:
            return True
    return False

def generate_permutations (N: int, M: int=-1, prefix=None):
    """Генерация всех перестановок N чисел в M посициях, с префиксом prefix"""
    if M == -1:
        M = N           #по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()


generate_permutations(4)

