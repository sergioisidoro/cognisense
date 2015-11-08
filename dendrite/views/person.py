from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from cortex.core.models import Person, DataBlock

import json

# FIXME - Propper path to templates
person_blueprint = Blueprint('person', __name__,
                             template_folder='../templates/',
                             static_folder='../static',)

class ListView(MethodView):
    def get(self):
        people = Person.objects.all()
        return render_template('person/list.html', people=people,
                               page='person')


class DetailView(MethodView):
    def get(self, uid):
        # person = Person.objects.get(uid=uid)
        person = None
        dummy_data = {
            "tp9": [],
            "tp10": [],
            "fp1": [],
            "fp2": [],
            'timestamp': [],
        }
        return render_template('person/detail.html',
                               person=person, page='person',
                               data=json.dumps(dummy_data))

class DetailHistoryView(MethodView):
    def get(self, uid):
        tp_10_data_blocks = DataBlock.objects(channel_name='tp10')
        lists = (x.data for x in tp_10_data_blocks)
        tp10_values = reduce(lambda x, y: x+y, lists)

        tp_9_data_blocks = DataBlock.objects(channel_name='tp9')
        lists = (x.data for x in tp_9_data_blocks)
        tp9_values = reduce(lambda x, y: x+y, lists)

        fp1_data_blocks = DataBlock.objects(channel_name='fp1')
        lists = (x.data for x in fp1_data_blocks)
        fp1_values = reduce(lambda x, y: x+y, lists)

        fp2_data_blocks = DataBlock.objects(channel_name='fp2')
        lists = (x.data for x in fp2_data_blocks)
        fp2_values = reduce(lambda x, y: x+y, lists)

        person = None
        dummy_data = {
            "tp9": list(tp9_values),
            "tp10": list(tp10_values),
            "fp1": list(fp1_values),
            "fp2": list(fp2_values),
            'timestamp': list(x for x in range(1, len(fp2_values))),
        }
        return render_template('person/history.html',
                               person=person, page='person',
                               data=json.dumps(dummy_data))


class DiagnosticView(MethodView):
    def get(self, uid):
        # person = DataBlock.objects.get()
        person = None
        dummy_data = {
            "tp9": [],
            "tp10": [],
            "fp1": [],
            "fp2": [],
            'timestamp': [],
        }
        return render_template('person/diagnostics.html',
                               person=person, page='person',
                               data=json.dumps(dummy_data))


# Register the urls
person_blueprint.add_url_rule('/', view_func=ListView.as_view('list'))
person_blueprint.add_url_rule(
    '/<uid>/live',
    view_func=DetailView.as_view('live'))
person_blueprint.add_url_rule(
    '/<uid>/history',
    view_func=DetailHistoryView.as_view('histoy_detail'))
person_blueprint.add_url_rule(
    '/<uid>/diagnostics',
    view_func=DiagnosticView.as_view('diagnostics'))
