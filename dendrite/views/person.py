from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from cortex.core.models import Person

## FIXME - Propper path to templates
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
        person = Person.objects.get(uid=uid)
        return render_template('person/detail.html',
                                person=person, page='person')

# Register the urls
person_blueprint.add_url_rule('/', view_func=ListView.as_view('list'))
person_blueprint.add_url_rule('/<uid>/', view_func=DetailView.as_view('detail'))
