import json

from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint
from flask_appbuilder import BaseView as AppBuilderBaseView
from flask_appbuilder import expose
from google.oauth2 import service_account

def get_cred():
    print('')

class demo(AppBuilderBaseView):
    @expose("/", methods=['GET'])
    def main(self):
        return self.render_template('plugin_view/demo.html')
    

bp = Blueprint(
    "test_plugin",
    __name__,
    template_folder='templates'
)

v_appbuilder_view = demo()
v_appbuilder_package = {
    "name": "Manager",
    "category":"Demo Plugin",
    "view":v_appbuilder_view
}

class AirflowDemoPlugin(AirflowPlugin):
    name='demo'
    flask_blueprints=[bp]
    appbuilder_views=[v_appbuilder_package]

if __name__ == '__name__':
    print()
