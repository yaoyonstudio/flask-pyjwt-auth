from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import app
from app import db

app.config.from_object('app.config')

db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
