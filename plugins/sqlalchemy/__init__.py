from ferris import plugins, settings
from sqlalchemy import create_engine

plugins.register('sqlalchemy')

db = settings.get('database')
params = (db.get('username'), db.get('password'), db.get('host'), db.get('name'))
engine = create_engine('mysql://%s:%s@%s/%s' % params, echo=db.get('echo'),
                       pool_size=10, max_overflow=2)  # Cloud SQL limits
