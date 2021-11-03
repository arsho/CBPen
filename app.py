from flask import Flask, render_template, request
import sys
from controller import get_top_ports, get_service_version, get_subdomains, get_ssl_certificates
from utils import get_formatted_time
from configurations import get_allowed_sites, get_contributors, get_terms, get_policies

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/port', methods=['GET', 'POST'])
def get_ports():
    sites = get_allowed_sites()
    if request.method == "POST":
        site = request.form["site"]
        hosts, port_scan_time = get_top_ports(site)
        total_time = get_formatted_time(port_scan_time)
        print("Get top ports from nmap complete for: " + site, file=sys.stderr)
        return render_template(
            'port.html',
            sites=sites,
            site=site,
            hosts=hosts,
            total_time=total_time
        )
    return render_template('port.html', sites=sites)


@app.route('/services', methods=['GET', 'POST'])
def get_services():
    sites = get_allowed_sites()
    if request.method == "POST":
        site = request.form["site"]
        hosts, port_scan_time = get_service_version(site)
        total_time = get_formatted_time(port_scan_time)
        print("Get service version from nmap complete for: " + site, file=sys.stderr)
        return render_template(
            'services.html',
            sites=sites,
            site=site,
            hosts=hosts,
            total_time=total_time
        )
    return render_template('services.html', sites=sites)


@app.route('/subdomains', methods=['GET', 'POST'])
def get_subdomains_ssl():
    sites = get_allowed_sites()
    if request.method == "POST":
        site = request.form["site"]
        subdomains, subdomains_list_time = get_subdomains(site)
        ssl_certificates, ssl_certificates_list_time = get_ssl_certificates(site)
        total_time = get_formatted_time(subdomains_list_time + ssl_certificates_list_time)
        print("Get subdomains, ssl complete for: " + site, file=sys.stderr)
        return render_template(
            'subdomains.html',
            sites=sites,
            site=site,
            total_time=total_time,
            subdomains=subdomains,
            ssl_certificates=ssl_certificates
        )
    return render_template('subdomains.html', sites=sites)


@app.route('/about')
def about():
    contributors = get_contributors()
    return render_template('about.html', contributors=contributors)


@app.route('/terms')
def terms():
    our_terms = get_terms()
    policies = get_policies()
    return render_template('terms.html', terms=our_terms, policies=policies)
