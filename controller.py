from urllib.parse import urljoin
import urllib.request
import json
import time
from requests_futures.sessions import FuturesSession
import nmap3
import nmap
import sublist3r
from sslyze import ServerNetworkLocationViaDirectConnection, ServerConnectivityTester, Scanner, ServerScanRequest, \
    ScanCommand
from utils import print_on_console, get_formatted_time
import sys


def get_multiple_view(ip_addresses, virtual_machines, scan_type, parallel=True):
    start = time.time()
    api_endpoints = []
    vm_index = 0
    scanner_machines = {}
    for ip_address in ip_addresses:
        base = urljoin(virtual_machines[vm_index], scan_type)
        base = base + "json"
        endpoint = urljoin(base, "?site=" + ip_address)
        scanner_machine = "Scanner engine {}".format(vm_index + 1)
        scanner_machines[endpoint] = scanner_machine
        api_endpoints.append(endpoint)
        vm_index += 1
        if vm_index == len(virtual_machines):
            vm_index = 0
    data = dict()
    data["sites"] = []
    if parallel:
        with FuturesSession() as session:
            parallel_data = {}
            for endpoint in api_endpoints:
                parallel_data[endpoint] = session.get(endpoint)
            for endpoint in parallel_data:
                site = endpoint.split("=")[1]
                fetched_result = parallel_data[endpoint].result().content
                api_data = json.loads(fetched_result)
                api_data["site"] = site
                api_data["api_path"] = endpoint
                api_data["scanner"] = scanner_machines[endpoint]
                data["sites"].append(api_data)

    else:
        for endpoint in api_endpoints:
            response = urllib.request.urlopen(endpoint)
            api_data = json.loads(response.read())
            site = endpoint.split("=")[1]
            api_data["site"] = site
            api_data["api_path"] = endpoint
            api_data["scanner"] = scanner_machines[endpoint]
            data["sites"].append(api_data)
    total_time = time.time() - start
    data["total_time"] = get_formatted_time(total_time)
    data["total_scanners"] = min(len(virtual_machines), len(ip_addresses))
    data["scan_type"] = scan_type
    return data


def get_port_view(site):
    hosts, port_scan_time = get_top_ports(site)
    total_time = get_formatted_time(port_scan_time)
    print("Get top ports from nmap complete for: " + site, file=sys.stderr)
    data = {
        "total_time": total_time,
        "hosts": hosts
    }
    return data


def get_service_view(site):
    hosts, port_scan_time = get_service_version(site)
    total_time = get_formatted_time(port_scan_time)
    print("Get service version from nmap complete for: " + site, file=sys.stderr)
    data = {
        "total_time": total_time,
        "hosts": hosts
    }
    return data


def get_subdomain_view(site):
    subdomains, subdomains_list_time = get_subdomains(site)
    ssl_certificates, ssl_certificates_list_time = get_ssl_certificates(site)
    total_time = get_formatted_time(subdomains_list_time + ssl_certificates_list_time)
    print("Get subdomains, ssl complete for: " + site, file=sys.stderr)
    data = {
        "total_time": total_time,
        "ssl_certificates": ssl_certificates,
        "subdomains": subdomains
    }
    return data


def get_os(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments="-O")
    results = nm[target]['osmatch']
    print_on_console("get_os", target, results)
    return results


def get_top_ports(target):
    start_time = time.time()
    nmap3_object = nmap3.NmapHostDiscovery()
    results = nmap3_object.scan_top_ports(target)
    print_on_console("scan_top_ports", target, results)

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
    print_on_console("nmap_version_detection", target, results)

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
    subdomains = list(subdomains)
    print_on_console("subdomains", target, subdomains)
    total_time = time.time() - start_time
    return subdomains, total_time


def get_ssl_certificates(target):
    start_time = time.time()
    certificates = []
    server_location = ServerNetworkLocationViaDirectConnection.with_ip_address_lookup(target, 443)

    # Do connectivity testing to ensure SSLyze is able to connect
    try:
        server_info = ServerConnectivityTester().perform(server_location)
    except Exception as e:
        total_time = time.time() - start_time
        print("Error: " + str(e), file=sys.stderr)
        return certificates, total_time

    scanner = Scanner()
    server_scan_req = ServerScanRequest(
        server_info=server_info, scan_commands={ScanCommand.CERTIFICATE_INFO, ScanCommand.SSL_2_0_CIPHER_SUITES},
    )
    scanner.start_scans([server_scan_req])

    for server_scan_result in scanner.get_results():
        certinfo_result = server_scan_result.scan_commands_results[ScanCommand.CERTIFICATE_INFO]
        for cert_deployment in certinfo_result.certificate_deployments:
            certificates.append(cert_deployment.received_certificate_chain_as_pem[0])
    print_on_console("ssl_certificates", target, certificates)
    total_time = time.time() - start_time
    return certificates, total_time
