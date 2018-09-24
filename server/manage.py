import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from server import app, db

app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['DATABASE_URL'])

# OLD LOCAL DATABASE
#'sqlite:////Users/toddbaldwin/Documents/AyobiFiles/AyobiWeb/server/users.db'

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()