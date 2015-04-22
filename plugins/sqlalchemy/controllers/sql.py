from ferris import Controller, BasicModel, route_with, messages
from ..model import SQLModel
from .. import engine
import os
import glob


class Sql(Controller):
    class Meta:
        Model = BasicModel
        prefixes = ('api',)
        components = (messages.Messaging,)

    def load_all_sql_models(self):
        models_path = os.path.join(os.path.dirname(__file__), '../' * 3, 'app', 'models')
        module_names = glob.glob(models_path + '/*_sql.py')
        modules = [os.path.basename(f)[:-3] for f in module_names]
        for model in modules:
            __import__('app.models.%s' % model, fromlist=['*'])

    @route_with('/_sql/create_tables')
    def api_create_tables(self):
        self.load_all_sql_models()
        SQLModel.metadata.create_all(engine)
        return 200

    @route_with('/_sql/drop_tables')
    def api_drop_tables(self):
        self.load_all_sql_models()
        SQLModel.metadata.drop_all(engine)
        return 200
