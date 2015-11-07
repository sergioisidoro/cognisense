# coding=utf-8

import logging

from flask import render_template, Blueprint, Response

from cortex.api.event_stream import event_stream


dendrite = Blueprint('dendrite', __name__,
                     static_folder='static',
                     template_folder='templates')


@dendrite.route('/')
def index():
    page = 'overview'
    data = {
        'page': page,
    }
    return render_template('index.html', **data)


@dendrite.route('/event_listener/<tagID>')
def stream(tagID):
    print "Connection started"
    resp = Response(event_stream(tagID), mimetype="text/event-stream")
    return resp
