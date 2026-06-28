from datetime import datetime
import os
from flask_mysqldb import MySQL
from .connection import cursor

### Global mysql variable, initialised in set_up_database
mysql: MySQL

def get_env_contents(app):
   '''Gets contents of an .env file and puts them in app context for MySQL'''
   if not os.path.exists(".env"):
      raise Exception("Could not locate .env file; please put it in project root.")
   config: dict[str, str | None] = {
      'MYSQL_HOST': None,
      'MYSQL_USER': None,
      'MYSQL_PASSWORD': None,
      'MYSQL_DB': None,
   }
   with open(".env") as f:
      for line in f:
         key, value = line.strip().split("=", 1)
         if key in config:
            if not value:
               raise Exception("Your .env file needs to specify " + key)
            app.config[key] = value
         else:
            raise Exception("Your .env file contains an unrecognised item called" + value)

   app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


def set_up_database(app):
   '''Sets up the database connection and ensures it works, raising errors if it doesn't'''
   global mysql
   get_env_contents(app)

   ### Initialise the mysql global variable
   mysql = MySQL(app)

   with app.app_context():
      # Above is only needed here because db is called outside a route handler.
      # Normally Flask supplies it behind the scenes.
      test_connection()


def test_connection():
   try:
      cur = cursor()
      cur.execute('Select 1')
      cur.close()
   except:
      raise Exception("Database connection failed.")
