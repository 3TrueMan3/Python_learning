import socket


serv_sock = socket.socket(socket.AF_INET,       # задаём семейство протоколов "Интернет" (INET)
                          socket.SOCK_STREAM,   # задаем тип передачи данных 'потоковый' (TCP)
                          proto=0)              # выбираем протокол 'по умолчанию' для TCP, т.е.
serv_sock.bind(('127.0.0.1', 53210))            # привязка сокета к локальному IP и открываем порт для соединения
                                                # для привязки ко всем портам используем ''

serv_sock.listen(10)                            # прослушка сокета, 10 - размер очереди входящих подключений

while True:
    # Бесконечно обрабатываем входящие подключения
    client_sock, client_addr = serv_sock.accept()
    print('Connected by', client_addr)

    while True:
        # Пока клиент не отключился, читаем передаваемые
        # им данные и отправляем их обратно
        data = client_sock.recv(1024)
        if not data:
            # Клиент отключился
            break
        client_sock.sendall(data)

    client_sock.close()