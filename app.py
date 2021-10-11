from flask import Flask, render_template, flash, redirect, request, url_for, g, \
    Markup, escape
from controller import get_open_ports

app = Flask(__name__)


@app.route('/')
def index():
    site = "scanme.nmap.org"
    open_ports = get_open_ports(site, common=True)
    return render_template(
        'index.html',
        site=site,
        open_ports=open_ports
    )
