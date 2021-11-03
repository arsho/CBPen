from flask import Flask, render_template, request, jsonify
from controller import get_port_view, get_service_view, get_subdomain_view
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
        data = get_port_view(site)
        return render_template(
            'port.html',
            sites=sites,
            site=site,
            hosts=data["hosts"],
            total_time=data["total_time"]
        )
    else:
        site = request.args.get('site', default='', type=str)
        if site != "":
            return jsonify(get_port_view(site))
        return render_template('port.html', sites=sites)


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
