# coding=utf-8

import logging

from flask import render_template, Blueprint

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
