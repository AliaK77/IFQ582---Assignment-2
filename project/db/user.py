from .connection import cursor, connection
from ..models.user import User

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


def add_public_user(form):
   '''Receives the public user form and creates the user'''
   conn = connection()
   cur = conn.cursor()
   
   try:
      # Create parent user
      cur.execute("""
         INSERT INTO users (first_name, last_name, email, phone, password)
         VALUES (%s, %s, %s, %s, %s, %s)
      """, 
      (form.first_name.data, form.last_name.data, form.email.data, form.phone.data, form.password.data))
      
      # Fetch newly created user ID
      row = cur.fetchone()
      if not row.ID:
         conn.rollback()
         raise Exception("No user ID received back")
      
      # Create public user
      cur.execute("""
         INSERT INTO public_user (user_id)
         VALUES (%s)
      """, (row.ID))
      conn.commit()
      
   except conn.Error as e:
      conn.rollback()
      print(f"Transaction failed with error: {e}")
   finally:
      cur.close()

