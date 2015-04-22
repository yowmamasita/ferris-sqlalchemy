from ferris import plugins, settings
from sqlalchemy import create_engine

plugins.register('sqlalchemy')

db = settings.get('database')
engine = create_engine(db.get('connect_string'), **db.get('args'))
