with open('dataset_24465_4.txt', 'r') as straight, open('reversed.txt', 'w') as rev:

    rev.write('\n'.join(str(i).strip() for i in straight.readlines()[::-1]))
