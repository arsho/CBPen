from socket import gethostbyname, socket, AF_INET, SOCK_STREAM
import time
import nmap3


def get_open_ports(target, common=False, start_port=80, end_port=81):
    start_time = time.time()
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
    total_time = "{:0.2f}".format(time.time() - start_time)
    return sorted(open_ports), total_time


def get_open_ports_nmap(target):
    start_time = time.time()
    nmap = nmap3.NmapHostDiscovery()
    results = nmap.nmap_portscan_only(target)
    port_info = []
    for key in results.keys():
        host = {}
        if results[key].get("ports", None):
            host["host"] = key
            host["ports"] = results[key].get("ports", None)
            port_info.append(host)
    total_time = "{:0.2f}".format(time.time() - start_time)
    return port_info, total_time
