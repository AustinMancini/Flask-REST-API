from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from server import create_app, db


app = create_app('config')

# Init Migrate with app & db
migrate = Migrate(app, db)
manager = Manager(app)

# Connect manager & migrate
manager.add_command('db', MigrateCommand)


# Start manager
if __name__ == '__main__':
    manager.run()