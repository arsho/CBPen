from socket import gethostbyname, socket, AF_INET, SOCK_STREAM


def get_open_ports(target, common=False, start_port=80, end_port=81):
    host_ip = gethostbyname(target)
    open_ports = []
    # Common ports
    # 80 (http), 443 (https)
    # SSH (port 22), FTP (port 21)
    # DNS (port 53), POP3 (port 110)
    ports = [80, 443, 22, 21, 53, 110]
    if common == False:
        ports = list([i for i in range(50, 500)])

    for i in ports:
        connection = socket(AF_INET, SOCK_STREAM)
        status = connection.connect_ex((host_ip, i))
        if status == 0:
            open_ports.append(i)
        connection.close()

    return sorted(open_ports)
