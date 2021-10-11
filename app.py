import time
from flask import Flask, render_template, flash, redirect, request, url_for, g, \
    Markup, escape

app = Flask(__name__)


@app.route('/')
def index():
    time_in_seconds = time.localtime()
    current_time = time.strftime("%H:%M:%S", time_in_seconds)
    message = "(Update) Current time: {}".format(current_time)
    return render_template(
        'index.html', data=message
    )
