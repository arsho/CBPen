import nmap3
import time
from utils import print_nmap_results


def get_top_ports(target):
    start_time = time.time()
    nmap = nmap3.NmapHostDiscovery()
    results = nmap.scan_top_ports(target)
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
    nmap = nmap3.Nmap()
    results = nmap.nmap_version_detection(target)
    print_nmap_results("nmap_version_detection", target, results)

    port_info = []
    for key in results.keys():
        host = {}
        if results[key].get("ports", None):
            host["host"] = key
            host["ports"] = results[key].get("ports", None)
            port_info.append(host)

    total_time = time.time() - start_time
    return port_info, total_time


def get_host_discovery_results(target):
    start_time = time.time()
    nmap = nmap3.NmapHostDiscovery()
    results = nmap.nmap_portscan_only(target)
    print_nmap_results("nmap_portscan_only", target, results)
    #
    # results = nmap.nmap_no_portscan(target)
    # print_nmap_results("nmap_no_portscan", target, results)
    #
    # results = nmap.nmap_disable_dns(target)
    # print_nmap_results("nmap_disable_dns", target, results)

    port_info = []
    for key in results.keys():
        host = {}
        if results[key].get("ports", None):
            host["host"] = key
            host["ports"] = results[key].get("ports", None)
            port_info.append(host)

    total_time = time.time() - start_time
    return port_info, total_time
