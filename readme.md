# Ferris-SQLAlchemy

Basic Ferris plugin for [SQLAlchemy](http://www.sqlalchemy.org/)

## Configuration

Configure database connection in `settings.py`

```
local = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

if local:
    settings['database'] = {
        'connect_string': 'mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>',
        # show SQL statements
        'args': {
            'echo': True,
        },
    }
else:
    settings['database'] = {
        'connect_string': 'mysql+gaerdbms:///<dbname>?instance=<instancename>',
        'args': {},
    }
```

## Models

Place your SQLAlchemy models in `app/models` and follow this naming format `*_sql.py`, ex: `user_sql.py`

```
from plugins.sqlalchemy.model import SQLModel
from sqlalchemy import Column, Integer, String


class User(SQLModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(12))
```

To create tables for all your models, visit `/_sql/create_tables` (only nonexistent tables are created)

To drop *ALL* tables and their data, visit `/_sql/drop_tables`

## Controllers

You can use the `SQLAlchemy` component included in the plugin to access a SQLAlchemy session instance. You can use this through `self.db_session` inside your routes to "stage" and commit your changes to the database.

```
from ferris import Controller, BasicModel, messages, route
from plugins.sqlalchemy.component import SQLAlchemy
from app.models.user_sql import User


class Users(Controller):
    class Meta:
        prefixes = ('api',)
        Model = BasicModel
        components = (messages.Messaging, SQLAlchemy,)

    @route
    def api_test(self):
        ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')
        self.db_session.add(ed_user)
        self.db_session.commit()
        return 200
```

## TODO

* protorpc integration
