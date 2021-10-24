from flask import Flask, render_template, flash, redirect, request, url_for, g, \
    Markup, escape
import sys
from controller import get_open_ports, get_open_ports_nmap, get_Os_Info, get_top_ports

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    sites = ["localhost", "scanme.nmap.org", "example.com", "walmart.com", "uab.edu", "Apple.com", "Facebook.com"]
    if request.method == "POST":
        site = request.form["site"]
        # open_ports, total_time = get_open_ports(site, common=True)
        hosts, total_time = get_open_ports_nmap(site)
        #IP will always be first item in json array
        ip = hosts[0]['host']
        # get_Os_Info(ip)
        # print(hosts[0]['host'])
        print("Get data from nmap complete", file=sys.stderr)
        return render_template(
            'index.html',
            sites=sites,
            site=site,
            hosts=hosts,
            total_time=total_time,
            os = get_Os_Info(ip)
        )
    return render_template('index.html', sites=sites)


