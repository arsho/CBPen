import time
import nmap3
import nmap
import sublist3r
from utils import print_nmap_results


def get_os(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments="-O")
    results = nm[target]['osmatch']
    print_nmap_results("get_os", target, results)
    return results


def get_top_ports(target):
    start_time = time.time()
    nmap3_object = nmap3.NmapHostDiscovery()
    results = nmap3_object.scan_top_ports(target)
    print_nmap_results("scan_top_ports", target, results)

    port_info = []
    for key in results.keys():
        host = {}
        if results[key].get("ports", None):
            host["host"] = key
            host["ports"] = results[key].get("ports", None)
            port_info.append(host)
    total_time = time.time() - start_time
    return port_info, total_time


def get_service_version(target):
    start_time = time.time()
    nmpa3_object = nmap3.Nmap()
    results = nmpa3_object.nmap_version_detection(target)
    print_nmap_results("nmap_version_detection", target, results)

    detail_info = []
    for key in results.keys():
        host = {}
        if results[key].get("ports", None):
            host["host"] = key
            host["os"] = get_os(key)
            host["ports"] = results[key].get("ports", None)
            detail_info.append(host)

    total_time = time.time() - start_time
    return detail_info, total_time


def get_subdomains(target):
    start_time = time.time()
    subdomains = sublist3r.main(target, 40, 'subdomains.txt', ports=None, silent=True, verbose=True,
                                enable_bruteforce=False, engines=None)
    print_nmap_results("subdomains", target, subdomains)
    total_time = time.time() - start_time
    return subdomains, total_time
