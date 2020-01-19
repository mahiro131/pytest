from .database import ConnectDatabase
from flask import Flask,current_app,g
from flask.cli import with_appcontext

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('C:\\Users/Otani.Masahiro/mdsystem/pytest/voteboo/config/config_file.cfg')   # ここが微妙。。


# database.pyからConnectDatabaseのインスタンスを作る

def get_db(name='default'):

    vars = {
            'host': app.config['DB_HOST'],
            'port': app.config['DB_PORT'],
            'db': app.config['DB_NAME'],
            'user': app.config['DB_USER'],
            'password': app.config['DB_PASS'],
        }

    db = ConnectDatabase(**vars)

    return db


# db = get_db()
# print(db.select_one("select * from test_table"))
