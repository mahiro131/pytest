from flask import Flask
from flask import current_app
from flask import g
from psycopg2 import connect
from psycopg2.extras import DictCursor


class DBConnectionError(Exception):
    pass

class ConnectDatabase():

    # def __init__(self, host=None, port='5432', db=None, user=None, password=None):
    #     url = 'postgresql://%s:%s@%s:%s/%s' \
    #             % (user, password, host, port, db)

    def __init__(self, host=None, port='5432', db='several', user=None, password=None):

        url = 'postgresql://%s:%s@%s:%s/%s' \
                % (user, password, host, port, db)

        try:
            self.conn = connect(url)
            self.conn.autocommit = True
        except Exception as e:
            raise DBConnectionError('Database not connected. url: %s' % url)

    def close(self):
        # self.conn.rollback()
        pass

    def select_one(self, sql, vals={}):
        cur = self.conn.cursor(cursor_factory=DictCursor)
        cur.execute(sql, vals)
        row = cur.fetchone()
        if row is None:
            return None
        return dict(row)


