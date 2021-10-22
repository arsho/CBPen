from socket import gethostbyname, socket, AF_INET, SOCK_STREAM
import time
import nmap3
import nmap


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
    results = nmap.nmap_arp_discovery(target)
    port_info = []
    for key in results.keys():
        host = {}
        if results[key].get("ports", None):
            host["host"] = key
            host["ports"] = results[key].get("ports", None)
            port_info.append(host)
    total_time = "{:0.2f}".format(time.time() - start_time)
    return port_info, total_time

# def ports(target):

# # initialize the port scanner
#     nmap = nmap3.PortScanner(target)

#     # scan localhost for ports in range 21-443
#     nmap.scan('127.0.0.1', '21-443')

#     # run a loop to print all the found result about the ports
#     for host in nmap.all_hosts():
#         print('Host : %s (%s)' % (host, nmap[host].hostname()))
#         print('State : %s' % nmap[host].state())
#         for proto in nmap[host].all_protocols():
#             print('----------')
#             print('Protocol : %s' % proto)

#             lport = nmap[host][proto].keys()
#             lport.sort()
#             for port in lport:
#                 print ('port : %s\tstate : %s' % (port, nmap[host][proto][port]['state']))
#                 results = nmap3.ports(target)

def get_Os_Info(target):
    start_time = time.time()
    nmap = nmap3.NmapHostDiscovery()
    results = nmap.nmap_os_detection(target)
    port_info = []
    for key in results.keys():
        host = {}
        if results[key].get("ports", None):
            host["host"] = key
            host["ports"] = results[key].get("ports", None)
            port_info.append(host)
    total_time = "{:0.2f}".format(time.time() - start_time)
    return port_info, total_time

def get_top_ports(target):
    start_time = time.time()
    nmap = nmap3.NmapHostDiscovery()
    results = nmap.scan_top_ports(target)
    port_info = []
    for key in results.keys():
        host = {}
        if results[key].get("ports", None):
            host["host"] = key
            host["ports"] = results[key].get("ports", None)
            port_info.append(host)
    total_time = "{:0.2f}".format(time.time() - start_time)
    return port_info, total_time