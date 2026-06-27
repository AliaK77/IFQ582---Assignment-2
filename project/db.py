from datetime import datetime
import os
from flask_mysqldb import MySQL
from .models.user import User

mysql: MySQL

def get_env_contents(app):
   '''Gets contents of an .env file and puts them in app context for MySQL'''
   if not os.path.exists(".env"):
      raise Exception("Could not locate .env file; please put it in project root.")
   with open(".env") as f:
      for line in f:
         key, value = line.strip().split("=", 1)
         os.environ[key] = value

   def set_in_app_config(key):
      value = os.getenv(key)
      if not key:
         raise Exception("Your .env file needs to specify " + key)
      app.config[key] = value

   set_in_app_config('MYSQL_HOST')
   set_in_app_config('MYSQL_USER')
   set_in_app_config('MYSQL_PASSWORD')
   set_in_app_config('MYSQL_DB')
   app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


def set_up_database(app):
   '''Sets up the database connection and ensures it works, raising errors if it doesn't'''
   global mysql
   get_env_contents(app)
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


def connection():
   '''Supplies a database connection with no type errors'''
   assert mysql.connection is not None
   return mysql.connection


def cursor():
   '''
   Supplies a more compact cursor without the extra connection code, when
   the connection is not needed later.
   '''
   return connection().cursor()


def check_for_user(email, password):
    cur = cursor()
    cur.execute("""
        SELECT user_id, first_name, last_name, email, phone
        FROM user
        WHERE email = %s AND password = %s
    """, (email, password))
    row = cur.fetchone()
    cur.close()
    if row:
        return User(row['first_name'], row['last_name'], row['email'], row['phone'], password)
    return None


def add_user(form):
    conn = connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (first_name, last_name, email, phone, password)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, 
    (form.first_name.data, form.last_name.data, form.email.data, form.phone.data, form.password.data))
    conn.commit()
    cur.close()
