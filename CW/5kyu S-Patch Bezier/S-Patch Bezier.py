

def indices(n, d):

    def generate_number(N: int, M: int = n, prefix=None):


        prefix = prefix or []
        if M == 0:
            print(prefix)
            return
        for digit in range(N+1):
            prefix.append(digit)
            generate_number(N, M - 1, prefix)
            prefix.pop()


    c = generate_number(n)
    return c
#     for i in range(len(c)):
#         if sum(c[i]) != d:
#             c[i] = 0
#     answer = []
#     for i in range(len(c)):
#         if c[i] != 0:
#             answer.append(list(c[i]))
#     return answer
#
#
print(indices(4, 16))

