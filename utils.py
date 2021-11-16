import json
from socket import gethostbyname, socket, AF_INET, SOCK_STREAM
import time
import sys
import requests


def is_url_available(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except Exception as ex:
        print(str(ex))
        return False
    return False


def print_on_console(method_name, target, results, json_output=True):
    print("*" * 12, file=sys.stderr)
    print("{} for {}".format(method_name, target), file=sys.stderr)
    if json_output:
        print(json.dumps(results, indent=4), file=sys.stderr)
    else:
        print(results, file=sys.stderr)
    print("=" * 12, file=sys.stderr)


def get_formatted_time(value):
    return "{:0.2f}".format(value)


def get_open_ports(target, common=False, start_port=80, end_port=100):
    start_time = time.time()
    host_ip = gethostbyname(target)
    open_ports = []
    # Common ports
    # 80 (http), 443 (https)
    # SSH (port 22), FTP (port 21)
    # DNS (port 53), POP3 (port 110)
    ports = [80, 443, 22, 21, 53, 110]
    if not common:
        ports = list([i for i in range(start_port, end_port)])

    for i in ports:
        connection = socket(AF_INET, SOCK_STREAM)
        status = connection.connect_ex((host_ip, i))
        if status == 0:
            open_ports.append(i)
        connection.close()
    total_time = time.time() - start_time
    return sorted(open_ports), total_time
