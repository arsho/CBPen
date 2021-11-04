from flask import Flask, render_template, request, jsonify
from controller import get_port_view, get_service_view, get_subdomain_view, get_multiple_view
from configurations import get_allowed_sites, get_contributors, get_terms, get_policies, get_scan_types

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/multiple', methods=['GET', 'POST'])
def get_multiple():
    scan_types = get_scan_types()
    if request.method == "POST":
        ip_addresses = [s.strip() for s in request.form["ip_addresses"].split(",")]
        virtual_machines = [s.strip() for s in request.form["virtual_machines"].split(",")]
        scan_type = request.form["scan_type"]
        # To get results in non parallel execution add parallel=False to the following method call
        data = get_multiple_view(ip_addresses, virtual_machines, scan_type)

        return render_template(
            'multiple.html',
            scan_types=scan_types,
            data=data
        )
    else:
        return render_template('multiple.html', scan_types=scan_types)


@app.route('/ports', methods=['GET', 'POST'])
def get_ports():
    sites = get_allowed_sites()
    if request.method == "POST":
        site = request.form["site"]
        data = get_port_view(site)
        return render_template(
            'ports.html',
            sites=sites,
            site=site,
            hosts=data["hosts"],
            total_time=data["total_time"]
        )
    else:
        site = request.args.get('site', default='', type=str)
        if site != "":
            return jsonify(get_port_view(site))
        return render_template('ports.html', sites=sites)


@app.route('/services', methods=['GET', 'POST'])
def get_services():
    sites = get_allowed_sites()
    if request.method == "POST":
        site = request.form["site"]
        data = get_service_view(site)
        return render_template(
            'services.html',
            sites=sites,
            site=site,
            hosts=data["hosts"],
            total_time=data["total_time"]
        )
    else:
        site = request.args.get('site', default='', type=str)
        if site != "":
            return jsonify(get_service_view(site))
        return render_template('services.html', sites=sites)


@app.route('/subdomains', methods=['GET', 'POST'])
def get_subdomains_ssl():
    sites = get_allowed_sites()
    if request.method == "POST":
        site = request.form["site"]
        data = get_subdomain_view(site)
        return render_template(
            'subdomains.html',
            sites=sites,
            site=site,
            total_time=data["total_time"],
            subdomains=data["subdomains"],
            ssl_certificates=data["ssl_certificates"]
        )
    else:
        site = request.args.get('site', default='', type=str)
        if site != "":
            return jsonify(get_subdomain_view(site))
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
